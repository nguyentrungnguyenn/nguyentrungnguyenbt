# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:17:22 2024

@author: Nguyen Trung Nguyen
"""
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
d = int(input("Nhập số nguyên d: "))
minvalue = a
if b < minvalue:
    minvalue = b
if c < minvalue:
    minvalue = c
if d < minvalue:
    minvalue = d
print("Giá trị nhỏ nhất là: ", minvalue)
