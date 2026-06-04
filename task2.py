from task1 import *
inventory= []
laptop1 = {"Laptop ID": 101,"Brand": "Dell",  "RAM": "8GB", "Storage": "512GB","Status": "Available"}
laptop2 = {"Laptop ID": 102,"Brand": "HP",    "RAM": "16GB","Storage": "512B", "Status": "Allocated"}
laptop3 = {"Laptop ID": 103,"Brand": "HP",    "RAM": "8GB", "Storage": "256GB","Status":"Available"}
laptop4 = {"Laptop ID": 104,"Brand": "Dell",  "RAM": "32GB","Storage": "256GB","Status": "Damaged"}
inventory.append(laptop1)
inventory.append(laptop2)
inventory.append(laptop3)
inventory.append(laptop4)
# UPDATE LAPTOP CONFIGURATION
for laptop in inventory:
    if laptop["Laptop ID"] == 101:
        laptop["RAM"] =     "16GB"
        laptop["Storage"] = "512GB"
# MODIFY LAPTOP ALLOCATION STATUS
for laptop in inventory:
    if laptop["Laptop ID"] == 103:
        laptop["Status"] = "Allocated"
print("\nUPDATED LAPTOP RECORDS")
print("--------------------------------------------------------------------------------")
print("Laptop ID\tBrand\t\tRAM\t\tStorage\t\tStatus")
print("--------------------------------------------------------------------------------")
for laptop in inventory:
    print(laptop["Laptop ID"], "\t\t",laptop["Brand"], "\t\t",laptop["RAM"], "\t\t",laptop["Storage"], "\t\t",laptop["Status"])
print("--------------------------------------------------------------------------------")
print("\nBRAND-WISE LAPTOPS REPORT")
print("--------------------------------------------------------------------------------")
print("Laptop ID\tBrand\t\tRAM\t\tStorage\t\tStatus")
print("--------------------------------------------------------------------------------")
for laptop in inventory:
    if laptop["Brand"] == "Dell":
        print(laptop["Laptop ID"], "\t\t",laptop["Brand"], "\t\t",laptop["RAM"], "\t\t",laptop["Storage"], "\t\t",laptop["Status"])
print("--------------------------------------------------------------------------------")