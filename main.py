from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import time
import random

headers = ({'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit\
/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})


vehicle_type = []
#car, truck, suv, van
vehicle_drive = []
#awd, 2wd, rwd
vehicle_mileage = []
#0-25k, 26k-50k, 51k-75k, 76-100k
vehicle_price = []
#0-15k, 16k-25k, 26k-50k, 51k-75k, 76k-100+k

ez_search = True

while ez_search:
    start_search =  input("\nWelcome to EZ Auto Search!\nI can help you find your new car! Are you ready to get started?\nType yes to begin or q anytime to quit. ")

    if start_search == 'q':
        break 

    if str.lower(start_search) == "yes":
        veh_type = input("Great! lets get started. What type of vehicle are you looking for?\nCar, truck, van or SUV? ")
    vehicle_type.append(veh_type)
    print (vehicle_type)
    
    if start_search == 'q':
        break 

    if str.lower(start_search) == "yes":
        drive_type = input("Would you like four wheel drive, front wheel drive, or rear wheel drive?\nPlease enter 4WD, FWD, or RWD. ")
    vehicle_drive.append(drive_type)
    print(vehicle_drive)
   
    if drive_type == 'q':
        break

    if str.lower(start_search) == "yes":
        veh_mileage = input("What's the max mileage you would prefer? ")
    vehicle_mileage.append(veh_mileage)    
    print(veh_mileage)
    
    if veh_mileage == 'q':
        break 

    if str.lower(start_search) == "yes":
        veh_price = input("What price range would you prefer? ")
    vehicle_price.append(veh_price)
    print(vehicle_price)

    if veh_price == 'q':
        break

else:
    print("Thank you for using EZ Auto Search!")

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
names = []
style = []
drivetrain = []
mileage = []
engine = []
price = []

for i in range(9):
    base_url =  "https://www.neilhuffman.com/searchused.aspx?campaignid=11473286766&adgroupid=113104937998&keyword=%2Bused%20%2Bauto&gclid=CjwKCAjwuIWHBhBDEiwACXQYscZHj-vjUdI_wGzL4Ge5tOUHhH2W17pYYnHoU0JVmgEImnBU0iQ2uRoC9CcQAvD_BwE"
    response = get(base_url, headers=headers)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    content_list = html_soup.find_all('div', attrs = {'class': 'row srpVehicle hasVehicleInfo'})
    
    basic_info = get_basic_info(content_list)
    basic_info2 = get_basic_info2(content_list)
    basic_info3 = get_basic_info3(content_list)
    names1 = get_names(basic_info)
    style1 = get_style(basic_info2)
    drive1 = get_drivetrain(basic_info2)
    mileage1 = get_mileage(basic_info2)
    engine1 = get_engine(basic_info2)
    price1 = get_price(basic_info3)

    names.extend(names1)
    style.extend(style1)
    drivetrain.extend(drive1)
    mileage.extend(mileage1)
    engine.extend(engine1)
    price.extend(price1)

    page_number = page_number + 1
    time.sleep(random.randint(1,2))

a = {"Model" : names, "Body_Style": style, "Drive_Type": drivetrain, "Engine": engine, "Mileage": mileage, "Price": price}
df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()

df1 = df.query('Drive_Type.str.contains("FWD")' and 'Body_Style.str.contains("Sedan")')
# df2 = df.query('Drive_Type == FWD')
# df.query('Price > 50,000')
df1.drop_duplicates(inplace=True)
df1.to_csv('results_list.csv')
print("")
print("Here are the vehicles for sale at Neil Huffman based on your input.\nA csv file with these results called results_list.csv is available locally.")
print("")
print(df1)
print("")
print("Thank you for using EZ Auto Search!")

# issues

# query dataframe with user input

#change user input to a list of options. User enters 1,2,3,4 etc
#1. Sedan
#2. Sport Utility
#3. Truck
#4. Van



