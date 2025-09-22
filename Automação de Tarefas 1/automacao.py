# Este script automatiza o processo de login em um sistema web e o cadastro de produtos a 
# partir de um arquivo CSV.

import pyautogui
import time

# Passo 1: entrar no sistema da empresa
# A seguir, usamos o atalho do Windows para abrir o menu iniciar (tecla Win),
# escrever o nome do navegador ("brave") e pressionar Enter para executá-lo.
pyautogui.press('win')  # pressiona a tecla Windows para abrir o menu iniciar
pyautogui.write('brave')  # digita o nome do navegador que será aberto
pyautogui.press('enter')  # pressiona Enter para abrir o navegador digitado

time.sleep(2)  # esperar 2 segundos para o navegador iniciar
# Após o navegador abrir, digitamos a URL do sistema e pressionamos Enter para navegar até ela
# URL demosntrativa usada na aula
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')  # escreve a URL na barra de endereços
pyautogui.press('enter')   # pressiona Enter para carregar a página

time.sleep(5)  # esperar 5 segundos para a página web carregar completamente

# Passo 2: fazer login
# Clica nas coordenadas onde o campo de usuário aparece na resolução usada
pyautogui.click(x=772, y=401)  # posiciona o cursor e clica no campo de usuário (resolução 1360x768)
# Digita o nome de usuário no campo selecionado
pyautogui.write('seu_usuario')  # substitua por seu usuário real se for usar automaticamente
# Pressiona tab para ir para o próximo campo (senha)
pyautogui.press('tab')  # envia tecla Tab para mover o foco
# Digita a senha no campo de senha
pyautogui.write('sua_senha')  # substitua por sua senha real se for usar automaticamente
# Pressiona Tab para ir ao botão de login ou próximo elemento
pyautogui.press('tab')  # envia tecla Tab novamente
# Pressiona Enter para submeter o formulário de login
pyautogui.press('enter')  # submete o formulário (pressiona Enter)

time.sleep(3)  # esperar 3 segundos para que o sistema processe o login e carregue a próxima página

# Passo 3: importar a base de dados
import pandas  # importa a biblioteca pandas para manipulação de dados (CSV)
# Lê o arquivo 'produtos.csv' e armazena em um DataFrame chamado tabela
tabela = pandas.read_csv('produtos.csv')  # lê a base de dados de produtos a partir do arquivo CSV


# Passo 4: cadastrar todos os produtos (itera sobre cada linha da tabela)
for linha in tabela.index:  # percorre todos os índices (linhas) do DataFrame

    # Clica no botão/área de cadastro do primeiro item para iniciar um novo cadastro
    pyautogui.click(x=853, y=282)  # clica na posição onde começa o formulário (resolução 1360x768)

    # Recupera o código do produto na linha atual e garante que seja string
    codigo = str(tabela.loc[linha, 'codigo'])  # obtém o valor da coluna 'codigo' e converte para string
    pyautogui.write(codigo)  # escreve o código no campo ativo
    pyautogui.press('tab')  # avança para o próximo campo

    # Recupera a marca do produto e insere no formulário
    marca = str(tabela.loc[linha, 'marca'])  # obtém a marca como string
    pyautogui.write(marca)  # escreve a marca
    pyautogui.press('tab')  # avança para o próximo campo

    # Recupera o tipo do produto e insere
    tipo = str(tabela.loc[linha, 'tipo'])   # obtém o tipo como string
    pyautogui.write(tipo)  # escreve o tipo
    pyautogui.press('tab')  # avança para o próximo campo

    # Recupera a categoria do produto e insere
    categoria = str(tabela.loc[linha, 'categoria'])  # obtém a categoria como string
    pyautogui.write(categoria)  # escreve a categoria
    pyautogui.press('tab')  # avança para o próximo campo

    # Recupera o preço unitário do produto e insere
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])  # obtém preço unitário como string
    pyautogui.write(preco_unitario)  # escreve o preço unitário
    pyautogui.press('tab')  # avança para o próximo campo

    # Recupera o custo do produto e insere
    custo = str(tabela.loc[linha, 'custo'])  # obtém custo como string
    pyautogui.write(custo)  # escreve o custo
    pyautogui.press('tab')  # avança para o próximo campo

    # Recupera observações e escreve apenas se não estiver vazia (tratamento robusto)
    # Mantemos o valor original (pode ser um float NaN) para usar pandas.isna()
    obs_val = tabela.loc[linha, 'obs']  # valor original da coluna 'obs' (pode ser NaN)
    # Verifica corretamente se o valor é ausente usando pandas.isna
    if not pandas.isna(obs_val):
        # Converte para string somente quando houver um valor válido e escreve no campo
        pyautogui.write(str(obs_val))  # escreve a observação no campo correspondente

    pyautogui.press('tab')  # avança para o botão/enviar do formulário

    pyautogui.press('enter')    # pressiona Enter para submeter o cadastro do produto
    pyautogui.scroll(10000)  # rola a página para cima (valor grande para garantir posição)

    time.sleep(1)  # espera 1 segundo para o sistema processar o cadastro antes de seguir para o próximo

