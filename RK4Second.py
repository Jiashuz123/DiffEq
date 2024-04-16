'''
File Name: RK4SecondOrder.py
Author: Natasha, Sach, Pheonix, Jiashu
Date: April/2024
Description: RK4 for second order function
'''
from sympy import *
def RungeKutta4(x0, y0, h, tf):
    def f(x, y):
        return 2 * x + 4 * y

    def g(x, y):
        return -x + 6 * y

    # Exact solution
    def x_exact(t):
        return (26 * t - 1) * exp(4 * t)

    def y_exact(t):
        return (13 * t + 6) * exp(4 * t)

    iterations = int((tf - t0) / h)
    x_current = x0
    y_current = y0
    t = t0 + h

    for i in range(iterations):
        k1 = h * f(x_current, y_current)
        l1 = h * g(x_current, y_current)
        k2 = h * f(x_current + k1 / 2, y_current + l1 / 2)
        l2 = h * g(x_current + k1 / 2, y_current + l1 / 2)
        k3 = h * f(x_current + k2 / 2, y_current + l2 / 2)
        l3 = h * g(x_current + k2 / 2, y_current + l2 / 2)
        k4 = h * f(x_current + k3, y_current + l3)
        l4 = h * g(x_current + k3, y_current + l3)

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