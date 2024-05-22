'''
File Name: ImprovedEuler.py
Author: Natasha, Sach, Pheonix, Jiashu
Date: 03/07/2024
Description: Euler's method function in python

The script defines the Eulers function, which takes the following inputs:

- diffEq: The differential equation in symbolic form.
- x0: The initial value of the independent variable (x).
- y0: The initial value of the dependent variable (y).
- StepSize: The step size for numerical integration.
- xf: The final value of the independent variable (x) at which the solution is desired.

The Eulers function performs the following steps:

1. It calculates the total number of steps required to reach xf from x0 based on the given StepSize.
2. It iterates over the number of steps:
  a. It evaluates the slope of the differential equation at the current point (x0, y0) using SymPy's subs and evalf functions.
  b. It calculates the temporary value of y1 using the regular Euler's method formula: y1temp = slope_x0 * StepSize + y0.
  c. It evaluates the slope of the differential equation at the next point (x0 + StepSize, y1temp) using SymPy's subs and evalf functions.
  d. It calculates the average slope using the improved Euler's method: slope = (slope_x0 + slope_x1) / 2.
  e. It updates the value of y using the improved Euler's method formula: yfinal = slope * StepSize + y0.
  f. It updates the values of x0 and y0 for the next iteration.
3. After the iterations, the function returns the final value of y.

The script also includes an example usage, where it solves the differential equation 2*x*y with the initial conditions x0 = 1, y0 = 1, step size of 0.1, and a final value of x = 1.5.

Note: The script uses the SymPy library for symbolic mathematics, which allows the user to input the differential equation in symbolic form.
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
