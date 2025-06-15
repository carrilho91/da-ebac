import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Lê o arquivo CSV
df = pd.read_csv("gasolina.csv")

# Cria o gráfico
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="dia", y="venda", marker="o")

# Ajustes de layout
plt.title("Preço médio da gasolina em São Paulo - Julho/2021")
plt.xlabel("Dia")
plt.ylabel("Preço (R$)")
plt.grid(True)

# Salva o gráfico em PNG
plt.savefig("gasolina.png")
plt.close()
