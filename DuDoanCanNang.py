import numpy as np
import pandas as pd
import seaborn as sns
import IPython.display as display
from matplotlib import pyplot as plt

import io
import base64

# Thư viện Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# =========================
# 1. Load dữ liệu chim cánh cụt
# =========================
penguins = sns.load_dataset("penguins")

# Xóa dữ liệu bị thiếu
penguins = penguins.dropna()


# =========================
# 2. Chọn dữ liệu dự đoán cân nặng
# =========================
X = penguins[['bill_length_mm','bill_depth_mm','flipper_length_mm']]
y = penguins['body_mass_g']


# =========================
# 3. Chia dữ liệu train và test
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)


# =========================
# 4. Tạo mô hình Linear Regression
# =========================
model = LinearRegression()
model.fit(X_train, y_train)


# =========================
# 5. Dự đoán cân nặng
# =========================
y_pred = model.predict(X_test)


# =========================
# 6. Đánh giá mô hình
# =========================
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Sai số MSE:", mse)
print("Độ chính xác R2:", r2)


# =========================
# 7. Biểu đồ chart so sánh cân nặng
# =========================
fig = plt.figure(figsize=(8,4), facecolor='white')

plt.scatter(y_test, y_pred,
            color="#6A5ACD",
            alpha=0.7)

plt.xlabel("Cân nặng thực tế (gram)")
plt.ylabel("Cân nặng dự đoán (gram)")
plt.title("Linear Regression dự đoán cân nặng chim cánh cụt")

# Vẽ đường chuẩn
plt.plot([y_test.min(), y_test.max()],
         [y_test.min(), y_test.max()],
         color="red")

plt.tight_layout()


# =========================
# 8. Hiển thị hình giống code của bạn
# =========================
data = io.BytesIO()
plt.savefig(data)

image = f"data:image/png;base64,{base64.b64encode(data.getvalue()).decode()}"

alt = "Biểu đồ Linear Regression chim cánh cụt"

display.display(display.Markdown(f"""![{alt}]({image})"""))

plt.close(fig)
