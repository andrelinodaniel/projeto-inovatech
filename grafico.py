import pandas as pd
import matplotlib.pyplot as plt


caminho_arquivo = './arquivo.xlsx'


dados = pd.read_excel(caminho_arquivo)


dados['Valor Final'] = dados['Valor Final'].str.replace('$', '').astype(float)


faturamento_loja = dados.groupby('ID Loja')['Valor Final'].sum()


faturamento_loja.plot(kind='bar', figsize=(10, 6))

nomes_lojas = faturamento_loja.index.tolist()

plt.title('Faturamento por Loja')
plt.xticks(range(len(nomes_lojas)), nomes_lojas)
plt.ylabel('Faturamento')
plt.show()


ranking_lojas = faturamento_loja.sort_values(ascending=False)
print('Ranking de Faturamento por Loja:')
print(ranking_lojas)
