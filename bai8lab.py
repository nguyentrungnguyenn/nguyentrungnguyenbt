# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:39:17 2024

@author: Nguyen Trung Nguyen
"""
Can_nang = float(input("Nhập cân nặng (kg): "))
Chieu_cao = float(input("Nhập chiều cao (m): "))
BMI = round(Can_nang / Chieu_cao**2, 2)
print("Số đo kiểm tra sức khỏe của BMI là:", BMI)


