'''
File Name: RK4.py
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
2. It iterates over the number of steps:
  a. It calculates the first slope (k1) using the current values of x0 and y0.
  b. It calculates the second slope (k2) using the intermediate point (x0 + StepSize/2, y0 + StepSize * (k1/2)).
  c. It calculates the third slope (k3) using the intermediate point (x0 + StepSize/2, y0 + StepSize * (k2/2)).
  d. It calculates the fourth slope (k4) using the next point (x0 + StepSize, y0 + StepSize * k3).
  e. It calculates the value of y at the next point (yfinal) using the RK4 formula: yfinal = y0 + (StepSize/6) * (k1 + 2*k2 + 2*k3 + k4).
  f. It updates the values of x0 and y0 for the next iteration.
3. After the iterations, the function returns the final value of y.

The script also includes an example usage, where it solves the differential equation 2*x*y with the initial conditions x0 = 1, y0 = 1, step size of 0.1, and a final value of x = 1.5.

Note: The script uses the SymPy library for symbolic mathematics, which allows the user to input the differential equation in symbolic form.
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
