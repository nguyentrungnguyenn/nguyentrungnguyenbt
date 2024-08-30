# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:03:57 2024

@author: Nguyen Trung Nguyen
"""
a = input("Nhập 1 chữ cái: ")
if a.islower():
    coverted_a = a.upper()
    print("Chữ cái sau chuyển đổi là: ", coverted_a)
if a.isupper():
    converted_b = a.lower()
    print("Chữ cái sau chuyển đổi là: ", converted_b)
    
