
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from fun_db import create_table,add_data,view_all_products,view_all_products_names,get_product,edit_product_data,delete_data,view_all_orders,view_all_prior,view_all_customers,get_customer

orders = pd.DataFrame(view_all_orders(),columns=["order_id","user_id","eval_set","order_number","order_dow","order_hour_of_day","days_since_prior_order"])
orders_prior=pd.DataFrame(view_all_prior(),columns=["order_id","product_id","add_to_cart_order",	"reordered","user_id","order_number","order_dow","order_hour_of_day","days_since_prior_order"])
products = pd.DataFrame(view_all_products(),columns=["product_id","product_name","aisle_id","department_id"])
#prior=pd.read_csv('/Users/ronimalihi/Desktop/project/t/order_products_prior.csv')
customers = pd.DataFrame(view_all_customers(),columns=["user_id","Gender","Age","District"])

cus_ord =  customers
cus_ord = cus_ord.merge(orders[['order_id','user_id', 'order_number', 'order_dow',
       'order_hour_of_day', 'days_since_prior_order']], on = 'user_id')


customer_orders = cus_ord.groupby('user_id')['order_id'].count()


#orders_prior =  prior
#orders_prior = orders_prior.merge(orders[['order_id','user_id', 'order_number', 'order_dow',
 #     'order_hour_of_day', 'days_since_prior_order']], on = 'order_id')
#orders_prior = orders_prior.fillna(value = 0)
#orders_prior.to_csv('/Users/ronimalihi/Desktop/project/t/final_prior.csv')

customer_total_products = orders_prior.groupby('user_id')['product_id'].count()

customer_distinct_products = orders_prior.groupby('user_id')['product_id'].nunique()

df = pd.concat([customer_orders, customer_total_products], axis=1)

df = df.rename(columns={"order_id": "customer_orders","product_id": "customer_total_products"})


df["customer_distinct_products"] = customer_distinct_products
df = df.dropna()

df["customer_average_basket"] = df["customer_total_products"] / df["customer_orders"]


##customer_features
#customers = pd.get_dummies(customers, columns = ['Gender', 'District'], drop_first= True )
#genders = pd.get_dummies(genders)
#districts = pd.get_dummies(districts)

#df = df.merge(customers[['user_id', 'Age']], on = 'user_id')
#df = df.merge(genders, on = 'user_id')
#df = df.merge(districts, on = 'user_id')

#orders_prior.to_csv(index=False)
#orders_prior.to_csv (r'/Users/ZOHAR/OneDrive/שולחן העבודה/export_dataframe.csv', index = False, header=True)


#df = df.set_index('user_id')
#All correlations in df 
correlation_df = df.corr()
#רואים שהעמודות דיסטינקט וטוטל ממש דומות, אולי בהמשך נוותר על אחת



scaler = MinMaxScaler()
scaler.fit(df)
df= pd.DataFrame(scaler.transform(df), index=df.index, columns=df.columns)
                                                                                                                                                                                
#df = df.merge(customers, on = 'user_id')

#id = df['user_id']
#df = df.drop(columns ='user_id')
#df = df.drop(columns= 'Age_y')


#aisle_vol_pivot = aisle_vol_pivot.fillna(value = 0)
X = df
X.info()

#kmeans clustering

ks = range(2,11) #hit and trial, let's try it 10 times.
inertias = []
for k in ks:
    model = KMeans(n_clusters=k, init='k-means++', max_iter=100).fit(X)
   # Create a KMeans instance with k clusters: model
                       # Fit model to samples
    inertias.append(model.inertia_) # Append the inertia to the list of inertias

plt.plot(ks, inertias, '-o', color='black') #Plotting. The plot will give the 'elbow'.
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
plt.show()



kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=100)
kmeans.fit(X) # fitting the Kmeans algorithm to our data (the clustering Process)
pred = kmeans.fit_predict(X)
clusters= kmeans.fit_transform(X)
cluster_df = pd.DataFrame(clusters)


#cluster correlations check
#cluster_correlation_df = cluster_df.corr()


#check model quality 
print(kmeans.inertia_) #returns the SSE value (The lesser the model inertia, the better the model fit.)



frame = pd.DataFrame(X)
cluster_df['cluster'] = pred
frame['cluster']= pred
cluster_df = pd.concat([pd.Series(X.index),cluster_df],axis=1)


#כמה בכל קלאסטר
pd.DataFrame(cluster_df['cluster'].value_counts().reset_index())

#חלוקת קלאסטרים
cluster_df['cluster'].value_counts().sort_index() / cluster_df['cluster'].value_counts().sum() * 100

#########################RECOMMENDATIONS####################################



def get_cluster(index):
    user_line = cluster_df.loc[cluster_df['user_id'] == index]
    user_cluster = user_line['cluster'].values
    user_cluster = int(user_cluster)
    
    return user_cluster





def get_recommendations(user_id, n): #n- num of recommended products
    row_list = []

    C = get_cluster(user_id)
    clusterC= cluster_df[cluster_df['cluster'].isin([C])]
    clusterC = clusterC.merge(orders, on = 'user_id')
    clusterC = clusterC.merge(orders_prior, on = 'order_id')
    clusterC = clusterC[clusterC.reordered == 0]
    # get top n most frequent products(id)
    rec_list = clusterC['product_id'].value_counts()[:5].index.tolist()
    
    # print recommended products for cluster C
    for x in rec_list:
        row_list.append(products[products["product_id"] == x])
        rec = pd.concat(row_list)
    #user_rec = recom.loc[recom["cluster"] == c]
    return rec
                        

def get_cluster_recommendations(C, n): #n- num of recommended products
    row_list = []

    
    clusterC= cluster_df[cluster_df['cluster'].isin([C])]
    clusterC = clusterC.merge(orders, on = 'user_id')
    clusterC = clusterC.merge(orders_prior, on = 'order_id')
    
    # get top n most frequent products(id)
    rec_list = clusterC['product_id'].value_counts()[:n].index.tolist()
    
    # print recommended products for cluster C
    for x in rec_list:
        row_list.append(products[products["product_id"] == x])
        rec = pd.concat(row_list)
    #user_rec = recom.loc[recom["cluster"] == c]
    return rec
                        

