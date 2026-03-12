import numpy as np
import IPython.display as display
from matplotlib import pyplot as plt
import io
import base64

# Dữ liệu giả lập về thức ăn của chim cánh cụt
foods = ["Cá", "Krill", "Mực"]
food_percent = [50, 35, 15]

# Dữ liệu về môi trường sống
habitats = ["Biển lạnh", "Băng tuyết", "Bờ biển đá"]
habitat_percent = [60, 25, 15]

fig = plt.figure(figsize=(8,4), facecolor='white')

# Biểu đồ 1: Thức ăn
plt.subplot(1,2,1)
colors_food = ["#6A5ACD", "#FF8C00", "#20B2AA"]  # màu lạ
plt.pie(food_percent, labels=foods, autopct='%1.0f%%', colors=colors_food, startangle=90)
plt.title("Thức ăn của chim cánh cụt")

# Biểu đồ 2: Môi trường sống
plt.subplot(1,2,2)
colors_habitat = ["#00CED1", "#9370DB", "#FF7F50"]
plt.bar(habitats, habitat_percent, color=colors_habitat)
plt.title("Môi trường sống của chim cánh cụt")
plt.ylabel("Tỷ lệ (%)")

plt.tight_layout()

data = io.BytesIO()
plt.savefig(data)
image = f"data:image/png;base64,{base64.b64encode(data.getvalue()).decode()}"
alt = "Phân tích chim cánh cụt"
display.display(display.Markdown(f"""![{alt}]({image})"""))
plt.close(fig)
