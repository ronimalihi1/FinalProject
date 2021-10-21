#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 11:34:47 2021

@author: ronimalihi
"""
import sqlite3
import pandas as pd

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
    
    
    ### customers tables ###
    
