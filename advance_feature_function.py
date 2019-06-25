def minutes_of_hours(minutes,seconds):
    hours = minutes / 60 + seconds /3600
    return hours
print(minutes_of_hours(200,6600)+10)

# In another way:

def minutes_of_the_hours(min,sec = 9000):
    hour = min / 60 + sec / 3600
    print(hour)
minutes_of_the_hours(2000)