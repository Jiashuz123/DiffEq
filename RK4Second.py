'''
File Name: RK4SecondOrder.py
Author: Natasha, Sach, Pheonix, Jiashu
Date: April/2024
Description: RK4 for second order function

The script defines the RungeKutta4 function, which takes the following inputs:

- x0: The initial value of the first dependent variable (x).
- y0: The initial value of the second dependent variable (y).
- h: The step size for numerical integration.
- tf: The final value of the independent variable (t) at which the solution is desired.

The RungeKutta4 function performs the following steps:

1. It defines the original system of differential equations (f and g) and the exact analytical solutions (x_exact and y_exact) for calculating the errors.
2. It calculates the total number of iterations required to reach tf from t0 based on the given step size (h).
3. It initializes the current values of x and y with the given initial conditions (x0 and y0).
4. It iterates over the number of iterations:
  a. It calculates the four slopes (k1, k2, k3, k4) and (l1, l2, l3, l4) for the two ODEs using the RK4 method.
  b. It calculates the next values of x and y using the RK4 formula: x_next = x_current + (k1 + 2*k2 + 2*k3 + k4) / 6 and y_next = y_current + (l1 + 2*l2 + 2*l3 + l4) / 6.
  c. It calculates the exact values of x and y at the current time (t) using the analytical solutions.
  d. It calculates the absolute errors between the numerical and exact solutions for x and y.
  e. It prints the current time (t), numerical solutions (x_next, y_next), exact solutions (x_exact_value, y_exact_value), and absolute errors (x_abs_error, y_abs_error).
  f. It updates the current values of x and y for the next iteration.
  g. It increments the time (t) by the step size (h).
5. After the iterations, the function returns the final values of x and y.

The script also includes an example usage, where it solves the system of second-order ODEs with initial conditions x0 = -1, y0 = 6, and step sizes of 0.001, 0.002, and 0.004. The final time (tf) is set to 0.01.

Note: The script assumes that the analytical solutions for the system of ODEs are x_exact(t) = (26*t - 1)*exp(4*t) and y_exact(t) = (13*t + 6)*exp(4*t). These solutions are used to calculate the exact values and the errors.
'''
from sympy import *
def RungeKutta4(x0, y0, h, tf):
    #This function requires 4 inputs: Initial conditions for x and y, the step size, and the final t value
    #define the original differential equations
    def f(x, y):
        return 2 * x + 4 * y

    def g(x, y):
        return -x + 6 * y

    # Exact solution (used to calculate the errors) 
    def x_exact(t):
        return (26 * t - 1) * exp(4 * t)

    def y_exact(t):
        return (13 * t + 6) * exp(4 * t)
    #This calculate the total number of iterations and update the x and y values
    iterations = int((tf - t0) / h)
    x_current = x0
    y_current = y0
    t = t0 + h

    for i in range(iterations):
        #This calculate the first slope in the RK4 method
        k1 = h * f(x_current, y_current)
        l1 = h * g(x_current, y_current)
        #This calculate the second slope in the RK4 method
        k2 = h * f(x_current + k1 / 2, y_current + l1 / 2)
        l2 = h * g(x_current + k1 / 2, y_current + l1 / 2)
        #This calculate the third slope in the RK4 method
        k3 = h * f(x_current + k2 / 2, y_current + l2 / 2)
        l3 = h * g(x_current + k2 / 2, y_current + l2 / 2)
        #This calculate the fourth slope in the RK4 method
        k4 = h * f(x_current + k3, y_current + l3)
        l4 = h * g(x_current + k3, y_current + l3)
        #This calculate the y value and x values
        x_next = x_current + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        y_next = y_current + (l1 + 2 * l2 + 2 * l3 + l4) / 6

        # Calculate absolute error
        x_exact_value = x_exact(t)
        y_exact_value = y_exact(t)
        x_abs_error = abs(x_next - x_exact_value)
        y_abs_error = abs(y_next - y_exact_value)

        print(f"t = {t:.4f}, x = {x_next:.15f}, y = {y_next:.15f}, x_exact ={x_exact_value:.15f}, x_abs_error = {x_abs_error:.15f}, y_exact ={y_exact_value:.15f} y_abs_error = {y_abs_error:.15f}")

        x_current = x_next
        y_current = y_next
        t += h  # Increment time by the step size

    return x_current, y_current

x0 = -1
y0 = 6
h = 0.001
t0 = 0
tf = 0.01
print("h = 0.001")
result = RungeKutta4(x0, y0, h, tf)
print("h = 0.002")
result = RungeKutta4(x0, y0, h*2, tf)
print("h = 0.004")
result = RungeKutta4(x0, y0, h*4, tf)
