import datetime

# # Create a datetime object for January 1, 2022 at 9:00 AM
# dt = datetime.datetime(2023, 1, 1, 9, 0, 0)
#
# # Print the datetime object
# print(dt)

# # Create a date object for January 1, 2022
# d = datetime.date(2023, 1, 1)
#
# # Print the date object
# print(d)


# # Create a time object for 9:00 AM
# t = datetime.time(9, 0, 0)
#
# # Print the time object
# print(t)


# td = datetime.timedelta(days=1)
#
# print(td)

# formatted = dt.strftime('%m/%d/%Y %H-%M-%S')
# print(formatted)


dt1 = datetime.datetime(2023, 1, 1, 9, 0, 0)


td1 = datetime.timedelta(hours=1, days=5)

# Add the timedelta to the datetime
dt2 = dt1 + td1

# Print the new datetime object
print(dt2)