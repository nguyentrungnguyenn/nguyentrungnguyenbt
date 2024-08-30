# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:29:14 2024

@author: Nguyen Trung Nguyen
"""
Ngaysinh = input("Nhập ngày tháng năm sinh:")
Ngay, Thang, Nam = map(float, Ngaysinh.split(" "))
print(f"{Ngay}/{Thang}/{Nam}")
print(f"{Ngay}/{Thang}/{str(Nam)[2:]}")
print(f"{Nam}/{Thang}/{Ngay}")


