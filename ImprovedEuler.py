'''
File Name: ImprovedEuler.py
Author: Natasha, Sach, Pheonix, Jiashu
Date: 03/07/2024
Description: Euler's method function in python
'''
from sympy import symbols

def Eulers(diffEq, x0, y0, StepSize, xf):
   #This function requires 5 inputs: The differential Equation, initial conditions for x and y, the step size, and the final x value
  x = Symbol('x')
  y = Symbol('y')
  iterations = int((xf - x0) / StepSize)
   #This calculate the total number of steps
  for i in range(iterations) :
    slope_x0 = diffEq.subs({x : x0, y : y0}).evalf()
      #This put the x and y values into the function to evaluate the slope of the function at x0
    y1temp = slope_x0 * StepSize + y0
      #this calculate the value for y1 under regular Euler's method
    slope_x1 = diffEq.subs({x : (x0 + StepSize), y : y1temp}).evalf()
      #This put the x and y values into the function to evaluate the slope of the function at x1
    slope = (slope_x0 + slope_x1)/2
      #According to improved Euler's method, the slope is the average of the two slopes
    yfinal = slope * StepSize + y0
      #This substitue all the known value into the Euler's formula to calculate the y value after the step
    x0 = x0 + StepSize
    #This update the x value
    y0 = yfinal
    #This update the y value
  return y0

x = Symbol('x')
y = Symbol('y')
diffEq = 2*x*y
   #This is the differential Equation
x0 = 1
   #This is the inital value for x
y0 = 1
   #This is the initial value for y
StepSize = 0.1
   #This is the step size
xf = 1.5
   #This is the final value of x in which the user want this function to be evaluate to
result = Eulers(diffEq, x0, y0, StepSize, xf)
print(result)
