basket = [
("Peaches", 3.0, 2.99),
("Pears", 5.0, 1.66),
("Plums", 2.5, 3.99)
]

subtotal = 0.00
for item in basket:
    fruit, weight, unitprice = item
    subtotal+= weight*unitprice

tax = subtotal*0.06625

total = subtotal + tax

print("Your subtotal amount came out to be {:.2f}".format(subtotal))
print("Your tax amount came out to be {:.2f}".format(tax))
print("Your total amount came out to be {:10,.2f}".format(total))
# :10,.2f this will leave 10 white spaces

'''
{:d}

integer value   "{0:.0f}".format(10.5) → '10'   

{:.2f}   floating point with that many decimals   '{:.2f}'.format(0.5) → '0.50'   

{:.2s}  string with that many characters     '{:.2s}'.format('Python') → 'Py'   

{:<6s} string aligned to the left that many spaces   '{:<6s}'.format('Py') → 'Py    '  

{:>6s} string aligned to the right that many spaces    '{:>6s}'.format('Py') → '    Py'   

{:^6s} string centered in that many spaces   '{:^6s}'.format('Py') → '  Py  '

'''
