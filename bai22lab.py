# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:32:48 2024

@author: Nguyen Trung Nguyen
"""
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
if a == 0 and b == 0:
    print("Phương trình có vô số nghiệm.")
elif a == 0 and b != 0:
    print("Phương trình vô nghiệm.")
elif a != 0:
    print("Phương trình có nghiệm duy nhất: ", -b/a)
else:
    print("Không hợp lệ.")
    

