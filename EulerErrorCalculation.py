'''
File Name: EulerErrorCalculation.py
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
2. It prints a header for the table displaying x_n, y_n, ActVal (actual value), and AbsErr (absolute error).
3. It iterates over the number of steps:
  a. It evaluates the slope of the differential equation at the current point (x0, y0) using SymPy's subs and evalf functions.
  b. It calculates the value of y using the Euler's method formula: yfinal = slope * StepSize + y0.
  c. It updates the values of x0 and y0 for the next iteration.
  d. It calculates the actual value of y using the analytical solution: yactual = math.e**((x0**2) - 1).
  e. It calculates the absolute error between the approximated value (y0) and the actual value (yactual).
  f. It prints a row in the table displaying x_n, y_n, ActVal, and AbsErr.
4. After the iterations, the function returns the final value of y.

The script also includes an example usage, where it solves the differential equation 2*x*y with the initial conditions x0 = 1, y0 = 1, and step sizes of 0.05 and 0.1.

After running the script with both step sizes, it comments on the observation that reducing the step size by a factor of 2 approximately reduces the error by a factor of 2. This demonstrates the linear relationship between the step size and the error in Euler's method.

Note: The script assumes that the analytical solution to the differential equation is yactual = math.e**((x**2) - 1). This solution is used to calculate the actual value and the error.
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
    slope = diffEq.subs({x : x0, y : y0}).evalf()
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
#By looking at the Error Value, we can see an approximately 2 time reduction when the StepSize is reduced by 2 time, proving that Improved Euler Error is linearly proportional to StepSize
