import pyautogui
import time
import os
import subprocess

print('===== ROBÔ INICIADO =====')

# -----------------------------------
# CONFIGURAÇÕES
# -----------------------------------

PASTA_DESTINO = r'C:\Users\Profectum\Desktop\meu_robo'

ARQUIVO = 'demonstracao.txt'

CAMINHO_COMPLETO = os.path.join(
    PASTA_DESTINO,
    ARQUIVO
)

# -----------------------------------
# VALIDAR PASTA
# -----------------------------------

print('Verificando se a pasta existe...')

if os.path.exists(PASTA_DESTINO):

    print('Pasta encontrada.')

else:

    print('Pasta NÃO existe.')
    print('Criando nova pasta...')

    os.makedirs(PASTA_DESTINO)

    print('Pasta criada com sucesso.')

# -----------------------------------
# INÍCIO DA AUTOMAÇÃO
# -----------------------------------

print('Aguardando 5 segundos...')
time.sleep(5)

print('Procurando imagem na tela...')

icone = pyautogui.locateCenterOnScreen(
    'imagens/image.png',
    confidence=0.8
)

if icone is None:

    print('ERRO: imagem não encontrada.')
    raise Exception('Imagem não encontrada')

print(f'Imagem encontrada: {icone}')

# abre notepad
pyautogui.click(icone)

print('Notepad aberto.')

time.sleep(3)

#pyautogui.click()

texto = (
    'A ferramenta automation pro e excelente! '
    'Voce deveria adquiri-la'
)

print('Digitando texto...')

pyautogui.write(texto, interval=0.03)

print('Texto digitado.')

# -----------------------------------
# SALVAR ARQUIVO
# -----------------------------------

print('Executando CTRL + S...')

pyautogui.hotkey('ctrl', 's')

time.sleep(2)

print('Digitando caminho do arquivo...')

pyautogui.write(CAMINHO_COMPLETO)

time.sleep(1)

print('Salvando arquivo...')

pyautogui.press('enter')

time.sleep(2)

print('Arquivo salvo com sucesso.')

# -----------------------------------
# FECHAR NOTEPAD
# -----------------------------------

print('Fechando Notepad...')

subprocess.run(
    ['taskkill', '/F', '/IM', 'notepad.exe'],
    capture_output=True
)

print('Notepad fechado.')

print('===== ROBÔ FINALIZADO =====')