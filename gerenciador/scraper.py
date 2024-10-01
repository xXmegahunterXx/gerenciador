from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class Scraper:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.chrome_options.add_argument("--disable-gpu")
        self.chrome_options.add_argument("--no-sandbox")
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)

    def login(self):
        self.driver.get('https://painel.infinitetv.fun/panel.php')
        self.driver.find_element(By.NAME, 'username').send_keys(self.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        self.driver.find_element(By.XPATH, '//button[text()="Log In"]').click()
        # Fecha o pop-up
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'btn-close'))
        ).click()

    def get_clientes(self):
        try:
            self.login()
            # Navega até o menu "Clientes"
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Clientes'))
            ).click()
            # Espera o carregamento da tabela
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, 'DataTables_Table_0'))
            )
            # Extrai os dados
            clientes = []
            table = self.driver.find_element(By.ID, 'DataTables_Table_0')
            rows = table.find_elements(By.TAG_NAME, 'tr')
            for row in rows[1:]:
                cols = row.find_elements(By.TAG_NAME, 'td')
                if cols:
                    cliente = {
                        'id': cols[0].text,
                        'nome': cols[1].text,
                        'status': cols[2].text,
                        'acoes': cols[3].text,
                    }
                    clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f"Erro durante o scraping: {e}")
            return []
        finally:
            self.driver.quit()
