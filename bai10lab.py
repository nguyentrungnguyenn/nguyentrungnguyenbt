# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:56:49 2024

@author: Nguyen Trung Nguyen
"""
soxe = int(input("Nhập số xe của bạn:"))
Chu_so_hang_nghin = soxe // 1000
Chu_so_hang_tram = (soxe % 1000) // 100
Chu_so_hang_chuc = ((soxe % 1000) % 100) // 10
Chu_so_hang_don_vi = soxe % 10
Tong_cac_chu_so = Chu_so_hang_nghin + Chu_so_hang_tram + Chu_so_hang_chuc + Chu_so_hang_don_vi
a = Tong_cac_chu_so // 10
b = Tong_cac_chu_so % 10
sonut = a + b
c = sonut // 10
d = sonut % 10
print("Số nút của xe bạn là:", c + d)
