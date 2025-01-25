##### ASSIGNMENT STARTS HERE #####


#%%
# First Assignment
'''
1: Please create a program which inputs two years and outputs the years as well as the difference
between them!

Your output should look like:

Year 1: 2025
Year 2: 2028
Difference: 3
'''
year1=int(input('Year 1: '))#input for fist year
year2=int(input('Year 2: '))#input for second year
difference=(year2 - year1) #equation to get difference of years
#formating output with f-string
txt = f"""Year 1: {year1} 
Year 2: {year2}
Difference: {difference}"""
print(txt) #print output

#%%
# Second Assignment

'''
2: Please create a program which collects an input as fahrenheit and outputs the 
temperature in celsius

Your output should look like:

Fahrenheit: 25
Celsius: -3.89
'''
import math #importing math module for mathematical functions
fahrenheit=float(input('Fahrenheit: '))#input for fahrenheit
celsius=((fahrenheit - 32)*(5/9)) #equation to convert fahrenheit to celsius
#formating output with f-string
txt = f"""Fahrenheit: {math.floor(fahrenheit)} 
Celsius: {celsius:.2f}""" # using math.floor to round number downwards its nearest integer and rounding the celsius output to 2 decimal places
print(txt) #print output

#%%
# Third Assignment

'''

3: Please create a program which collects an input as US Dollars and converts the output to Euros 
given the exchange rate on 1/19/25 as 1 USD = 0.97 Euro

Your output should look like:
USD: 1
EU: 0.97

'''
usd=float(input('US Dollars: '))#input for US Dollars
eu=(usd * 0.97) #equation to convert usd to eu
#formating output with f-string
txt = f"""USD: {math.floor(usd)}
EU: {eu:.2f}""" # using math.floor to round number downwards its nearest integer and rounding the Euro output to 2 decimal places
print(txt) #print output

##### ASSIGNMENT ENDS HERE #####
