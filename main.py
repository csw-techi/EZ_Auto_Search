from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import time
import random

headers = ({'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit\
/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})

ez_search = True

# feature - create a master loop
while ez_search:
    start_search =  input("\nWelcome to EZ Auto Search!\nI can help you find your new car! Are you ready to get started?\nEnter yes to begin or q to quit anytime. ")

    if start_search == 'q':
        print("Never quit! Thank you for using EZ Auto Search!")
        exit() 

    if str.lower(start_search) == "yes":
        veh_type = input("Great! lets get started. What type of vehicle are you looking for?\n1. SUV\n2. Car\n3. Van\n4. Truck\nPlease enter the number of your choice. ")
        print("You chose {}!".format(veh_type))
    
    if veh_type == '1':
        veh_type = 'Sport Utility'

    if veh_type == '2':
        veh_type = 'Sedan'    
    
    if veh_type == '3':
        veh_type = 'Van'

    if veh_type == '4':
        veh_type = 'Crew Cab'
     
    if veh_type == 'q':
        print("Never quit! Thank you for using EZ Auto Search!")
        exit() 

    if str.lower(start_search) == "yes":
        drive_type = input("What drive type would you prefer?\n1. Front wheel drive\n2. Rear wheel drive\n3. All wheel drive\nPlease enter the number of your choice. ")
        print("You chose {}!".format(drive_type))
    if drive_type == '1':
        drive_type = 'FWD'

    if drive_type == '2':
        drive_type = 'RWD'

    if drive_type == '3':
        drive_type = 'AWD'

    if drive_type == 'q':
        print("Never quit! Thank you for using EZ Auto Search!")
        exit()

    if str.lower(start_search) == "yes":
        veh_mileage = input("What's the maximum mileage would you prefer?\n1. 15k\n2. 25k\n3. 50k\n4. 75k\n5. 100\nPlease enter the number of your choice. ")
        print("You chose {}!".format(veh_mileage))

    if veh_mileage == '1':
        veh_mileage = '15000'

    if veh_mileage == '2':
        veh_mileage = '25000'   
   
    if veh_mileage == '3':
        veh_mileage = '50000'

    if veh_mileage == '4':
        veh_mileage = '75000'

    if veh_mileage == '5':
        veh_mileage = '100000'
    
    if veh_mileage == 'q':
        print("Never quit! Thank you for using EZ Auto Search!")
        exit() 

    if str.lower(start_search) == "yes":
        veh_price = input("What's the max price you would like to pay?\n1. 15k\n2. 25k\n3. 50k\n4. 75k\n5. 100k\nPlease enter the number of your choice. ")
        print("You chose {}!\n".format(veh_price))

    if veh_price == '1':
        veh_price = '15000'

    if veh_price == '2':
        veh_price = '25000'    
   
    if veh_price == '3':
        veh_price = '50000'

    if veh_price == '4':
        veh_price = '75,000'

    if veh_price == '5':
        veh_price = '100,000'
    
    if veh_price == 'q':
       print("Never quit! Thank you for using EZ Auto Search!")
       exit()

    else: 
        choice = input("Would you like to change your choices?\nPlease enter yes or no. ")
    if choice == 'yes':
        start_search = True
    if choice == 'no':
        break
    if choice == 'q':
       print("Never quit! Thank you for using EZ Auto Search!")
       exit()
print("Please wait as we look for your new car....")

# feature - create 3 or more functions

def find_car_attribute(html,html_tag, html_class, prefix):
    text = html.find_all(html_tag, attrs={"class": html_class})[0].text.strip()
    return strip_prefix(text, prefix)

def strip_prefix(text, prefix):
    return text[len(prefix):]   

def get_basic_info(content_list):
    basic_info = []
    for item in content_list:
        basic_info.append(item.find_all('div', attrs = {'class': 'col-md-12 col-sm-12 hidden-xs'}))
    return basic_info

def get_basic_info2(content_list):
    basic_info2 = []
    for item in content_list:
        basic_info2.append(item.find_all('div', attrs = {'class': 'col-sm-6 col-sm-pull-6 col-xs-12'}))
    return basic_info2

def get_basic_info3(content_list):
    basic_info3 = []
    for item in content_list:
        basic_info3.append(item.find_all('div', attrs = {'class': 'col-sm-6 col-sm-push-6 hidden-xs'}))
    return basic_info3

def get_names(basic_info):
    names = []
    for item in basic_info:
        for i in item:
            names.append(i.find_all("span", attrs = {"class" : "notranslate"})[0].text.strip())
    return names

def get_style(basic_info2):
    style = []
    for item in basic_info2:
        for i in item:
            attr = find_car_attribute(i, "li", "bodyStyleDisplay", "Body Style: ")
            style.append(attr)
    return style

def get_drivetrain(basic_info2):
    drivetrain = []
    for item in basic_info2:
        for i in item:
                attr = find_car_attribute(i, "li", "driveTrainDisplay", "Drive Type: ")
                drivetrain.append(attr) 
    return drivetrain     

def get_mileage(basic_info2):
    mileage = []
    for item in basic_info2:
        for i in item:
            attr = find_car_attribute(i, "li", "mileageDisplay", "Mileage: ")
            mileage.append(attr)
    return mileage
    
def get_engine(basic_info2):
    engine = []
    for item in basic_info2:
        for i in item:
            attr = find_car_attribute(i, "li", "engineDisplay", "Engine: ")
            engine.append(attr)
    return engine

def get_price(basic_info3):
    price = []
    for item in basic_info3:
        for i in item:
            attr = find_car_attribute(i, "span", "pull-right primaryPrice", "$")
            price.append(attr)
    return price

page_number = 1
# feature - create a list 
names = []
style = []
drivetrain = []
mileage = []
engine = []
price = []

for i in range(9):
    # feature - create a scraper
    base_url =  "https://www.neilhuffman.com/searchused.aspx?campaignid=11473286766&adgroupid=113104937998&keyword=%2Bused%20%2Bauto&gclid=CjwKCAjwuIWHBhBDEiwACXQYscZHj-vjUdI_wGzL4Ge5tOUHhH2W17pYYnHoU0JVmgEImnBU0iQ2uRoC9CcQAvD_BwE&pt={}".format(page_number)
    response = get(base_url, headers=headers)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    content_list = html_soup.find_all('div', attrs = {'class': 'row srpVehicle hasVehicleInfo'})
    
    basic_info = get_basic_info(content_list)
    basic_info2 = get_basic_info2(content_list)
    basic_info3 = get_basic_info3(content_list)
    names1 = get_names(basic_info)
    style1 = get_style(basic_info2)
    drivetrain1 = get_drivetrain(basic_info2)
    mileage1 = get_mileage(basic_info2)
    engine1 = get_engine(basic_info2)
    price1 = get_price(basic_info3)

    names.extend(names1)
    style.extend(style1)
    drivetrain.extend(drivetrain1)
    mileage.extend(mileage1)
    engine.extend(engine1)
    price.extend(price1)
    
    page_number = page_number + 1
    time.sleep(random.randint(1,2))

a = {"Model" : names, "Body_Style": style, "Drive_Type": drivetrain, "Engine": engine, "Mileage": mileage, "Price": price}
df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()

df.query("Drive_Type == @drive_type",inplace=True)
# Query needs work, I could not get it to work properly with all user input. TypeError: unsupported operand type(s) for &: 'str' and 'str'
df.drop_duplicates(inplace=True)
df.to_csv('ez_auto_search.csv')
print("")
print("Here are the vehicles for sale at Neil Huffman based on your input.\nA csv file with these results called ez_auto_search.csv is available locally.")
print("")
print(df)
print("")
print("Thank you for using EZ Auto Search!")