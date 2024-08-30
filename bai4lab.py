# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:17:53 2024

@author: Nguyen Trung Nguyen
"""
N = int(input("Nhập số nguyên dương N:"))
So_hang_chuc = N // 10
So_hang_don_vi = N % 10
Tong_cac_chu_so_cua_N = So_hang_chuc + So_hang_don_vi
if 10 <= N <= 99:
    print("Tổng các chữ số của N là:", Tong_cac_chu_so_cua_N)
else:
    print("Nhập lại số nguyên có hai chữ số!")

