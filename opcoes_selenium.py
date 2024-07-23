# Tutorial de instalação webdriver
# sudo apt update
# sudo apt install -y wget gnupg
# wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
# sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list'
# sudo apt update
# sudo apt install -y google-chrome-stable
# google-chrome --version


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Configurar opções do Chrome
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Usar o WebDriver Manager para gerenciar o ChromeDriver
service = Service(ChromeDriverManager().install())

# Iniciar o driver do Selenium com as opções configuradas
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Abrir a página
    driver.get('https://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/consultas/mercado-a-vista/opcoes/posicoes-em-aberto/posicoes-em-aberto-8AE490C877D179740177DEC0BF4C5BD2.htm?empresaEmissora=BCO%20BRASIL%20S.A.&data=22/07/2024&f=0')

    # Esperar que a tabela seja carregada
    table_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="2024081670ONNM"]'))
    )

    # Ler a tabela em um DataFrame do pandas
    table_html = table_element.get_attribute('outerHTML')
    df = pd.read_html(table_html)[0]

    # Mostrar as primeiras linhas do DataFrame
    print(df)

    # Salvar o DataFrame em um arquivo CSV
    df.to_csv('posicoes_em_aberto.csv', index=False)
finally:
    # Fechar o driver do Selenium
    driver.quit()
