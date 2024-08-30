# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:24:14 2024

@author: Nguyen Trung Nguyen
"""
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
maxvalue = a
if b > maxvalue:
    maxvalue = b
if c > maxvalue:
    maxvalue = c
print("Giá trị lớn nhất là: ", maxvalue)
