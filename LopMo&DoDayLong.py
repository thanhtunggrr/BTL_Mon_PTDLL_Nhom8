# 1. Nhập thư viện
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 2. Tải dữ liệu chim cánh cụt
du_lieu = sns.load_dataset("penguins")

# 3. Làm sạch dữ liệu
du_lieu = du_lieu.dropna()

# 4. Tạo dữ liệu mô phỏng lớp mỡ và độ dày lông
np.random.seed(1)

du_lieu["Lop_mo_cm"] = np.random.normal(3.5, 0.6, len(du_lieu))   
du_lieu["Do_day_long_mm"] = np.random.normal(25, 3, len(du_lieu)) 

# 5. Thống kê dữ liệu
print("THỐNG KÊ LỚP MỠ CHIM CÁNH CỤT")
print("Trung bình:", round(du_lieu["Lop_mo_cm"].mean(),2), "cm")
print("Nhỏ nhất:", round(du_lieu["Lop_mo_cm"].min(),2), "cm")
print("Lớn nhất:", round(du_lieu["Lop_mo_cm"].max(),2), "cm")

print("\nTHỐNG KÊ ĐỘ DÀY LÔNG")
print("Trung bình:", round(du_lieu["Do_day_long_mm"].mean(),2), "mm")
print("Nhỏ nhất:", round(du_lieu["Do_day_long_mm"].min(),2), "mm")
print("Lớn nhất:", round(du_lieu["Do_day_long_mm"].max(),2), "mm")

# 6. Tính trung bình theo loài
trung_binh = du_lieu.groupby("species")[["Lop_mo_cm","Do_day_long_mm"]].mean()

print("\nTrung bình theo loài:")
print(trung_binh)

# 7. Vẽ biểu đồ so sánh
plt.figure(figsize=(8,5))

x = np.arange(len(trung_binh.index))
width = 0.35

plt.bar(x - width/2, trung_binh["Lop_mo_cm"], width,
        label="Lớp mỡ (cm)", color="#4C72B0")

plt.bar(x + width/2, trung_binh["Do_day_long_mm"], width,
        label="Độ dày lông (mm)", color="#55A868")

plt.xticks(x, trung_binh.index)

plt.title("So sánh lớp mỡ và độ dày lông của các loài chim cánh cụt")
plt.xlabel("Loài chim cánh cụt")
plt.ylabel("Giá trị")

plt.legend()

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()
