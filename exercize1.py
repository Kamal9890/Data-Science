india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("Enter City name : ")

if city in india :
    print(f" {city } in india ")
    
elif city in pakistan :
    print(f" {city } in pakistan ")
    
    
elif city in bangladesh :
    print(f" {city } in bangladesh ")
    

else:
     print(f"this is city not belong {city}")
    