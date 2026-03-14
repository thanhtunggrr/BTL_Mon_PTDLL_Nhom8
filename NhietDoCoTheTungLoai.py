# 1. Nhập các thư viện cần thiết
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 2. Tải dữ liệu chim cánh cụt
du_lieu_chim = sns.load_dataset("penguins")

# 3. Làm sạch dữ liệu
du_lieu_chim = du_lieu_chim.dropna()

# 4. Tạo dữ liệu nhiệt độ cơ thể giả lập
np.random.seed(42)
du_lieu_chim["Nhiet_do_co_the"] = np.random.normal(38, 0.5, len(du_lieu_chim))

# 5. Thống kê nhiệt độ cơ thể
print("Thống kê nhiệt độ cơ thể chim cánh cụt")
print("Trung bình:", round(du_lieu_chim["Nhiet_do_co_the"].mean(),2),"°C")
print("Nhỏ nhất:", round(du_lieu_chim["Nhiet_do_co_the"].min(),2),"°C")
print("Lớn nhất:", round(du_lieu_chim["Nhiet_do_co_the"].max(),2),"°C")

# 6. Tính nhiệt độ trung bình theo loài
nhiet_do_theo_loai = du_lieu_chim.groupby("species")["Nhiet_do_co_the"].mean()

print("\nNhiệt độ cơ thể trung bình theo loài:")
print(nhiet_do_theo_loai)

# 7. Chuyển dữ liệu sang dạng bảng để vẽ heatmap
heatmap_data = nhiet_do_theo_loai.to_frame()

# 8. Vẽ Heatmap
plt.figure(figsize=(8,5))

sns.heatmap(
    heatmap_data,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5
)

plt.title(" nhiệt độ cơ thể trung bình của các loài chim cánh cụt")
plt.xlabel("Nhiệt độ cơ thể (°C)")
plt.ylabel("Loài chim cánh cụt")

plt.tight_layout()
plt.show()
