# 2d lists

# creatong NUM PAD OR FOR EXAMPLE WE USE DIALER TO DIAL A PHONE IN OUR MOBILE

#Note -> A Tuple is faster than the list .
# A Tuple is ordered and unchangeable

# insetad of printing this you can create matrix
fruits = ["appla", "orange", "banana" , "coconut"]
vegetables = ["celery" , "carrots" , "potatoes"]
snacks = ["chips" , " kurkure" , "mixture"]

groceries  = [fruits , vegetables , snacks]

print(groceries[1][2])


# this is matrix
groceries = [["apple", "orange", "banana" , "coconut"],
             ["celery" , "carrots" , "potatoes"],
             ["chips" , " kurkure" , "mixture"]]

print(groceries[1][1])




# you can access with for loop

groceries = [["apple", "orange", "banana" , "coconut"],
             ["celery" , "carrots" , "potatoes"],
             ["chips" , "kurkure" , "mixture"]]

for collection in groceries:

    print(collection) #-> to print all items

for collection in groceries:

    for food in collection:

        print(food , end =" ")
    print()



# creating NUMPAD OR DIALER

Num_Pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for dailer in  Num_Pad:

    for number in dailer:

        

      print(number, end=" ")

    print()
