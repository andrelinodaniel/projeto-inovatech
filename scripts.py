import pandas as pd

def calcular_dados(arquivo):
   

 

   tabela = pd.read_excel(arquivo)
   faturamento_todas_as_lojas = format(tabela['Valor Final'].sum(), ',.2f')
   qtd = format(tabela['Quantidade'].sum(), ',.2f')





   return faturamento_todas_as_lojas,qtd