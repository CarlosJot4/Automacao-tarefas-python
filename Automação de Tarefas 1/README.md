# Automação de Cadastro de Produtos

Este projeto contém um script simples em Python que automatiza o processo de login em um sistema web e o cadastro de produtos a partir de um arquivo CSV. É um exemplo prático para aprender automação de interface com a biblioteca `pyautogui` e manipulação de dados com `pandas`.

> Aviso: este script controla o mouse e o teclado do seu computador. Use com cuidado e preferencialmente em um ambiente de testes. Não execute em ambientes de produção sem antes adaptar e testar cuidadosamente.

## Estrutura do repositório

- `automacao.py` — Script principal que abre o navegador, faz login e cadastra produtos do CSV.
- `auxiliar.py` — Script auxiliar que espera alguns segundos e imprime a posição atual do cursor (útil para descobrir coordenadas de clique).
- `produtos.csv` — Arquivo CSV (minha base de dados) com os dados dos produtos a serem cadastrados (colunas esperadas: `codigo`, `marca`, `tipo`, `categoria`, `preco_unitario`, `custo`, `obs`).

## Objetivo

Demonstrar como automatizar interações básicas de interface (clicar, digitar, tab, enter) para automatizar cadastros repetitivos. Ideal para aprendizado e prototipagem de automações simples.

## Pré-requisitos

- Python 3.8+ (teste com Python 3.12 no ambiente de desenvolvimento deste projeto).
- Bibliotecas Python:
  - `pyautogui` — para controlar mouse/teclado.
  - `pandas` — para leitura e manipulação de CSV.

Recomenda-se criar um ambiente virtual antes de instalar dependências:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

Para instalar dependências:

```powershell
pip install pyautogui pandas
```

Nota: em alguns sistemas, `pyautogui` pode exigir bibliotecas adicionais (por exemplo Pillow) — o pip resolverá dependências automaticamente.

## Uso

1. Ajuste as coordenadas dentro de `automacao.py` para o seu monitor e resolução. Use o `auxiliar.py` para descobrir coordenadas: execute-o, posicione o cursor no elemento desejado e copie as coordenadas mostradas.

```powershell
python auxiliar.py
```

2. Atualize credenciais em `automacao.py` (substitua `seu_usuario` e `sua_senha`) ou, preferivelmente, implemente variáveis de ambiente para não deixar credenciais no código.

3. Garanta que `produtos.csv` esteja no mesmo diretório e com as colunas esperadas.

4. Execute o script com cuidado. Durante a execução o script controlará o mouse/teclado — não toque no mouse/teclado até que a execução termine.

```powershell
python automacao.py
```

## Arquivo CSV esperado

O `produtos.csv` deve ter pelo menos as colunas:

- `codigo`
- `marca`
- `tipo`
- `categoria`
- `preco_unitario`
- `custo`
- `obs` (opcional)

Exemplo de linhas CSV:

```
001,MarcaX,TipoA,Categoria1,10.50,5.00,Observação
002,MarcaY,TipoB,Categoria2,20.00,12.00,
```

## Segurança e boas práticas

- Não deixe credenciais (usuário/senha) salvas em texto no repositório.
- Use variáveis de ambiente ou um arquivo de configuração fora do repositório para armazenar credenciais de forma segura.
- Adicione delays (time.sleep) adequados entre ações para permitir carregamento das páginas.
- Teste em um ambiente controlado antes de usar em produção.

## Melhorias sugeridas

- Substituir coordenadas fixas por identificação de elementos (por exemplo, com OCR ou imagens via `pyautogui.locateOnScreen`) para maior robustez.
- Usar `pandas.isna()` ao invés de comparar com a string `'nan'` para detectar valores ausentes no CSV.
- Implementar um modo `dry-run` que apenas imprime as ações ao invés de executá-las.
- Armazenar credenciais em variáveis de ambiente ou integrar com um cofre de segredos.
- Adicionar logging e tratamento de exceções para melhorar diagnósticos.

## Licença

Use conforme desejar. Este é um exemplo educacional; não há garantias.

---

