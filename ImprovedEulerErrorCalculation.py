'''
File Name: ImprovedEulerErrorCalculation.py
Author: Natasha, Sach, Pheonix, Jiashu
Date: 03/07/2024
Description: Euler's method function in python
'''
import math
from sympy import symbols

def Eulers(diffEq, x0, y0, StepSize, xf):
   #This function requires 5 inputs: The differential Equation, initial conditions for x and y, the step size, and the final x value
  x = symbols('x')
  y = symbols('y')
  iterations = int((xf - x0) / StepSize)
   #This calculate the total number of steps
  print('{0} {1} {2} {3}'.format(" x_n ", "y_n  ", "ActVal", "AbsErr"))
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
    yactual = math.e**((x0**2) - 1)
      #This calculate the actual y value
    error = abs(yactual-y0)
      #This calculate the error of the Euler's Method
    print('{0} {1} {2} {3}'.format(format(round(x0,4),'.2f'), round(y0,4), round(yactual,4), round(error,4)))
      #This print a table of informations we know
  return y0

x = symbols('x')
y = symbols('y')
diffEq = 2*x*y
   #This is the differential Equation
x0 = 1
   #This is the inital value for x
y0 = 1
   #This is the initial value for y
StepSize = 0.05
   #This is the step size
xf = 1.5
   #This is the final value of x in which the user want this function to be evaluate to
print("StepSize ", 0.05)
result = Eulers(diffEq, x0, y0, StepSize, xf)
print("StepSize ", 0.10)
result = Eulers(diffEq, x0, y0, StepSize*2, xf)
#By looking at the Error Value, we can see a 4 time reduction when the StepSize is reduced by 2 time, proving that Improved Euler Error is proportional to StepSize squared