import pyautogui

pyautogui.PAUSE = 0.5

# 1) Entrar no sistema da empresa

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# 2) Fazer Login
# Para dar uma pausa maior somente nesse passo, pois internet pode estar lenta.
pyautogui.sleep(3)

pyautogui.click(x=340, y=413)

pyautogui.write("example@gmail.com")
pyautogui.press("tab")
pyautogui.write("qualquercoisaexemplo")
pyautogui.press("tab")
pyautogui.press("enter")

# 3) Importar a base de dados

import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)

# 4) Cadastrar um produto

# Clicar no primeiro campo

for linha in tabela.index:

    pyautogui.click(x=373, y=302)

    #pegar coluna na tabela
    codigo = tabela.loc[linha, "codigo"]

    #preencher com valor coletado e passar para o próximo
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #preencher os outros campos
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)


# 5) Repetir processo de cadastro até acabar