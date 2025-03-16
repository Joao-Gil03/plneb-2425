# TPC5

Este trabalho consistiu na implementação de uma aplicação Flask que permite a visualização de uma lista de conceitos médicos e a navegação para páginas individuais de cada conceito, onde são exibidas as suas descrições. A aplicação utiliza templates HTML para renderizar as páginas e rotas dinâmicas para acessar os conceitos específicos.

## Funcionalidades Implementadas

1. **Lista de Conceitos**:
   - Exibe uma lista de todos os conceitos médicos disponíveis.
   - Cada conceito é um link clicável que redireciona para a página específica do conceito.

2. **Página Individual de Conceitos**:
   - Exibe a designação e a descrição de um conceito específico.
   - A descrição é obtida dinamicamente a partir de um arquivo JSON.

3. **Rotas Dinâmicas**:
   - As rotas são configuradas para capturar a designação do conceito diretamente da URL, permitindo a exibição dinâmica do conteúdo.

## Estrutura do Projeto

- `app.py`: Arquivo principal da aplicação Flask.
- `conceitos.json`: Arquivo JSON contendo os conceitos e suas descrições.
- `templates/`: Pasta contendo os templates HTML.
  - `conceitos.html`: Template que exibe a lista de conceitos com links para as páginas individuais.
  - `um_conceito.html`: Template que exibe a designação e a descrição de um conceito específico.
