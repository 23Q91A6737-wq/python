# Count-Down timer 🌟🌠⭐

import time

my_time = int(input("Enter your time in seconds : "))

for x in range(my_time,0,-1):

    print(x)



# After each iteration, we will sleep for 1 second in below step
    time.sleep(7)

print("Times Up!")


# The total count-down project


import time

my_time = int(input("Enter your time : "))

for x in range(my_time,0,-1):

    seconds = x % 60   #  %  -> remainder of a division

    minutes =int (x / 60) % 60

    hours = int(x / 3600)

    print(f"{hours}:{minutes}:{seconds}")        # you can often use print(f"00:00:{seconds:02} format specifier -> for to display two digits.then zero pad those digits
    time.sleep(1)
print("Times Up!")
