'''
File Name: RK4.py
Author: Natasha, Sach, Pheonix, Jiashu
Date: 03/07/2024
Description: RK4 method in python
'''

from sympy import symbols

def RK4(diffEq, x0, y0, StepSize, xf):
   #This function requires 5 inputs: The differential Equation, initial conditions for x and y, the step size, and the final x value
  x = symbols('x')
  y = symbols('y')
  iterations = int((xf - x0) / StepSize)
  #This calculate the total number of steps
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
  return y0

x = symbols('x')
y = symbols('y')
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
result = RK4(diffEq, x0, y0, StepSize, xf)
print(result)
