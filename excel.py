import pandas as pd 


#dataframe = pd.read_excel("teste.xlsx")
"""
def converter_numero_para_dinheiro(numero):
    valor = numero
    valor_formatado = format(valor, ',.2f')
    return valor_formatado

def resultado_faturamento():
	soma = 0
	for index, row in dataframe.iterrows():
		soma += row[6]
	
	return converter_numero_para_dinheiro(soma)"""


df = pd.read_excel('vendas.xlsx')



def count_values_in_all_columns(dataframe, show_print=False):
    all_counts = {}
    for column in dataframe.columns:
        counts = dataframe[column].value_counts().to_dict()
        all_counts[column] = counts

        if show_print: 
            for key, freq in counts.items():
                print(f"A COLUNA {column} TEVE O VALOR: {key} {freq} VEZES")

    return all_counts


def count_values_in_column(dataframe, column_name, show_print=False):
    counts = dataframe[column_name].value_counts().to_dict()

    if show_print:
        for key, freq in counts.items():
            print(f"A COLUNA {column_name} TEVE O VALOR: {key} {freq} VEZES")

    return counts




def calcular_dados(nome_coluna):
    tabela = df
    
    if nome_coluna not in tabela.columns:
        return "Erro: Coluna especificada não existe no arquivo."
    
    try:
        faturamento = tabela[nome_coluna].sum()
        faturamento_formatado = format(faturamento, ',.2f')
        return faturamento_formatado
    except TypeError:
        return "Erro: Não é possível somar a coluna especificada."

nome_coluna = "Valor Unitário"

resultado = calcular_dados(nome_coluna)
print(resultado)







