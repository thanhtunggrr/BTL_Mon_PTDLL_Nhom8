# 1. Import thư viện
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 2. Tải dataset chim cánh cụt
penguins = sns.load_dataset("penguins")

# 3. Xem dữ liệu
print("5 dòng dữ liệu đầu:")
print(penguins.head())

# 4. Làm sạch dữ liệu (loại bỏ giá trị thiếu)
penguins = penguins.dropna()

# 5. Lấy dữ liệu chiều dài vây
flipper_length = penguins["flipper_length_mm"]

# 6. Thống kê cơ bản
print("\nThống kê chiều dài vây của chim cánh cụt")
print("Chiều dài trung bình:", flipper_length.mean())
print("Chiều dài nhỏ nhất:", flipper_length.min())
print("Chiều dài lớn nhất:", flipper_length.max())
print("Độ lệch chuẩn:", flipper_length.std())

# 7. Tính chiều dài vây trung bình theo loài
flipper_by_species = penguins.groupby("species")["flipper_length_mm"].mean()
print("\nChiều dài vây trung bình theo loài:")
print(flipper_by_species)

# 8. Vẽ biểu đồ histogram
plt.figure(figsize=(6,4))
plt.hist(flipper_length, bins=20, color="#20B2AA", edgecolor="black")

plt.title("chiều dài vây của chim cánh cụt")
plt.xlabel("Chiều dài vây (mm)")
plt.ylabel("Số lượng")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()
