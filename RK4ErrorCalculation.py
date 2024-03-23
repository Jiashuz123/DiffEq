'''
File Name: RK4ErrorCalculation.py
Author: Natasha, Sach, Pheonix, Jiashu
Date: 03/07/2024
Description: RK4 method in python
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