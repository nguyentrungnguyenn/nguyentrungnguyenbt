# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:42:41 2024

@author: Nguyen Trung Nguyen
"""
import math
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
denta = b**2 - 4*a*c
if a == 0:
    print("phương trình có nghiệm duy nhất x = ", -b/c)
elif a != 0 and denta < 0:
    print("Phương trình vô nghiệm.")
elif a !=0 and denta == 0:
    print("Phương trình có nghiệm kép x1 = x2 = ", -b/(2*a))
elif a != 0 and denta > 0:
    print("Phương trình có 2 nghiệm phân biệt x1 = ", (-b + math.sqrt(denta))/(2*a))
    print("Phương trình có 2 nghiệm phân biệt x2 = ", (-b - math.sqrt(denta))/(2*a))