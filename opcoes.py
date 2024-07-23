import requests
from lxml import html

# URL da página
url = 'https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/mercado-a-vista/opcoes/posicoes-em-aberto/posicoes-em-aberto-8AE490C877D179740177DEC0BF4C5BD2.htm?empresaEmissora=BCO%20BRASIL%20S.A.&data=22/07/2024&f=0'

# Solicitação HTTP para obter o conteúdo da página
response = requests.get(url)
html_content = response.content

# Usando lxml para analisar o HTML
tree = html.fromstring(html_content)

# Verificar se o XPath encontra o elemento
elements = tree.xpath('//*[@id="2024072670ONNM"]')
print(f"Número de elementos encontrados: {len(elements)}")

if elements:
    table = elements[0]
    print(html.tostring(table, pretty_print=True).decode())
else:
    print("Elemento não encontrado.")
