# 1. Import thư viện
import seaborn as sns
import matplotlib.pyplot as plt

# 2. Tải dữ liệu chim cánh cụt
penguins = sns.load_dataset("penguins")

# 3. Làm sạch dữ liệu
penguins = penguins.dropna()

# 4. Lấy dữ liệu độ dày mỏ
bill_depth = penguins["bill_depth_mm"]

# 5. Thống kê cơ bản
print("Thống kê độ dày mỏ chim cánh cụt")
print("Trung bình:", bill_depth.mean())
print("Nhỏ nhất:", bill_depth.min())
print("Lớn nhất:", bill_depth.max())

# 6. Tính trung bình theo từng loài
bill_depth_species = penguins.groupby("species")["bill_depth_mm"].mean()
print("\nĐộ dày mỏ trung bình theo loài:")
print(bill_depth_species)

# 7. Vẽ biểu đồ
plt.figure(figsize=(6,4))

plt.bar(bill_depth_species.index, bill_depth_species.values)

plt.title("Độ dày mỏ trung bình của các loài chim cánh cụt")
plt.xlabel("Loài chim cánh cụt")
plt.ylabel("Độ dày mỏ (mm)")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()
