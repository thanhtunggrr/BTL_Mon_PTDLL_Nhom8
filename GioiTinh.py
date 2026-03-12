import seaborn as sns
import matplotlib.pyplot as plt
import IPython.display as display
import io
import base64

# Tải dữ liệu chim cánh cụt
penguins = sns.load_dataset("penguins")

# Đếm số lượng theo giới tính
gioi_tinh = penguins["sex"].value_counts()

labels = ["Con đực", "Con cái"]
values = gioi_tinh.values

fig = plt.figure(figsize=(5,4), facecolor='white')

mau = ["#6A5ACD", "#FF69B4"]

plt.pie(values, labels=labels, autopct='%1.1f%%', colors=mau, startangle=90)
plt.title("Tỷ lệ giới tính của chim cánh cụt")

plt.axis("equal")

plt.tight_layout()

data = io.BytesIO()
plt.savefig(data, bbox_inches='tight')
image = f"data:image/png;base64,{base64.b64encode(data.getvalue()).decode()}"
alt = "Biểu đồ giới tính chim cánh cụt"
display.display(display.Markdown(f"""![{alt}]({image})"""))
plt.close(fig)
