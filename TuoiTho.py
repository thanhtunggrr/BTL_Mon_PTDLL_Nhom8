import matplotlib.pyplot as plt
import IPython.display as display
import io
import base64

# Dữ liệu tuổi thọ trung bình (năm)
loai_chim = [
    "Chim cánh cụt Adelie",
    "Chim cánh cụt Chinstrap",
    "Chim cánh cụt Gentoo"

]

tuoi_tho = [15, 18, 17]

fig = plt.figure(figsize=(6,4), facecolor='white')

mau_sac = ["#6A5ACD", "#20B2AA", "#FF8C00"]

plt.bar(loai_chim, tuoi_tho, color=mau_sac)

plt.title("Tuổi thọ trung bình của các loài chim cánh cụt")
plt.xlabel("Loài chim cánh cụt")
plt.ylabel("Tuổi thọ trung bình (năm)")
plt.xticks(rotation=20)

plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()

data = io.BytesIO()
plt.savefig(data, bbox_inches='tight')
image = f"data:image/png;base64,{base64.b64encode(data.getvalue()).decode()}"
alt = "Biểu đồ tuổi thọ chim cánh cụt"
display.display(display.Markdown(f"""![{alt}]({image})"""))
plt.close(fig)
