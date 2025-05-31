from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from PIL import ImageGrab
import time
from datetime import datetime
import os
import sys

# ---------- CONFIGURAÇÕES ----------
url_planilha = "https://docs.google.com/spreadsheets/d/1CQ0LKwt6kAvAsK1-QSMK75XgZrjuqnYElTuWwrlb264/edit?gid=0"

# ---------- CONFIGURAR CHROME COM PERFIL ----------
#Modificar esse caminho dependendo do ambiente
caminho_user_data = r"C:\Users\F4k3r\AppData\Local\Google\Chrome\User Data\Profile 1"
nome_do_perfil = "Profile 1"

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument(f"--user-data-dir={caminho_user_data}")
chrome_options.add_argument(f"--profile-directory={nome_do_perfil}")

# ---------- INICIALIZA O NAVEGADOR ----------
try:
    print("[INFO] Iniciando Chrome com Selenium...")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
except Exception as e:
    print(f"[ERRO] Falha ao iniciar o navegador: {e}")
    sys.exit(1)

# ---------- ACESSA A PLANILHA ----------
print("[INFO] Abrindo planilha...")
driver.get(url_planilha)

# ---------- PAUSA EXTRA ----------
time.sleep(5)

# ---------- TIRA A CAPTURA DE TELA ----------
try:
    print("[INFO] Capturando screenshot...")
    x, y, largura, altura = 300, 200, 1920, 1080  # Ajuste conforme seu monitor
    bbox = (x, y, x + largura, y + altura)
    screenshot = ImageGrab.grab(bbox=bbox)
except Exception as e:
    print(f"[ERRO] Erro ao capturar a tela: {e}")
    driver.quit()
    sys.exit(1)

# ---------- SALVA IMAGEM ----------
pasta_destino = "PicturesAuto"
os.makedirs(pasta_destino, exist_ok=True)

hora_atual = datetime.now().strftime("%H")
nome_arquivo = f"Report das {hora_atual}.png"
caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)

try:
    screenshot.save(caminho_arquivo)
    print(f"[INFO] Screenshot salva em: {caminho_arquivo}")
except Exception as e:
    print(f"[ERRO] Erro ao salvar a imagem: {e}")

# ---------- FECHA O NAVEGADOR ----------
driver.quit()
print("[INFO] Processo finalizado com sucesso.")
