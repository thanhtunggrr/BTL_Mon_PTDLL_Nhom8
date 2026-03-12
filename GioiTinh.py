import seaborn as sns
import matplotlib.pyplot as plt
import IPython.display as display
import io
import base64

# Tải dữ liệu chim cánh cụt
penguins = sns.load_dataset("penguins")

# Đổi giới tính sang tiếng Việt
penguins["Giới_tính"] = penguins["sex"].map({
    "Male": "Con đực",
    "Female": "Con cái"
})

# Tạo figure
fig = plt.figure(figsize=(6,4), facecolor='white')

# Vẽ biểu đồ violin
sns.violinplot(
    data=penguins,
    x="Giới_tính",
    y="body_mass_g",
    palette=["#6A5ACD", "#FF69B4"]
)

plt.xlabel("Giới tính")
plt.ylabel("Khối lượng cơ thể (gram)")
plt.title("Phân bố khối lượng cơ thể chim cánh cụt theo giới tính")

plt.tight_layout()

data = io.BytesIO()
plt.savefig(data, bbox_inches='tight')

image = f"data:image/png;base64,{base64.b64encode(data.getvalue()).decode()}"
alt = "Biểu đồ khối lượng cơ thể chim cánh cụt"

display.display(display.Markdown(f"""![{alt}]({image})"""))

plt.close(fig)
