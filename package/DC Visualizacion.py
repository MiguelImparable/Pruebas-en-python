# %%
import matplotlib.pyplot as plt

# 1. Estructura
x = list(range(10))
y = x

# 1.1 Figura
fig = plt.figure(figsize=(10, 6))

# 1.2 Axes
plt.title('ONE LINE')
plt.plot(x, y)
plt.show()
