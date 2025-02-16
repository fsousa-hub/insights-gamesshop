# Transformar dados de vendas sem informações relevantes para a fabricante.

# Prompt:
Com base no cenário atual e nos arquivo em anexo imagem base_dados.png, e Meganium_Sales_data.xlsx:
- Cenário:
    - A empresa foca apenas em fabricação de consoles, deixando a distribuição e venda para terceiros.
    - Os produtos são vendidos globalmente.
- Arquivos em anexo:
    - base_dados.png
    - Meganium_Sales_data.xlsx

Transforme os dados de vendas sem informações relevantes para a fabricante.

# Resultado:
Para transformar os dados de vendas e excluir informações irrelevantes para a fabricante, focando apenas nos pontos relevantes, podemos seguir os seguintes passos:

1. Carregar os dados do arquivo Meganium_Sales_data.xlsx.
2. Filtrar as colunas que são relevantes para a fabricação de consoles.
3. Excluir as informações de distribuição e vendas realizadas por terceiros.
4. Focar nas seguintes informações:
    . Quantidade de consoles fabricados por período.
    . Regiões de maior demanda para fabricação.
    . Tendências de mercado que impactam a fabricação.
    . Feedback dos distribuidores sobre a qualidade dos consoles.


Gerou um script nome dados_relevantes faz o seguinte:
1. Lê os dados do arquivo Excel.
2. Filtra as colunas relevantes para a fabricação de consoles.
3. Agrupa os dados por período e soma a quantidade de consoles fabricados.
4. Obtém as regiões de maior demanda, tendências de mercado e feedback dos distribuidores.
5. Exibe os dados transformados.


# Prompt atualizado, com as informações do insight info.txt:

- Tipos de Dados:
 - SKU: object
 - product_sold: object
 - date: datetime64[ns]
 - quantity: int64
 - unit_price: int64
 - total_price: int64
 - currency: object
 - site: object
 - discount_coupon: object
 - discount_value: float64
 - buyer_birth_date: datetime64[ns]  - buyer_name: object
 - delivery_country: object
 - invoice_id: object

Com base no Tipos de Dados modifique o script para obter as regiões de maior demanda para isso use o campo [delivery_country], e verificar a tendência de mercado utilize o campo [product_sold] 

# Resultado:
Este script faz o seguinte:

1. Lê os dados do arquivo Excel.
2. Filtra as colunas relevantes para a fabricação de consoles (date, quantity, delivery_country, product_sold).
3. Agrupa os dados por período (date) e soma a quantidade de consoles fabricados.
4. Obtém as regiões de maior demanda usando o campo delivery_country.
5. Verifica a tendência de mercado usando o campo product_sold.
6. Exibe os dados transformados.

# Prompt atualizado, para retornar o resultado quantidade_por_periodo considerando o mês e o trimestre.

# Resultado:
Este script faz o seguinte:

1. Lê os dados do arquivo Excel.
2. Filtra as colunas relevantes para a fabricação de consoles (date, quantity, delivery_country, product_sold).
3. Converte a coluna date para o tipo datetime.
4. Agrupa os dados por mês e soma a quantidade de consoles fabricados.
5. Agrupa os dados por trimestre e soma a quantidade de consoles fabricados.
6. Obtém as regiões de maior demanda usando o campo delivery_country.
7. Verifica a tendência de mercado usando o campo product_sold.
8. Exibe os dados transformados.


# Prompt atualizado: Atualize o código para exportar os dados nos formatos txt, csv e excel com o nome info_dados_relevantes.

Este script faz o seguinte:

1. Lê os dados do arquivo Excel.
2. Filtra as colunas relevantes para a fabricação de consoles (date, quantity, delivery_country, product_sold).
3. Converte a coluna date para o tipo datetime.
4. Agrupa os dados por mês e soma a quantidade de consoles fabricados.
5. Agrupa os dados por trimestre e soma a quantidade de consoles fabricados.
6. Obtém as regiões de maior demanda usando o campo delivery_country.
7. Verifica a tendência de mercado usando o campo product_sold.
8. Exibe os dados transformados.
9. Exporta os dados transformados nos formatos CSV, Excel e TXT com o nome info_dados_relevantes.