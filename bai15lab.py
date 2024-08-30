# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 18:31:57 2024

@author: Nguyen Trung Nguyen
"""
a = int(input("Nhập số a:"))
b = int(input("Nhập số b:"))
A = ((a + b)/ (pow(a, (1 / 3)) + pow(b, (1 / 3)))) - pow(a * b, (1 / 3))
B = ((pow(a, (1 / 3))) - (pow(b, (1 / 3))))**2
print("Kết quả của biểu thức là:", A / B)

