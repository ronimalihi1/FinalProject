#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 10:59:59 2021

@author: ronimalihi
"""
import streamlit as st
st.set_page_config(layout="centered")

import sqlite3
import pandas as pd
import smtplib as s
import sklearn as sk
from PIL import Image

# DB Management
conn7 = sqlite3.connect('data.db')
c7 = conn7.cursor()


import pandas as pd

import streamlit.components.v1 as components




#from fun_db import create_table,add_data,view_all_products,view_all_products_names,get_product,edit_product_data,delete_data,view_all_orders,view_all_prior,view_all_customers,get_customer,view_all_customers_names
#from project2 import get_cluster,get_recommendations
    ### customers tables ###

	###############
	
conn = sqlite3.connect('products.db')
c = conn.cursor()

conn3=sqlite3.connect('priortestt.db')
c3=conn3.cursor()

conn4=sqlite3.connect('orders.db')
c4=conn4.cursor()

conn2= sqlite3.connect('customers.sqlite')
c2= conn2.cursor()



def view_all_customers():
    c2.execute('SELECT * FROM Mall_Customers')
    data = c2.fetchall()
    return data


def view_all_customers_names():
	c2.execute('SELECT DISTINCT user_id FROM Mall_Customers')
	data = c2.fetchall()
	return data

def get_customer(user_id):
	c2.execute('SELECT * FROM Mall_Customers WHERE user_id="{}"'.format(user_id))
	data = c2.fetchall()
	return data

def view_all_orders():
    c4.execute('SELECT * FROM orders')
    data = c4.fetchall()
    return data


def view_all_prior():
    c3.execute('SELECT * FROM final_prior')
    data = c3.fetchall()
    return data


def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS products(product_id INT NOT NULL ,product_name TEXT, aisle_id INT, department_id INT)')

def add_data(product_id,product_name,aisle_id,department_id):
	c.execute('INSERT INTO products(product_id,product_name,aisle_id,department_id) VALUES (?,?,?,?)',(product_id,product_name,aisle_id,department_id))
	conn.commit()



def view_all_products():
    c.execute('SELECT * FROM products')
    data = c.fetchall()
    return data


def create_tabletest():
	c.execute('CREATE TABLE IF NOT EXISTS lili(department_id INT NOT NULL ,department TEXT)')

def view_all_cus():
    c.execute('SELECT * FROM lili')
    data = c.fetchall()
    return data



def view_all_products_names():
	c.execute('SELECT DISTINCT product_id FROM products')
	data = c.fetchall()
	return data

def get_product(product_id):
	c.execute('SELECT * FROM products WHERE product_id="{}"'.format(product_id))
	data = c.fetchall()
	return data




def edit_product_data(new_productid,new_productname,new_aisleid,new_depid,product_id,product_name,aisle_id,department_id):
	c.execute("UPDATE products SET product_id =?,product_name=?,aisle_id=? , department_id=? WHERE product_id =? and product_name=? and aisle_id=? and department_id=? ",(new_productid,new_productname,new_aisleid,new_depid,product_id,product_name,aisle_id,department_id))
	conn.commit()
	data = c.fetchall()
	return data

def delete_data(product_id):
	c.execute('DELETE FROM products WHERE product_id="{}"'.format(product_id))
	conn.commit()
    ###########

from project2 import get_recommendations,get_cluster,get_cluster_recommendations

import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False

# You can also use the verify functions of the various libraries for the same purpose

def create_usertable():
	c7.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')
def create_managerstable():
	c7.execute('CREATE TABLE IF NOT EXISTS managerstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c7.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn7.commit()
def add_managerdata(username,password):
        c7.execute('INSERT INTO managerstable(username,password) VALUES (?,?)',(username,password))
        conn7.commit()

def login_user(username,password):
	c7.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c7.fetchall()
	return data
def login_manager(username,password):
	c7.execute('SELECT * FROM managerstable WHERE username =? AND password = ?',(username,password))
	data = c7.fetchall()
	return data
def view_all_users():
    c7.execute('SELECT * FROM userstable')
    data = c7.fetchall()
    return data
def view_all_managers():
    c7.execute('SELECT * FROM managerstable')
    data = c7.fetchall()
    return data
#from sklearn.feature_extraction.text import CountVectorizer
#from sklearn.metrics.pairwise import cosine_similarity,linear_kernel
def get_user(username):
        c7.execute('SELECT * FROM userstable WHERE username="{}"'.format(username))
        data = c7.fetchall()
        return data
def view_all_usersnames():
	c7.execute('SELECT DISTINCT username FROM userstable')
	data = c7.fetchall()
	return data
def load_data(data):
    df=pd.read_csv(data)
    return df

#def vectorize_text(data):
 #   count_vect = CountVectorizer()
  #  cv_mat= count_vect.fit_transform(data)
  #  cosine_sim= cosine_similarity(cv_mat) 
  #  return cosine_sim
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#########################RECOMMENDATIONS####################################





import streamlit.components.v1 as stc





def main():
    
    


    menu2=["Home","Customers Details","Products","Settings"]
    choice2 = st.sidebar.selectbox("Menu",menu2)

    menu = ["Login As Manager","Login As User"]
    choice = st.sidebar.selectbox("Login",menu)
    HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">Company Profile </h1>
    </div>
    """
    title_container = st.container()
    col1, col2 = st.columns([1,20])
    #st.image(image, width=120)  
    image = Image.open('test.PNG') 
    st.image(image, width=120)     
       
    st.markdown('<div style="color: black;text-align:left;">•Data •Insights •Recommendations</div>',
                            unsafe_allow_html=True)             

    import seaborn as sns
    import matplotlib.pyplot as plt
    import numpy as np
    if choice2 == "Home":
      

        stc.html(HTML_BANNER)
        
       # st.markdown("<h1 style='text-align: center; color: black;'>Company Profile</h1>", unsafe_allow_html=True)
       



        st.write("Retail Recommender System \n\n\n - Boost your revenue using AI \n\n\n - Get insights about your business to boost repeat purchases, encourage bigger spending and win back customers. \n\n\n - Specific personal offers for your customers.")

      #  s1,s2= st.columns(2)
                        
      #  with s1:
        with st.expander("About",expanded=False):
            st.write('Established in 2021, DIR is a retail recommender system offering artificial intelligence solutions to local and international businesses.')
                              
      #  with s2:
        with st.expander("Contact",expanded=False):
            st.write('Feel free to contact us in the following communication channels: \n\n Email: DIR@gmail.com \n\n Phone: 0505555555')
                
             


        
       
                
                
        

    if choice == "Login As User" or choice == "Login As Manager":

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        #if choice == "Login As Manager":
        if st.sidebar.checkbox("Login"):
                  # if st.sidebar.checkbox("Login"):
                    # if password == '12345':
            create_usertable()
            create_managerstable()
            
                       
            hashed_pswd = make_hashes(password)
            result = login_user(username,check_hashes(password,hashed_pswd))
                #result2 = login_manager(username,check_hashes(password,hashed_pswd))
            
               
            if choice=="Login As Manager":
              
                    # if password == '12345':
                       # create_usertable()
                       create_managerstable()
        
                   
                       hashed_pswd = make_hashes(password)
                       #result = login_user(username,check_hashes(password,hashed_pswd))
                       result2 = login_manager(username,check_hashes(password,hashed_pswd))
                       if result2:
                           if choice2 == "Settings":
                            task = st.selectbox("task",["Users Profile","SignUp New User"])
                            if task== "Users Profile":
                                st.subheader("User Profiles")
                                user_result = view_all_users()
                                clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
                                st.dataframe(clean_db)
                                st.subheader("Managers Profiles")
                                manager_results= view_all_managers()
                                clean_dc2=pd.DataFrame(manager_results,columns=["Username","Password"])
                                st.dataframe(clean_dc2)
                            elif task == "SignUp New User":
                                t= st.selectbox("task",["Open User account", "Open Manager account"])
                                new_user = st.text_input("Username",key='1')
                                new_password = st.text_input("Password",type='password',key='2')
                                user_exsit= get_user(new_user)
                                if user_exsit:
                                  st.warning("You Can't Use This USERNAME, Please choose another one ")

                                elif st.button("Signup"):
                                    if t == "Open User account":
                                        st.subheader("Create New User Account")
                                        
                                        create_usertable()
                                        add_userdata(new_user,make_hashes(new_password))

                                    elif t == "Open Manager account":
                                        st.subheader("Create New User Account")
                                       
                                        create_usertable()
                                        create_managerstable()
                                        add_userdata(new_user,make_hashes(new_password))
                                        add_managerdata(new_user,make_hashes(new_password))
					
                             elif task == "Delete":
                                        
                                 with st.expander("View Data"):
                                     result = view_all_users()
                                    			# st.write(result)
                                     clean_df = pd.DataFrame(result,columns=["username","password"])
                                     st.dataframe(clean_df)
                                    
                                 unique_list = [i[0] for i in view_all_usersnames()]
                                 delete_by_users_name =  st.selectbox("Select username",unique_list)
                                 if st.button("Delete"):
                                    delete_data(delete_by_users_name)
                                    st.warning("Deleted: '{}'".format(delete_by_users_name))
                                    
                                 with st.expander("Updated Data"):
                                     result = view_all_users()
                                    			# st.write(result)
                                     clean_df = pd.DataFrame(result,columns=["username","password"])
                                     st.dataframe(clean_df)
                                    
                               
                                       
    
                                    
            		   	               
       
                   
              #  if st.sidebar.checkbox("Login"):
        
                # if st.sidebar.checkbox("Login"):
                        # if password == '12345':
               
                            
                #elif choice == "Login As Manager":
                
            if result:
                 
                st.sidebar.success("Logged In as {}".format(username))                
          
                  
                #Union of all the relevent tables
                               
                                              #  menu = ["Products","Customers Data"]
                   # choice = st.sidebar.selectbox("Menu",menu)
                    
                   # st.subheader("What do you want to do?")
                   # col1,col2 = st.beta_columns(2)
                   # with col1:
                        
                      #  task = st.selectbox("Analytics Data",["Clusters Data","Products Data","Profiles"])
                   # with col2:
                      #  product_task=st.selectbox("Products Data",["Clusters Data","Products Data","Profiles"])
                     
                                   
              

                if choice2 == "Customers Details":
                    st.subheader("")
                    task = st.selectbox("task",["","Dashboard","Customers Data"])
                    
                    if task== "Dashboard":
                         html_temp = "<div class='tableauPlaceholder' id='viz1634813606869' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fi&#47;FinalProject_16346326381700&#47;SalesDetails&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='FinalProject_16346326381700&#47;SalesDetails' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Fi&#47;FinalProject_16346326381700&#47;SalesDetails&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1634813606869');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='1427px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
                         components.html(html_temp, width=1000, height=850)
                         max_width_str = f"max-width: 1030px;"
                         st.markdown(f"""<style>.reportview-container .main .block-container{{{max_width_str}}}</style>""",unsafe_allow_html=True)

                       
                     
                        

                    #with st.beta_expander("Title"):
                     #   mytext= st.text_area("Type Here")
                      #  st.write(mytext)
                    
                      
                 
#########################Vvisualization####################################
                          
                        
                     
  
                    elif task == "Customers Data":
                       # df3["District"].value_counts().plot(kind="bar")
                       # st.pyplot()
                       # df3['District']('Haifa').value_counts()
                        #st.markdown(" TEST")
                        # Layout Templates
                    
                 
                        head_message_temp ="""
                        <div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
                        <h4 style="color:white;text-align:center;"> Custumer ID: {} </h1>
                        <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;"></h4>
                        <h6 style="color:white;text-align:center;"> Gender: {} </h6> 
                        <h6 style="color:white;text-align:center;"> District: {} </h6> 
                        <h6 style="color:white;text-align:center;"> Cluster: {} </h6>
                        
                        </div>
                        
                        """
                     
                        
                      #  st.write(t)
                       # dff= pd.DataFrame(result,columns=["user_id","Gender","Age","District"])
                        #st.dataframe(dff)
		
                       # for i in result:
                        #    b_user = i[0]
                         #   b_gender = i[1]
                          #  b_age = str(i[2])[0:30]
                           # b_dist = i[3]
                            #
                            
                        st.subheader("Search Customer")
                        cus_df=view_all_customers()
                        df=pd.DataFrame(cus_df,columns=['user_id','Gender','Age','District'])
                        with st.expander("View All Users"):
                            st.dataframe(df)
                        search_term = st.number_input('Enter Customer ID/cluster',step=1)

                        n=st.number_input('Enter products number',step=1)
                        search_choice = st.radio("Field to Search By",("Customer ID","cluster"))
              
                        if st.button("Search"):
                            if search_choice == "Customer ID":
                               
                                article_result = get_customer(search_term)
                                clus=get_cluster(search_term)
                                t=get_recommendations(search_term, n)
                                t=pd.DataFrame(t)
                           
                                
                                for i in article_result:
                                    b_user = i[0]
                                    b_gender = i[1]
                                    b_age = i[2]
                                    b_city = i[3]
                                
                                
                             
                                    st.markdown(head_message_temp.format(b_user,b_gender,b_city,clus),unsafe_allow_html=True)
                           
                                    st.dataframe(t)
                            elif search_choice=="cluster":
                                article_result = get_cluster_recommendations(search_term,n)
                                t=pd.DataFrame(article_result)
                                st.dataframe(t)
                                
                            
                      
                                
                                
                               
                           # elif search_choice == "author":
                            #    article_result = get_blog_by_author(search_term)
                         
                                #st.markdown(title_temp.format(b_user,b_dist,b_gender,b_age),unsafe_allow_html=True)
                         

                                    
                                    
                            

                                
                                

    
                
                            
                        
                                
                              #  st.text("Reading Time:{}".format(readingTime(b_author)))
                
                                		
                                    		                  
                        
                
                elif choice2 == "Products":
                    
                    st.subheader("Products Page")
                    
                    task = st.selectbox("task",[" ", "Add Product","Edit Product","Delete Product"])
                   # create_table()
                    
                    if task == "Add Product":
                    
                    
                    
                    #col1,col2 = st.beta_columns(2)
                    #with col1:
                        
                        product_id = st.text_input("product ID")
                        product_name = st.text_input("Product name")
                    #with col2:
                            
                        aisle_id=st.text_input("aisle ID")
                        department_id=st.text_input("department id")
	
                     
                    
                    #cosine_sim= vectorize_text(df['aisle'])  
                    #search_term= st.text_input("search")
                    #num_of_rec= st.sidebar.number_input("Number",4,20,7)
                        

                        if st.button("Add Product"):
                            add_data(product_id,product_name,aisle_id,department_id)
                            st.success("Product ID: {} Added  To Products".format(product_id))
                            with st.expander("Read"):
                                allproducts= view_all_products()
                              #  st.write(allproducts)
                                dff= pd.DataFrame(allproducts,columns=["product_id","product_name","aisle_id","department_id"])
                                st.dataframe(dff)
                   # st.subheader("Analytics")
                    elif task == "Edit Product":  
                            
                            #  dff.to_csv('/Users/ronimalihi/Desktop/project/t/products2.csv')
                        with st.expander("Current Products"):
                            
                            result = view_all_products()
    			# st.write(result)
                            clean_df= pd.DataFrame(result,columns=["product_id","product_name","aisle_id","department_id"])
                            st.dataframe(clean_df)
                            st.download_button("Download CSV", data= clean_df.to_csv(), mime ='text/csv')

                        st.subheader("Edit Items") 
                        list_of_products = [i[0] for i in view_all_products_names()]
                        selected_products = st.selectbox("Products ID you want to edit",list_of_products)
                        product_result = get_product(selected_products)
                         
                        if product_result:
                                
                            product_id = product_result[0][0]
                            product_name = product_result[0][1]
                            aisle_id = product_result[0][2]  
                            department_id=product_result[0][3]
                                                           
                    
                            col1,col2 = st.columns(2) 
                            
                                
                        with col1:
                            new_productid = st.text_input("Product ID : {} " .format(product_id))
                            new_productname = st.text_input("Product Name : {} " .format(product_name))
                                			
                        with col2:
                            
                            new_aisleid = st.text_input("aisle ID : {} " .format(aisle_id))      
                            new_depid = st.text_input("Deparment ID :  {} ".format(department_id))        
                            #with col2:
                                            
                    
                        if st.button("Update Product"):
                            edit_product_data(new_productid,new_productname,new_aisleid,new_depid,product_id,product_name,aisle_id,department_id)
                            st.success("Updated Product ID: ' {} '  To: \n\n\n\n\n Product ID: '{}' , Product Name: '{}' , Aisle ID: '{}' , Department ID: '{}'.".format(product_id,new_productid, new_productname,new_aisleid,new_depid))
                    
                        with st.expander("View Updated Data"):
                            result = view_all_products()
                    				# st.write(result)
                            clean_df = pd.DataFrame(result,columns=["product_id","product_name","aisle_id","department_id"])
                            st.dataframe(clean_df)
    
                    elif task == "Delete Product":
  
                        with st.expander("View Data"):
                                result = view_all_products()
                    			# st.write(result)
                                clean_df = pd.DataFrame(result,columns=["product_id","product_name","aisle_id","department_id"])
                                st.dataframe(clean_df)
                    
                        unique_list = [i[0] for i in view_all_products_names()]
                        delete_by_product_name =  st.selectbox("Select product",unique_list)
                        if st.button("Delete"):
                                delete_data(delete_by_product_name)
                                st.warning("Deleted: '{}'".format(delete_by_product_name))
                    
                        with st.expander("Updated Data"):
                                result = view_all_products()
                    			# st.write(result)
                                clean_df = pd.DataFrame(result,columns=["product_id","product_name","aisle_id","department_id"])
                                st.dataframe(clean_df)
                    
                      
              
                          
        
            # st.write(task_result)
                                      
                        #    resu=get_recommendation(search_term,cosine_sim, df, num_of_rec)
                         #   st.write(resu) 
                           
                    # data= pd.read_csv('all_orders.csv', index_col = 0)
                   # t=pd.DataFrame(data)
                    #st.dataframe(t)
                
                    
                    
     
                  
            else:
                    st.warning("Incorrect Username/Password")
        else:  
            st.subheader("Please LOGIN through the side menu to browse the site")



    

        

            
if __name__ =='__main__':
    main()









































    
