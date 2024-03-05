# Passo a passo
# Passo 1: Entrar no sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
# passo 2: Fazer login
# passo 3: Importar a base de dados
# passo 4: Cadastrar o produto
# passo 5: repetir o processo de cadastro até terminar
#site para teste https://dlp.hashtagtreinamentos.com/python/intensivao/login

#pyautogui.click - clicar
#pyautogui.write - escrever
#pyautogui.press - pressionar uma tecla py

import pyautogui
import time
import pandas

pyautogui.PAUSE = 1

#abrindo o navegador 
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)

#acessando o sistema 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(2)

#fazendo login
pyautogui.click(x=386, y=391) 
pyautogui.write("gabriel.uchoa92@gmail.com")
pyautogui.click(x=388, y=489)
pyautogui.write("gami0616")
pyautogui.click(x=634, y=551)
time.sleep(1)

#importar o banco de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    #cadastrar produto
    pyautogui.click(x=419, y=268)
    #codigo do produto
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    #preço
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    #curso
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
        pyautogui.press("tab")

    #enviar 
    pyautogui.press("enter")
    time.sleep(1)  
    pyautogui.scroll(5000)