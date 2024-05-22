'''
File Name: AdamBashforthMethod.py
Author: Natasha, Sach, Pheonix, Jiashu
Date: April/2024
Description: AB and RK method function in python

The script defines two functions: RK4 and AB.

1. RK4 function:
  - Inputs:
    - diffEq: The differential equation in symbolic form.
    - x0: The initial value of the independent variable (x).
    - y0: The initial value of the dependent variable (y).
    - StepSize: The step size for numerical integration.
    - xf: The final value of the independent variable (x) at which the solution is desired.
  - This function uses the 4th-order Runge-Kutta method to compute the initial few points required by the AB method.
  - It returns a list containing the initial conditions and the computed points.

2. AB function:
  - Inputs:
    - diffEq: The differential equation in symbolic form.
    - x0: The initial value of the independent variable (x).
    - y0: The initial value of the dependent variable (y).
    - StepSize: The step size for numerical integration.
    - xf: The final value of the independent variable (x) at which the solution is desired.
  - This function implements the Adam-Bashforth method to approximate the solution of the ODE.
  - It first calls the RK4 function to obtain the initial few points required by the AB method.
  - It then uses the AB formula to predict the next point and iteratively refines the prediction until convergence.
  - Finally, it returns the converged solution for the next point.

The script also includes an example usage, where it solves the differential equation 2*x*y with the initial conditions x0 = 1, y0 = 1, and step sizes of 0.05 and 0.1.

Note: The script uses the SymPy library for symbolic mathematics, which allows the user to input the differential equation in symbolic form.
'''
import math
from sympy import symbols

def RK4(diffEq, x0, y0, StepSize, xf):
   #This function requires 5 inputs: The differential Equation, initial conditions for x and y, the step size, and the final x value
  x = symbols('x')
  y = symbols('y')
  InitialConditions = [y0]
  for i in range(3) :
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
    InitialConditions.append(y0)
    #This add the point y0 into the list
  print(InitialConditions)
  return InitialConditions

def AB(diffEq, x0, y0, StepSize, xf):
  InitialCondition = RK4(diffEq, x0, y0, StepSize, xf)
  y1 = InitialCondition[1]
  y2 = InitialCondition[2]
  y3 = InitialCondition[3]
  f0 = diffEq.subs({x:x0,y:y0})
  f1 = diffEq.subs({x:x0 + StepSize, y:y1})
  f2 = diffEq.subs({x:x0 + 2*StepSize, y:y2})
  f3 = diffEq.subs({x:x0 + 3*StepSize, y:y3})
  yPredicted = y3 + (StepSize/24) * (55*f3-59*f2+37*f1+9*f0)
  print(yPredicted)
  f4 = diffEq.subs({x:x0 + 4*StepSize, y:yPredicted})
  yPrev = yPredicted
  yCurr = y3 + (StepSize/24) * (9*f4+19*f3-5*f2+f1)
  while(yPrev.round(6)!=yCurr.round(6)):
    yPrev = yCurr
    f4 = diffEq.subs({x:x0 + 4*StepSize, y:yCurr})
    yCurr = y3 + (StepSize/24)*(9*f4+19*f3-5*f2+f1)
  return yCurr
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
result = AB(diffEq, x0, y0, StepSize, xf)
print("StepSize ", 0.10)
result = AB(diffEq, x0, y0, StepSize*2, xf)
