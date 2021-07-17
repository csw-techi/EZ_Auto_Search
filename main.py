
type = []
#car, truck, suv
number_doors = []
#2 door, 4 door
drive = []
#awd, 2wd
color = []
#red, white, blue, grey, black, white

ez_search = True

while ez_search:
    start_search =  input("\nWelcome to EZ Auto Search!\nI can help you find your new car! Are you ready to get started?\nType yes to begin and q anytime to quit. ")

    if start_search == 'q':
        break 

    if str.lower(start_search) == "yes":
        vehicle_type = input("Great! lets get started. What type of vehicle are you looking for?\nCar, truck, or SUV? ")
    type.append(vehicle_type)
    print (type)
    
    if start_search == 'q':
        break 
    
    if str.lower(start_search) == "yes":
        num_doors = input("How many doors, 2 or 4?\nPlease enter 2 or 4. ")
    number_doors.append(num_doors)    
    print(number_doors)
    
    if num_doors == 'q':
        break 

    if str.lower(start_search) == "yes":
        drive_type = input("Would you like all wheel drive or 2 wheel drive?\nPlease enter AWD or 2WD. ")
    drive.append(drive_type)
    print(drive)    

    if drive_type == 'q':
        break

    if str.lower(start_search) == "yes":
        vehicle_color = input("What color vehicle do you prefer?\nPlease enter red, white, blue, grey, black, or white. ")
    color.append(vehicle_color)
    print(color)

         
print("Thank you for using EZ Auto Search!")
    
    # try:
    # vehicle_type = input("What type of vehicle would you like? Car, truck, or SUV?")
    
    # type.append(vehicle_type)    
