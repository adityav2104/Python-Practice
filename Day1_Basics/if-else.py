#IF-ELIF-ELSE
price = 50
if price < 50:
    print("The price is less than 50")
elif price == 50:
    print("The price is exactly 50")
else:
    print("The price is greater than 50")

#SHORT HAND IF ELSE
res = "Yes" if price < 50 else "No"
print(f"Result: {res}")

#NESTED IF
if price < 50:
    print("The price is less than 50")
    if price < 20:
        print("The price is also less than 20")
    else:
        print("The price is between 20 and 50")

'''
#MATCH CASE 
number = 3
match number:
    case 1:
        print("Number is 1")
    case 2:
        print("Number is 2")
    case 3:
        print("Number is 3")
    case _:
        print("Number is something else")
'''