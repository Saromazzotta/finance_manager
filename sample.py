import re


myStr = "-47"

print(type(myStr), myStr)

# amount = ":.2f".format(float(myStr))




try:
    amount = float(myStr)
    print("Converted Float:", myStr)
except ValueError:
    print("Invalid string format for conversion to float.")




# float(re.findall(r'\d+\.\d+', myStr))
print(type(amount), amount)


