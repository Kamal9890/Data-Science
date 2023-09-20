india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1 = input("Enter City name1 : ")
city2 = input("Enter city name2 : ")

if city1  in india and city2 in india  :
    print("both city  in india ")
    
elif city1 in pakistan and city2 in pakistan :
    print(" both city in pakistan ")
    
    
elif city1 in bangladesh and city2 in bangladesh :
    print("both city in bangladesh ")
    

else:
     print("this city is not belong to same country")