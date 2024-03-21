"""
=========================================================
Name : lab9_exe_C.py
Assignment : Lab 9, Exercise C
Author(s) : Mahdi Ansari , William Arthur Philip Louis
Edited by : Hongwoo Yoon, Steve(Hyunmung) Park
Submission : May 20, 2024
Description : Fetch data by Python.
=========================================================
"""


import requests
import json

def fetch_product_data(url):
    try:
        response = requests.get(url)
        # Raises an error for bad responses
        response.raise_for_status()
        # The JSON structure included a 'products' key
        return response.json()['products']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []
#This function is to list all the products.
#This is possible since the json file is now a list called products.
def list_all_products(products):   
    while True: #Loop always true until break is called
        try:
            for product in products:
                print(f"Name: {product['title']}\n") #Prints the name of the product
            break
        except TypeError:
            print("Invalid product data.")
            return

def search_product(products, name):
    for product in products:
        if product['title'] == name: #If the product name is found in the list of products
            print("Product found.\n")
            print(f"Name: {product['title']}\n")
            return
    print("Product not foun.")

def main():
    products_url = 'https://dummyjson.com/products' #URL to the json file
    products = fetch_product_data(products_url) #Fetches the data from the json file

    if products: #If the data is fetched
        while True: #Loop always true until break is called
            choice = input("Choose an option:\n1. List all products\n2. Search for a product\n3. Exit\n")
            if choice == '1':
                list_all_products(products)
            elif choice == '2':
                product_name = input("Enter the product name: ")
                search_product(products, product_name)
            elif choice == '3':
                break
            else:
                print("Invalid choice. Try again.")
    else: #If the data is not fetched
        print("Failed to fetch product data.")


if __name__ == "__main__":
    main()