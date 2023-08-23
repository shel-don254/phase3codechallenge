def convert_to_24_hour(hour, minute, period):

    if period == "am":
        if hour == 12:
            hour = 0
            print (f"{hour:02d}{minute:02d} hrs")

        else:
            if hour != 12:
                print (f"{hour:02d}{minute:02d} hrs")

    elif period == "pm":
        if hour == 12:
            print (f"{hour:02d}{minute:02d} hrs")
        else:
            if hour != 12:
                print (f"{(hour + 12):02d}{minute:02d} hrs")
                
hr = int(input("Enter hour: "))
min = int(input("Enter min: "))
period_of_day = input("Enter period: ")

convert_to_24_hour(hr, min, period_of_day)
