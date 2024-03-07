'''
File Name: Euler.py
Author: Natasha, Sach, Pheonix, Jiashu
Date: 03/07/2024
Description: Euler's method function in python
'''
from sympy import *
diffEq = 2*x + y
#This is the differential Equation
x0 = 0
#This is the inital value for x
y0 = 1
#This is the initial value for y
StepSize = 0.1
#This is the step size
xf = 5
#This is the final value of x in which the user want this function to be evaluate to
result = Euler(diffEq, x0, y0, StepSize, xf)
def Eulers(diffEq, x0, y0, StepSize, xf):
#This function requires 5 inputs: The differential Equation, initial conditions for x and y, the step size, and the final x value
  x = Symbol("x")
  y = Symbol("y")
  iterations = int(xf - x0) / StepSize
  #This calculate the total number of steps
  for i in range(iterations) :
    slope = diffEq.evalf(sub{x,x0}, sub{y,y0})
    #This put the x and y values into the function to evaluate the slope of the function at a certain point
    y = slope * StepSize + y0
    #This substitue all the known value into the Euler's formula to calculate the y value after the step
    x0 = x0 + StepSize
    #This update the x value
    y0 = y
    #This update the y value
