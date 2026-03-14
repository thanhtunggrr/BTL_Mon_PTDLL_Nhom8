import matplotlib.pyplot as plt
import IPython.display as display
import io
import base64
import seaborn as sns
import pandas as pd

# Dữ liệu tuổi thọ trung bình (năm)
loai_chim = [
    "Chim cánh cụt Adelie",
    "Chim cánh cụt Chinstrap",
    "Chim cánh cụt Gentoo"
]

tuoi_tho = [15, 18, 17]

# Chuyển dữ liệu sang dạng DataFrame
data_penguin = pd.DataFrame({
    "Loai": loai_chim,
    "TuoiTho": tuoi_tho,
    "Index": [1, 2, 3]   # dùng để vẽ regression
})

fig = plt.figure(figsize=(6,4), facecolor='white')

# Vẽ Regression Plot
sns.regplot(
    x="Index",
    y="TuoiTho",
    data=data_penguin,
    scatter_kws={"s":120},
    line_kws={"color":"red"}
)

plt.title("Tuổi thọ trung bình của các loài chim cánh cụt")
plt.xlabel("Chỉ số loài chim cánh cụt")
plt.ylabel("Tuổi thọ trung bình (năm)")

plt.xticks([1,2,3], loai_chim, rotation=20)

plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()

data = io.BytesIO()
plt.savefig(data, bbox_inches='tight')

image = f"data:image/png;base64,{base64.b64encode(data.getvalue()).decode()}"
alt = "Regression Plot tuổi thọ chim cánh cụt"

display.display(display.Markdown(f"""![{alt}]({image})"""))

plt.close(fig)
