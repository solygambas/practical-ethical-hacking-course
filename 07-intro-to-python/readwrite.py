# months = open('months.txt')

# print(months.read())
# print(months.mode) # r
# print(months.readable()) # True
# print(months.readline()) # January
# print(months.readline()) # February
# print(months.readlines()) # ['January\n', 'February\n', 'March\n', 'April\n', 'May\n', 'June\n', 'July\n', 'August\n', 'September\n', 'October\n', 'November\n', 'December\n']
# months.seek(0)
# print(months.readlines()) 

# for month in months:
#     print(month, end='')

# months.close()

# days = open('days.txt', 'w')

# print(days.writable()) # True
# print(days.mode) # w

# days.write('Monday\n')

days = open('days.txt', 'a')

days.write('Tuesday\n')

days.close()