

# got to file->settings -> editor -> font -> select -> (consolas or courier New or DejaVu Sans Mono) fonts to print the words correctly without wrong
# print(dir())                             # 5:20:23 (BroCode)

#print(__name__)

# asterisk (*) means everything    


#from script2 import*     # this means print everything  from script 2


#print(__name__)            #print("Inside script1:",__name__)

# output ->   script2
#             __main__

# the above output is correct , but it cannot show while running .because of total full length  program it is manipulating
# you can run singularly






def favorite_food(food):
    print(f"your favorite food is {food}")
  # our main function will contain the majority of our python code.
                # anything that's not already within a function.
def main():
    print("this is script1")
    favorite_food("pizza")
    print("Goodbye")


if __name__ == "__main__":     # by this method we can check to see which file is being directly.
                                  # if __name__ == "__main__" we will call a function of main to contain the main body of our program.
                                  # but we need to define the function
     main()