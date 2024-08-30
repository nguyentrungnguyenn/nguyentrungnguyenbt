# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:55:09 2024

@author: Nguyen Trung Nguyen
"""
gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))
if gio > 23 or (phut and giay) > 60:
    print("Thời gian không hợp lệ!")
else:
    print(f"Thời gian hợp lệ {gio}:{phut}:{giay}")