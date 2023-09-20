indian = ['samosa', 'kachori', 'naan']
pakistani = ['nihari','paya','karachi']
bangladesh = ['panta bhat' , 'chorchori','fuchka']

dish = input("Enter dish name : ")


if dish in pakistani:
    print(f"{dish} is pakistani")
    
elif dish in bangladesh:
    print(f"{dish} is bangladesh")
    
elif dish in indian:
    print(f"{dish} is indian")
    

else :
    print(f"Based on limited knowledge i don't know which cuisine {dish}")
    