# How many seconds are in 42 minutes 42seconds
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

pie = 3.142
r = 5 
volume = 4/3 * pie * r**3

print (volume)


