# 1. Nhập các thư viện cần thiết
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 2. Tải dữ liệu chim cánh cụt
du_lieu_chim = sns.load_dataset("penguins")

# 3. Làm sạch dữ liệu (loại bỏ giá trị bị thiếu)
du_lieu_chim = du_lieu_chim.dropna()

# 4. Tạo dữ liệu nhiệt độ môi trường theo từng đảo
nhiet_do_dao = {
    "Torgersen": -2,
    "Biscoe": 1,
    "Dream": -1
}

# Thêm cột nhiệt độ vào bảng dữ liệu
du_lieu_chim["Nhiet_do_C"] = du_lieu_chim["island"].map(nhiet_do_dao) 
+ np.random.normal(0,1,len(du_lieu_chim))

# 5. Thống kê nhiệt độ
print("Thống kê nhiệt độ môi trường của chim cánh cụt")
print("Trung bình:", round(du_lieu_chim["Nhiet_do_C"].mean(),2),"°C")
print("Nhỏ nhất:", round(du_lieu_chim["Nhiet_do_C"].min(),2),"°C")
print("Lớn nhất:", round(du_lieu_chim["Nhiet_do_C"].max(),2),"°C")

# 6. Tính nhiệt độ trung bình theo đảo
nhiet_do_trung_binh = du_lieu_chim.groupby("island")["Nhiet_do_C"].mean()

print("\nNhiệt độ trung bình theo đảo:")
print(nhiet_do_trung_binh)

# 7. Vẽ biểu đồ
plt.figure(figsize=(8,5))

mau_sac = ["#4C72B0", "#55A868", "#C44E52"]

cot = plt.bar(nhiet_do_trung_binh.index, nhiet_do_trung_binh.values, 
              color=mau_sac)

# Đổi tên hiển thị trục X
plt.xticks(
    ["Torgersen","Biscoe","Dream"],
    ["Biển lạnh","Băng tuyết","Biển bờ đá"]
)

# Hiển thị giá trị trên mỗi cột
for c in cot:
    y = c.get_height()
    plt.text(
        c.get_x()+c.get_width()/2,
        y+0.05,
        round(y,2),
        ha='center'
    )

plt.title("Nhiệt độ môi trường sống của chim cánh cụt")
plt.xlabel("Môi trường sống")
plt.ylabel("Nhiệt độ (°C)")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()
