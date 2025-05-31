from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from datetime import datetime
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request


# --- Configuração do Perfil do Chrome Corrigida ---

CHROME_USER_DATA_DIR = r"C:\Users\F4k3r\AppData\Local\Google\Chrome\User Data\Profile 1"
CHROME_PROFILE_DIRECTORY = "Profile 1"

# --- Configuração da Pasta de Screenshots ---

FolderShots = "PicturesAuto"

# Garante que a pasta de screenshots exista
if not os.path.exists(FolderShots):
    os.makedirs(FolderShots)
    print(f"Pasta '{FolderShots}' criada com sucesso.")
else:
    print(f"Pasta '{FolderShots}' já existe.")
# ---------------------------------------------

# Configura as opções do Chrome para usar o perfil existente
options = Options()
options.add_argument(f"--user-data-dir={CHROME_USER_DATA_DIR}")
options.add_argument(f"--profile-directory={CHROME_PROFILE_DIRECTORY}")
options.add_argument('--log-level=3')

# Inicializa o driver do Chrome com as opções configuradas
try:
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
except Exception as e:
    print(f"Erro ao inicializar o WebDriver: {e}")
    print("Verifique se o Chrome e o ChromeDriver estão atualizados e compatíveis.")
    print("Certifique-se de que o caminho do perfil do Chrome está correto.")
    exit() # Encerra o script se o WebDriver não inicializar
#time.sleep(30)
# --- Configurações ---
SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1CQ0LKwt6kAvAsK1-QSMK75XgZrjuqnYElTuWwrlb264/edit?gid=0#gid=0"
TOKEN_PATH = 'token.json'
CREDENTIALS_PATH = 'credentials.json' # Salve o JSON que você me enviou como este arquivo


# --- Lógica de Screenshot ---

timestamp_atual = datetime.now().strftime("%H")

# 2. Defina o nome do arquivo do screenshot
nome_arquivo_screenshot = f"Report_{timestamp_atual}.png"
caminho_completo_screenshot = os.path.join(FolderShots, nome_arquivo_screenshot)
sucesso_screenshot = driver.save_screenshot(caminho_completo_screenshot)

if sucesso_screenshot:
    print(f"Screenshot salvo com sucesso em: {caminho_completo_screenshot}")
else:
    print(f"Falha ao salvar o screenshot em: {caminho_completo_screenshot}")
# ---------------------------------------


driver.quit()
print("Navegador fechado.")