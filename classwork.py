# How many seconds are in 42 minutes 42seconds
from re import T


mins = 42
secs = 42 

# 60 seconds in 1 minute

t_mins = mins * 60 
t_secs = t_mins + secs

print(t_secs)

# how many miles are in 10kms, 1.61kms = a mile
miles = 1.61
km = 10

t_miles = km / miles
print (t_miles)

# if you run a 10km race in 42mins 42secs, what is your average pace (time per mile in minutes and seconds)? what is your average speed in miles per hour

distance = 10

# time 
tim_mins = 42
tim_secs = 42

# Minutes
minutes = tim_mins + (tim_secs/60)
print (minutes)

# Seconds
seconds = (tim_secs*60) + 42
print (seconds)

# Hour
hour = minutes/60
print(hour)

# Miles per Minutes
miles_mins = t_miles / minutes
print (miles_mins)

# Miles per Seconds
miles_secs = t_miles / seconds
print (miles_secs)

# Miles per Hour
miles_hour = t_miles / hour
print (miles_hour)

# The volume of a sphere with radius r =4/3 pi r^3 what is the volume of a sphere with radius 5 
pie = 3.142
r = 5 
volume = 4/3 * pie * r**3

print (volume)

# If i leave my house at 6:52am and run 1 mile at an easy pace (8:15 per mile) then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again what time do  get home for breakfast
start_time = (6*60 + 52) *60
easy_pace = (8*60 + 15) *2
tempo_pace = (7*60 + 12) *3

run_time = easy_pace + tempo_pace

home_time = start_time+run_time

break_fast_hour = home_time//3600
break_fast_min = (home_time%3600) // 60
break_fast_sec = (home_time%3600) % 60

print (f"{break_fast_hour}:{break_fast_min}:{break_fast_sec}am")


t = 'tomisin'
print (t)