import re                             #to restrict some patterns
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:38:42 2020

@author: aishwarya
"""
print("Hey,Here is Your Calculator")
print("Type q to Quit\n")

previousval = 0
run = True

def Perform_Calc():
    global run
    global previousval
    equation = ""
    if previousval == 0:
        equation = input("Enter the numbers to perform calculation:")
    else:
        equation = input(str(previousval))


    if equation == 'q': 
        print("Goodbye, Man.")
        run = False
    else:
        equation = re.sub('[A-Za-z:;,.()" "]',' ',equation)
        
    if previousval == 0:
        previousval = eval(equation)
    else:
        previousval = eval(str(previousval) + equation)
        
        
while run:
    Perform_Calc()
     

