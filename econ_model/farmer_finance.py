# modex parameter list is below.
climate = 1
inflation = 1.03
interest_rate = 1.01
land_tax = 1.00

import csv
from definitions import Product
    
def csv_to_dict(raw_csv_file):
    product_data = [] 
    products = [] 

    with open(raw_csv_file, "r") as csv_file:
        reader = csv.reader(csv_file)
        
        rownum = 0
        for row in reader:
            if rownum == 0:
                for col in row:
                    product_data.append(col)
                rownum += 1

            else:
               current_product = {}
               colnum = 0
               for col in row:
                   category = product_data[colnum]
                   current_product[category] = col
                   colnum += 1
               print current_product
               products.append(current_product)

                
                    
    return products

def objectify(products):
    object_list = []
    for product in products:
        object_list.append(Product(product))
    
    return object_list
        
processed_csv = csv_to_dict("farm_data.csv") 
probjects = objectify(processed_csv)

def calculate_profits(product_objects):
    for product_object in product_objects:
        print product_object.calculate_profit()

calculate_profits(probjects)
