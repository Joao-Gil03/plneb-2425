# Dicionário de Conceitos Médicos

Este projeto processa um ficheiro de texto contendo designações e definição e gera uma página HTML estruturada com essas informações.


## Funcionalidade
O script:
1. Lê o ficheiro `dicionario_medico.txt`.
2. Processa o texto para remover caracteres desnecessários e formatar corretamente os conceitos.
3. Extrai os termos e as respetivas descrições.
4. Gera uma página HTML contendo os conceitos formatados.
5. Guarda o resultado no ficheiro `dicionario_medico.html`.

## Explicação das Expressões Regulares
O script utiliza expressões regulares (`re.sub` e `re.split`) para processar o texto:

1. **`re.sub(r"(\w+\s*\w*)\n\n\f(.+)", r"\1\n\2", texto)`**
   - Captura um termo médico seguido por uma quebra de linha dupla (`\n\n`) e um `\f` (indicando uma nova página).
   - Substitui essa sequência por apenas uma quebra de linha simples, garantindo que a designação e a descrição fiquem na mesma estrutura.

2. **`re.sub(r"([A-Z]?.*)\n\n(.*\.)", r"\1\n\2", texto)`**
   - Captura descrições que possuem uma quebra de linha dupla no meio.
   - Substitui por uma quebra de linha simples, garantindo que as descrições permaneçam completas.

3. No entanto existe um caso único que sobra e é preciso retirar manualmente na palavra "sulco" em que existe um \n\n no meio do código e é preciso retirar manualmente.

4. **`re.sub(r"\f", "", texto)`**
   - Remove caracteres `\f` (form feed) que indicam mudanças de página, deixando o texto limpo.

5. **`re.sub(r"\n\n", r"\n\n@", texto)`**
   - Adiciona um `@` antes das quebras de linha duplas para facilitar a separação dos conceitos no passo seguinte.

6. **`re.split(r"\n\n@", texto)`**
   - Divide o texto em blocos de conceitos com base nas quebras de linha duplas marcadas anteriormente.

7. **`re.sub(r'\n', ' ', descricao)`** (na função `limpa_descricao`)
   - Substitui todas as quebras de linha dentro da descrição por espaços, garantindo que o texto fique fluido.




## Estrutura do HTML Gerado
- Um cabeçalho com o título "Dicionário De Conceitos Médicos".
- Uma breve introdução sobre o dicionário.
- Uma lista de conceitos, cada um com:
  - Uma designação (termo médico em negrito).
  - A sua descrição.
  - Uma linha de separação entre conceitos.


