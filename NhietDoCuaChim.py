import numpy as np
import IPython.display as display
from matplotlib import pyplot as plt
import io
import base64

temps = 38 + np.random.randn(100) * 0.5
x = [x for x in range(len(temps))]

fig = plt.figure(figsize=(4, 3), facecolor='w')
plt.plot(x, temps, '-')
plt.fill_between(x, temps, 37, where=(temps > 37), facecolor='g', alpha=0.6)
plt.title("Body Temperature of Penguins (~38°C)", fontsize=10)

data = io.BytesIO()
plt.savefig(data)
image = f"data:image/png;base64,{base64.b64encode(data.getvalue()).decode()}"
alt = "Penguin Body Temperature Visualization"
display.display(display.Markdown(f"""![{alt}]({image})"""))
plt.close(fig)
