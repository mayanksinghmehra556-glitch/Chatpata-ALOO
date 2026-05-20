#Good Morning Sir
a=input("enter the time: ").lower()
b=input("enter timezone: ").lower()
if "00:00" < a < "12:00" and b == "am":
    print("Good Morning Sir")
elif "12:00"<a<"16:00" and b=="pm":
    print("Good Afternoon Sir")
elif "16:00"<a<"18:00" and b=="pm":
    print("Good Evening Sir")
elif a=="00:00" and b=="am":
    print("Its Midnight Sir")
elif a=="12:00" and b=="pm":
 print("Its Noon Sir")
else:
    print("Good Night Sir")
