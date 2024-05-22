'''
File Name: RK4ErrorCalculation.py
Author: Natasha, Sach, Pheonix, Jiashu
Date: 03/07/2024
Description: RK4 method in python

The script defines the RK4 function, which takes the following inputs:

- diffEq: The differential equation in symbolic form.
- x0: The initial value of the independent variable (x).
- y0: The initial value of the dependent variable (y).
- StepSize: The step size for numerical integration.
- xf: The final value of the independent variable (x) at which the solution is desired.

The RK4 function performs the following steps:

1. It calculates the total number of steps required to reach xf from x0 based on the given StepSize.
2. It prints a header for the table displaying x_n, y_n, ActVal (actual value), and AbsErr (absolute error).
3. It iterates over the number of steps:
  a. It calculates the four slopes (k1, k2, k3, k4) using the RK4 method.
  b. It calculates the value of y at the next point (yfinal) using the RK4 formula: yfinal = y0 + (StepSize/6) * (k1 + 2*k2 + 2*k3 + k4).
  c. It updates the values of x0 and y0 for the next iteration.
  d. It calculates the actual value of y using the analytical solution: yactual = math.e**((x0**2) - 1).
  e. It calculates the absolute error between the approximated value (y0) and the actual value (yactual).
  f. It prints a row in the table displaying x_n, y_n, ActVal, and AbsErr.
4. After the iterations, the function returns the final value of y.

The script also includes an example usage, where it solves the differential equation 2*x*y with the initial conditions x0 = 1, y0 = 1, and step sizes of 0.025, 0.05, and 0.1.

After running the script with different step sizes, it comments on the observation that reducing the step size by a factor of 2 approximately reduces the error by a factor of 16, demonstrating the expected order 4 convergence of the RK4 method.

Note: The script assumes that the analytical solution to the differential equation is yactual = math.e**((x**2) - 1). This solution is used to calculate the actual value and the error.
'''
import math
from sympy import symbols

def RK4(diffEq, x0, y0, StepSize, xf):
   #This function requires 5 inputs: The differential Equation, initial conditions for x and y, the step size, and the final x value
  x = symbols('x')
  y = symbols('y')
  iterations = int((xf - x0) / StepSize)
  #This calculate the total number of steps
  print('{0} {1} {2} {3}'.format(" x_n ", "    y_n  ", "   ActVal ", "   AbsErr"))
  for i in range(iterations) :
    k1 = diffEq.subs({x:x0, y:y0})
    #This calculate the first slope in the RK4 method
    k2 = diffEq.subs({x : x0 + (StepSize/2), y : y0 + StepSize * (k1/2)})
    #This calculate the second slope in the RK4 method
    k3 = diffEq.subs({x : x0 + (StepSize/2), y : y0 + StepSize * (k2/2)})
    #This calculate the third slope in the RK4 method
    k4 = diffEq.subs({x : x0 + StepSize, y : y0 + StepSize * k3})
    #This calculate the fourth slope in the RK4 method
    yfinal = y0 + (StepSize/6)*(k1 + 2*k2 + 2*k3 + k4)
    #This calculate the y value
    x0 = x0 + StepSize
    #This update the x value
    y0 = yfinal
    #This update the y value
    yactual = math.e**((x0**2) - 1)
      #This calculate the actual y value
    error = abs(yactual-y0)
      #This calculate the error of the Euler's Method
    print('{0} {1} {2} {3}'.format(format(round(x0,4),'.3f'), format(round(y0,8),'.8f'), format(round(yactual,8),'.8f'), format(round(error,8),'.8f')))
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
StepSize = 0.025
   #This is the step size
xf = 1.5
   #This is the final value of x in which the user want this function to be evaluate to
print("StepSize ", 0.025)
result = RK4(diffEq, x0, y0, StepSize, xf)
print("StepSize ", 0.05)
result = RK4(diffEq, x0, y0, StepSize*2, xf)
print("StepSize ", 0.10)
result = RK4(diffEq, x0, y0, StepSize*4, xf)

'''
The error decreased by a factor of 16 when the step size is decresed by a factor of 2
For x = 1.5, the error with step size 0.050 is 0.00000914 and the error with step size 0.100 is 0.00013232 which is factor of 1/14.4
             the error with step size 0.025 is 0.00000060 and the error with step size 0.500 is 0.00000914 which is factor of 1/15.2
if the step size gets smaller, the error factor will converge to 1/16 when the step size is decresed by a factor of 2
'''
