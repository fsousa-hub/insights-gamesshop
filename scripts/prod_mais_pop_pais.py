import pandas as pd

def ler_dados_excel(nome_arquivo):
    dados = pd.read_excel(nome_arquivo)
    return dados

def produtos_mais_populares_por_pais(dados):
    produtos_populares = dados.groupby('delivery_country')['product_sold'].agg(lambda x: x.value_counts().index[0]).reset_index()
    produtos_populares.columns = ['País', 'Produto Mais Popular']
    return produtos_populares

def faturamento_acumulado_por_site(dados):
    dados['total_faturamento'] = dados['quantity'] * dados['unit_price'] - dados['discount_value']
    faturamento_site = dados.groupby('site')['total_faturamento'].sum().reset_index()
    faturamento_site.columns = ['Site', 'Faturamento Acumulado']
    return faturamento_site

def top_5_em_compras(dados):
    top_5_compras = dados.groupby('buyer_name')['total_price'].sum().reset_index().sort_values(by='total_price', ascending=False).head(5)
    top_5_compras.columns = ['Cliente', 'Valor Total de Compras']
    return top_5_compras

def exibir_dados(titulo, dados):
    print(titulo)
    print(dados)
    print()

def exportar_dados(titulo, dados):
    with open(f'{titulo.replace(" ", "_")}.txt', 'w') as f:
        f.write(f'{titulo}\n')
        f.write(dados.to_string(index=False))

def main():
    nome_arquivo = 'C:\\Git Entrega\\project-base-prompt-vendas\\data\\processed_data\\Meganium_Sales_data.xlsx'
    dados = ler_dados_excel(nome_arquivo)
    
    produtos_populares = produtos_mais_populares_por_pais(dados)
    faturamento_site = faturamento_acumulado_por_site(dados)
    top_5_compras = top_5_em_compras(dados)
    
    exibir_dados('Produtos mais populares por País', produtos_populares)
    exibir_dados('Faturamento acumulado por site', faturamento_site)
    exibir_dados('Top 5 em Compras', top_5_compras)
    
    exportar_dados('Produtos mais populares por País', produtos_populares)
    exportar_dados('Faturamento acumulado por site', faturamento_site)
    exportar_dados('Top 5 em Compras', top_5_compras)

if __name__ == "__main__":
    main()