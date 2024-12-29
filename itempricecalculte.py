basket = [("Mango", 3.0,2.98),
          ("Peahces", 5.0,3.98),
          ("", 2.0,1.98)]

subtotal = 0.00
for item in basket:
    fruit, weight, unitprice = item
    subtotal+= weight*unitprice

tax = subtotal*0.06625

total = subtotal + tax

print("Your tax amount came out to be {}".format(tax))

print("Your tax amount came out to be {}".format(tax))