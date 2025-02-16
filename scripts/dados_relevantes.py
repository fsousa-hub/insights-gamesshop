import pandas as pd

def ler_dados_excel(nome_arquivo):
    dados = pd.read_excel(nome_arquivo)
    return dados

def transformar_dados(dados):
    # Selecionar colunas relevantes
    colunas_relevantes = ['date', 'quantity', 'delivery_country', 'product_sold']
    dados_relevantes = dados[colunas_relevantes]
    
    # Converter a coluna 'date' para datetime
    dados_relevantes['date'] = pd.to_datetime(dados_relevantes['date'])
    
    # Agrupar por mês e somar a quantidade de consoles fabricados
    quantidade_por_mes = dados_relevantes.resample('M', on='date')['quantity'].sum().reset_index()
    
    # Agrupar por trimestre e somar a quantidade de consoles fabricados
    quantidade_por_trimestre = dados_relevantes.resample('Q', on='date')['quantity'].sum().reset_index()
    
    # Obter regiões de maior demanda
    regioes_maior_demanda = dados_relevantes.groupby('delivery_country')['quantity'].sum().reset_index()
    
    # Obter tendências de mercado
    tendencias_mercado = dados_relevantes['product_sold'].value_counts().reset_index()
    tendencias_mercado.columns = ['product_sold', 'count']
    
    return quantidade_por_mes, quantidade_por_trimestre, regioes_maior_demanda, tendencias_mercado

def exibir_dados(dados):
    for dado in dados:
        print(dado)
        print()

def exportar_dados(dados):
    quantidade_por_mes, quantidade_por_trimestre, regioes_maior_demanda, tendencias_mercado = dados
    
    # Exportar para CSV
    quantidade_por_mes.to_csv('info_dados_relevantes_mes.csv', index=False)
    quantidade_por_trimestre.to_csv('info_dados_relevantes_trimestre.csv', index=False)
    regioes_maior_demanda.to_csv('info_dados_relevantes_regioes.csv', index=False)
    tendencias_mercado.to_csv('info_dados_relevantes_tendencias.csv', index=False)
    
    # Exportar para Excel
    with pd.ExcelWriter('info_dados_relevantes.xlsx') as writer:
        quantidade_por_mes.to_excel(writer, sheet_name='Mes', index=False)
        quantidade_por_trimestre.to_excel(writer, sheet_name='Trimestre', index=False)
        regioes_maior_demanda.to_excel(writer, sheet_name='Regioes', index=False)
        tendencias_mercado.to_excel(writer, sheet_name='Tendencias', index=False)
    
    # Exportar para TXT
    with open('info_dados_relevantes.txt', 'w') as f:
        f.write('Quantidade por Mes:\n')
        f.write(quantidade_por_mes.to_string(index=False))
        f.write('\n\nQuantidade por Trimestre:\n')
        f.write(quantidade_por_trimestre.to_string(index=False))
        f.write('\n\nRegioes de Maior Demanda:\n')
        f.write(regioes_maior_demanda.to_string(index=False))
        f.write('\n\nTendencias de Mercado:\n')
        f.write(tendencias_mercado.to_string(index=False))

def main():
    nome_arquivo = 'C:\\Git Entrega\\project-base-prompt-vendas\\data\\processed_data\\Meganium_Sales_data.xlsx'
    dados = ler_dados_excel(nome_arquivo)
    dados_transformados = transformar_dados(dados)
    exibir_dados(dados_transformados)
    exportar_dados(dados_transformados)

if __name__ == "__main__":
    main()