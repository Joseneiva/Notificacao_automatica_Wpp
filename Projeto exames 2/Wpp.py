import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image, ImageTk
import time
import urllib.parse
import os

def formatar_data(data_raw):
    data_raw = ''.join(filter(str.isdigit, data_raw))
    if len(data_raw) == 8:
        return f"{data_raw[:2]}/{data_raw[2:4]}/{data_raw[4:]}"
    return data_raw

def formatar_hora(hora_raw):
    hora_raw = ''.join(filter(str.isdigit, hora_raw))
    if len(hora_raw) == 4:
        return f"{hora_raw[:2]}:{hora_raw[2:]}"
    return hora_raw

def enviar_mensagem():
    nome = entry_nome.get().strip().title()
    telefone = entry_telefone.get().strip()
    exame = entry_exame.get().strip().upper()
    data = formatar_data(entry_data.get().strip())
    hora = formatar_hora(entry_hora.get().strip())
    local = entry_local.get().strip().title()
    obs = entry_obs.get().strip().title()

    if not (nome and telefone and exame and data and hora and local):
        messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")
        return

    if not telefone.startswith("+"):
        telefone = "+55" + telefone

    mensagem = (
        f"Olá {nome}, tudo bem?\n\n"
        f"Seu exame de *{exame}* está agendado para o dia *{data}* às *{hora}*.\n"
        f"🏥 Local: {local}"
    )
    if obs:
        mensagem += f"\nℹ️ Observações: {obs}"
    mensagem += "\n\nEm caso de desistência, por favor, avisar com antecedência.\n\nEstamos à disposição!"

    mensagem_codificada = urllib.parse.quote(mensagem)
    url = f"https://web.whatsapp.com/send?phone={telefone}&text={mensagem_codificada}"

    chrome_options = Options()
    pasta_perfil = os.path.join(os.path.expanduser("~"), "whatsapp-session")
    os.makedirs(pasta_perfil, exist_ok=True)
    chrome_options.add_argument(f"--user-data-dir={pasta_perfil}")
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-software-rasterizer")

    service = Service(ChromeDriverManager().install())

    driver = None
    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(url)

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Enviar']"))
        )
        send_button = driver.find_element(By.XPATH, "//button[@aria-label='Enviar']")
        send_button.click()

        messagebox.showinfo("Sucesso", f"Mensagem enviada para {nome} ({telefone})")
    except Exception as e:
        messagebox.showerror("Erro no envio", f"Ocorreu um erro:\n{e}")
    finally:
        if driver:
            time.sleep(5)
            driver.quit()

# 🎨 Interface Tkinter com logo
janela = tk.Tk()
janela.title("Notificação Automática - WhatsApp")
janela.configure(bg="#E0F2F7")
largura_janela = 700
altura_janela = 800

# Pega a largura e altura da tela do usuário
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

# Calcula as coordenadas x e y para centralizar
pos_x = (largura_tela // 2) - (largura_janela // 2)
pos_y = (altura_tela // 2) - (altura_janela // 2)

# Aplica a geometria com posição
janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")


# Logo
try:
    caminho_logo = r"C:\Users\netoo\OneDrive\Imagens\Screenshots\logo.png"
    imagem_logo = Image.open(caminho_logo)
    imagem_logo = imagem_logo.resize((500, 90))
    logo_tk = ImageTk.PhotoImage(imagem_logo)
    logo_label = tk.Label(janela, image=logo_tk, bg="#E0F2F7")
    logo_label.image = logo_tk
    logo_label.pack(pady=(20, 15))
except Exception as e:
    print("Erro ao carregar a logo:", e)

# Campos
fonte_label = ("Segoe UI", 12, "bold")
fonte_input = ("Segoe UI", 12)

def campo_rotulado(label):
    container = tk.Frame(janela, bg="#E0F2F7")
    container.pack(pady=8)
    tk.Label(container, text=label, font=fonte_label, bg="#E0F2F7", anchor="w").pack(fill="x", padx=20)
    entrada = tk.Entry(container, width=40, font=fonte_input, relief="solid", borderwidth=1)
    entrada.pack(fill="x", padx=20)
    return entrada

entry_nome = campo_rotulado("👤 Nome do paciente:")
entry_telefone = campo_rotulado("📞 Telefone (somente números com DDD):")
entry_exame = campo_rotulado("🧪 Tipo de exame:")
entry_data = campo_rotulado("📅 Data do exame (ex: DD/MM/AAAA):")
entry_hora = campo_rotulado("⏰ Hora do exame (ex: HH:MM):")
entry_local = campo_rotulado("🏥 Local do exame:")
entry_obs = campo_rotulado("📝 Observações (opcional):")

btn_enviar = tk.Button(
    janela,
    text="📤 Enviar pelo WhatsApp",
    command=enviar_mensagem,
    bg="#4CAF50",
    fg="white",
    font=("Segoe UI", 14, "bold"),
    padx=20,
    pady=10,
    relief="raised",
    cursor="hand2"
)

btn_enviar.pack(pady=30, padx=30, fill="x")

janela.mainloop()
