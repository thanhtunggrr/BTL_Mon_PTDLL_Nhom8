import seaborn as sns
import IPython.display as display
from matplotlib import pyplot as plt
import io
import base64

# Tải dữ liệu chim cánh cụt
penguins = sns.load_dataset("penguins")

# Tính giá trị trung bình của các bộ phận
dac_diem = {
    "Độ dài mỏ (mm)": penguins["bill_length_mm"].mean(),
    "Độ dày mỏ (mm)": penguins["bill_depth_mm"].mean(),
    "Độ dài cánh (mm)": penguins["flipper_length_mm"].mean(),
    "KL cơ thể (g)": penguins["body_mass_g"].mean()
}

labels = list(dac_diem.keys())
values = list(dac_diem.values())

fig = plt.figure(figsize=(6,4), facecolor='w')

plt.bar(labels, values)
plt.title("Các đặc điểm cơ thể của chim cánh cụt", fontsize=11)
plt.xlabel("Bộ phận cơ thể")
plt.ylabel("Giá trị trung bình")
plt.xticks(rotation=20)
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()   # giúp không bị mất chữ

data = io.BytesIO()
plt.savefig(data, bbox_inches='tight')  # tránh cắt chữ
image = f"data:image/png;base64,{base64.b64encode(data.getvalue()).decode()}"
alt = "Biểu đồ đặc điểm chim cánh cụt"
display.display(display.Markdown(f"""![{alt}]({image})"""))
plt.close(fig)
