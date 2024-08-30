# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:05:06 2024

@author: Nguyen Trung Nguyen
"""
thoi_gian1 = input("Nhập thời gian thứ nhất(hh:ss:mm): ")
thoi_gian2 = input("Nhập thời gian thứ hai(hh:ss:mm): ")
hh, mm, ss = map(int, thoi_gian1.split(":"))
h, m, s = map(int, thoi_gian2.split(":"))
tong_giay1 = hh*3600 + mm*60 + ss
tong_giay2 = h*3600 + m*60 + s
hieu_thoi_gian = tong_giay1 - tong_giay2
if hieu_thoi_gian > 0:
    h1 = hieu_thoi_gian // 3600
    m1 = (hieu_thoi_gian % 3600) // 60
    s1 = hieu_thoi_gian % 60
    print(f"Hiệu của hai thời gian là: {h1}:{m1}:{s1}")
else:
    print("Thời gian nhỏ hơn!")
tong_thoi_gian = tong_giay1 + tong_giay2
h2 = tong_thoi_gian // 3600
m2 = (tong_thoi_gian % 3600) // 60
s2 = tong_thoi_gian % 60
print(f"Tổng của hai thời gian là: {h2}:{m2}:{s2}")