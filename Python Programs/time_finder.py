# import math

# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
# # find a total of all minutes
# fin = mins + dura
# # find a number of hours hidden in minutes and update the hour
# fine = fin / 60

# # correct minutes to fall in the (0..59) range
# mins = fin % 60
# # correct hours to fall in the (0..23) range
# hour = fine + hour

# print(round(hour, 4), ":", mins, sep='')

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Calculate the total time in minutes
fin = mins + dura

# Find the hidden hours within the minutes
hidden_hours = fin // 60

# Update the hour
hour += hidden_hours

# Correct minutes to fall in the (0..59) range
mins = fin % 60

print(f"{hour}:{mins:02}")  # Format the output with leading zeros for minutes
