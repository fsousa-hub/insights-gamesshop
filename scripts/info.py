import pandas as pd

def ler_dados_excel(nome_arquivo):
    dados = pd.read_excel(nome_arquivo)
    return dados

def resumo_dados(dados):
    resumo = {
        'Colunas': dados.columns.tolist(),  # Lista
        'Tipos de Dados': dados.dtypes.to_dict(),  # Dicionário
        'Dados Ausentes': dados.isnull().sum().to_dict(),  # Dicionário
        'Estatísticas Descritivas': dados.describe(include='all').to_dict()  # Dicionário
    }
    return resumo

def exibir_resumo(resumo):
    linhas = []  # Lista para armazenar os dados a serem exportados
    texto = []  # Lista para armazenar os dados para o arquivo txt
    
    for chave, valor in resumo.items():
        print(f"{chave}:")
        texto.append(f"{chave}:")
        
        if isinstance(valor, dict):
            for sub_chave, sub_valor in valor.items():
                print(f"  {sub_chave}: {sub_valor}")
                texto.append(f"  {sub_chave}: {sub_valor}")
                linhas.append([chave, sub_chave, sub_valor])  # Adiciona ao CSV

        elif isinstance(valor, list):
            for item in valor:
                print(f"  - {item}")
                texto.append(f"  - {item}")
                linhas.append([chave, item, ""])  # Adiciona ao CSV

        else:
            print(f"  {valor}")
            texto.append(f"  {valor}")
            linhas.append([chave, "", valor])  # Adiciona ao CSV
        
        print()
        texto.append("")
    
    # Exporta os dados para CSV
    df_export = pd.DataFrame(linhas, columns=["Categoria", "Item", "Valor"])
    df_export.to_csv("info.csv", index=False, encoding='utf-8')
    print("Resumo exportado para info.csv")
    
    # Exporta os dados para TXT
    with open("info.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(texto))
    print("Resumo exportado para info.txt")

def main():
    nome_arquivo = 'C:\\Git Entrega\\project-base-prompt-vendas\\data\\processed_data\\Meganium_Sales_data.xlsx'
    dados = ler_dados_excel(nome_arquivo)
    resumo = resumo_dados(dados)
    exibir_resumo(resumo)

if __name__ == "__main__":
    main()