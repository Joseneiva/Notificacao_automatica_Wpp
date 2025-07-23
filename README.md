# 📤 Sistema de Notificação Automática via WhatsApp

Um aplicativo em Python com interface gráfica (Tkinter) que automatiza o envio de mensagens de agendamento de exames médicos via WhatsApp Web, usando Selenium.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)

![Selenium](https://img.shields.io/badge/Selenium-Automation-brightgreen)

![Status](https://img.shields.io/badge/Status-100%25%20Funcional-green)

---

## 🖼️ Interface

## ✨ Funcionalidades

- Interface amigável com preenchimento de:
  - 👤 Nome do paciente
  - 📞 Telefone com DDD
  - 🧪 Tipo de exame
  - 📅 Data e ⏰ Hora do exame
  - 🏥 Local
  - 📝 Observações opcionais
- Formatação automática de data e hora
- Geração de mensagem personalizada para o paciente
- Envio automático via **WhatsApp Web** com abertura do navegador
- Janela centralizada na tela e suporte a imagem de logotipo

---

## 📦 Tecnologias

- `Python 3.10+`
- `Tkinter` – Interface gráfica
- `Selenium` – Automação do navegador
- `WebDriver Manager` – Gerenciador automático do ChromeDriver
- `Pillow` – Para exibir a imagem (logo)

---

## ⚙️ Instalação

### 1. Clone este repositório

```bash
git clone https://github.com/Joseneiva/Notificacao_automatica_Wpp.git
cd Notificacao_automatica_Wpp
```
### 2. Crie um ambiente virtual (opcional)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

#### 📄 requirements.txt

```txt
selenium
webdriver-manager
pillow
```