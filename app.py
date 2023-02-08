import pywhatkit
from datetime import datetime
import pyautogui
import time

msg_padrao = "esta é uma mensagem padrão"
contato = "+00000000000"

contato = pyautogui.prompt("Digite o numero ", "Numero da pessoa", contato)
#msg = pyautogui.prompt("Digite a mensagem", "mensagem", msg_padrao)

pywhatkit.sendwhatmsg(contato, msg_padrao, datetime.now().hour, datetime.now().minute + 1)
#time.sleep(10)
#pyautogui.hotkey("enter")
