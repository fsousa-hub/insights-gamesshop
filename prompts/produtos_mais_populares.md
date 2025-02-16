# Quais são os produtos mais populares em cada país.

# Prompt:
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

Com base no Tipos de Dados crie um script python que informe quais são os produtos mais populares em cada país. Informe o faturamento acumulado com base no site use os campos [site, quantity, unit_price, total_price, discount_value ] apresente com titulo "Faturamento acumulado por site". Informe quais são o 5 clientes com o maior valor e compra, use os campos [buyer_name, total_price] apresente com o titulo "Top 5 em Compras". Exiba o resultado no console. Exporte o resultado em um arquivo txt, com o mesmo nome do titulo.

# Resultado:
Gerou um script com nome prod_mais_pop_pais.py faz o seguinte:

1. Lê os dados do arquivo Excel.
2. Calcula os produtos mais populares por país.
3. Calcula o faturamento acumulado por site.
4. Identifica os 5 clientes com o maior valor de compra.
5. Exibe os resultados no console.
6. Exporta os resultados em arquivos TXT com os mesmos nomes dos títulos.
