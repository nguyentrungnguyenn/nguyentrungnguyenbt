# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:11:45 2024

@author: Nguyen Trung Nguyen
"""
a = int(input("Nhập số nguyên dương a:"))
b = int(input("Nhập số nguyên dương b:"))
Chia_lay_nguyen = a // b
Chia_lay_du = a % b
if a and b > 0:
    print("Chia lấy nguyên của a, b là:", Chia_lay_nguyen)
    print("Chia lấy dư của a, b là:", Chia_lay_du)
else:
    print("Nhập lại 2 số nguyên dương.")
    

