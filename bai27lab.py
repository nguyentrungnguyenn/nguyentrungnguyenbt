# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:26:35 2024

@author: Nguyen Trung Nguyen
"""
import math
nhap = input("Nhập hình: ")
"n" == "Hình chữ nhật"
"v" == "hình vuông"
"t" == "Hình tròn"
if nhap == "n":
    print("Tính P và S của hình chữ nhật")
    a = int(input("Nhập chiều rộng: "))
    b = int(input("Nhập chiều dài: "))
    P = (a + b) * 2
    S = a * b
    print(f"Kết quả P = {P} S = {S} ")
elif nhap == "v":
    print("Tính P và S của hình vuông")
    a = int(input("Nhập độ dài của cạnh: "))
    P = a * 4
    S = pow(a, 2)
    print(f"Kết quả P = {P} S = {S}")
else:
    print("Tính S và P của hình tròn")
    r = int(input("Nhập bán kính của hình tròn: "))
    P = round(2 * math.pi * r, 2)
    S = round(pow(r, 2) * math.pi, 2)
    print(f"Kết quả P = {P} S = {S}")

