# 1. Import thư viện
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx

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

# 7. Tạo graph hierarchy
G = nx.DiGraph()

# Nút gốc
G.add_node("Penguins")

# Thêm các loài làm nhánh
for species, value in bill_depth_species.items():
    label = f"{species}\n{round(value,2)} mm"
    G.add_node(label)
    G.add_edge("Penguins", label)

# 8. Vẽ biểu đồ
plt.figure(figsize=(6,4))

pos = nx.spring_layout(G, seed=42)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="lightblue",
    node_size=2500,
    font_size=9
)

plt.title(" độ dày mỏ trung bình của các loài chim cánh cụt")

plt.tight_layout()
plt.show()
