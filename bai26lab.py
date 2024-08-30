# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:17:53 2024

@author: Nguyen Trung Nguyen
"""
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a




N = int(input("nhập số nguyên N: "))
danh_sach = list(N)
sap_xep = danh_sach.sort()
sap_xep_danh_sach = "".join(danh_sach)
print(sap_xep_danh_sach)
    