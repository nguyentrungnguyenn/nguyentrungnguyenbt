# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:20:05 2024

@author: Nguyen Trung Nguyen
"""
Thoi_gian = input("Nhập giờ, phút, giây:")
Gio, Phut, Giay = map(int, Thoi_gian.split(":"))
Tong_so_giay = Gio*3600 + Phut*60 + Giay
print("Tổng số giây là:", Tong_so_giay)

