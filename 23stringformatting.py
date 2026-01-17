#creating an f string
name = str(input("enter your name: "))
text = f"hello, welcome {name}"
print(text)

#using modifiers in format string
price = 99.4966564
text = f"Price of the product is {price:.2f}"
print(text)

#performing operations in f string
text = f"At discount rate of 12% the final price is {price - price%12:2f}"
print(text)

#using ifelse in f strings
text = f"It is {'cheap' if price < 100 else 'expensive'}"
print(text)

#more modifiers
print(f"The price is {price:+}") #add + at start of result
print(f"The price is {-25:-}") #add - at start of result
print(f"The price is {price: }") #add blank at start of result
print(f"dinasours are existed {10000000000:,} years ago") #thousant seprator ","
print(f"dinasours are existed {10000000000:_} years ago") #thousant seprator "_"
print(f"The price is {price:.0%}") #add % at end of result
print(f"The value is {0.0000000004:e}") #convert into scientific format with e
print(f"The value is {0.0000000004:E}") #convert into scientific format with E

#using format method
price = 10
discountprice = 9
discount = 0.1
text = "the real price {}, after discout of {:.0%} price is {}"
print(text.format(price, discount, discountprice))
