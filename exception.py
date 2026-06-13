# Exception

# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError, TypeError , ValueError)
#             1.try, 2.except, 3.finally

try:

    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide bt zero")

except ValueError:
    print("Enter only numbers please")

except Exception:
    print("Something went wrong")
finally:
        print("Do some cleanup here")


# there are many different types of exceoptions .
# you can always look under the offcial python ducumentation for an expensive list

'''
-except  Exception → this is a general catch-all. It will handle any other error that isn’t specifically listed above.
👉 Think of it like safety nets stacked one after another:


- zeroError ->First net catches division by zero.

- ValueEror  ->Second net catches invalid input.

- Third net catches anything else unexpected.
'''