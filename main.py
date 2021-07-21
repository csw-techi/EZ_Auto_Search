from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import time
import random

headers = ({'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit\
/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'})


vehicle_type = []
#car, truck, suv
number_doors = []
#2D, 4D
drive = []
#awd, 2wd
color = []
#red, white, blue, grey, black, white

ez_search = True

while ez_search:
    start_search =  input("\nWelcome to EZ Auto Search!\nI can help you find your new car! Are you ready to get started?\nType yes to begin or q anytime to quit. ")

    if start_search == 'q':
        break 

    if str.lower(start_search) == "yes":
        veh_type = input("Great! lets get started. What type of vehicle are you looking for?\nCar, truck, or SUV? ")
    vehicle_type.append(veh_type)
    print (vehicle_type)
    
    if start_search == 'q':
        break 
    
    if str.lower(start_search) == "yes":
        num_doors = input("How many doors, 2 or 4?\nPlease enter 2D or 4D. ")
    number_doors.append(num_doors)    
    print(number_doors)
    
    if num_doors == 'q':
        break 

    if str.lower(start_search) == "yes":
        drive_type = input("Would you like four wheel drive, front wheel drive, or rear wheel drive?\nPlease enter 4WD, FWD, or RWD. ")
    drive.append(drive_type)
    print(drive)    

    if drive_type == 'q':
        break

    if str.lower(start_search) == "yes":
        vehicle_color = input("What color vehicle do you prefer?\nPlease enter red, white, blue, grey, black, or white. ")
    color.append(vehicle_color)
    print(color)

         
print("Thank you for using EZ Auto Search!")

def get_basic_info(content_list):
    basic_info = []
    for item in content_list:
        basic_info.append(item.find_all('div', attrs={'class': 'row srpVehicle hasVehicleInfo'}))
    return basic_info

def get_names(basic_info):
    names = []
    for item in basic_info:
        for i in item:
            names.append(i.find_all("li", attrs = {"class" : "bodyStyleDisplay"})[0].text.strip())
    return names

names = []

for i in range(9):
    base_url =  "https://www.neilhuffman.com/searchused.aspx?campaignid=11473286766&adgroupid=113104937998&keyword=%2Bused%20%2Bauto&gclid=CjwKCAjwuIWHBhBDEiwACXQYscZHj-vjUdI_wGzL4Ge5tOUHhH2W17pYYnHoU0JVmgEImnBU0iQ2uRoC9CcQAvD_BwE&pt=1"
    response = get(base_url, headers=headers)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    content_list = html_soup.find_all('div', attrs={'class': 'row row-offcanvas row-offcanvas-left margin-top-2x'})
    
    basic_info = get_basic_info(content_list)
    names1 = get_names(basic_info)
   
    names.extend(names1)
   
# basic_info = []
# for item in content_list:
#     basic_info.append(item.find_all('div', attrs={'class': 'row srpVehicle hasVehicleInfo'}))
# print(basic_info)    
    
data = pd.DataFrame(names)
data.columns = ["name"]
# data.name[2]


data.head()
data.drop_duplicates()
data.to_csv('results_list.csv')

