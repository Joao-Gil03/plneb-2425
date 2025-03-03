import re
file= open("aulas/aula_3/dicionario_medico.txt")

texto= file.read()

# [A-Z].*\n\n\f.+\.

#designão \f descrição
texto = re.sub(r"(\w+\s*\w*)\n\n\f(.+)",r"\1\n\2",texto)

#descrição \n descrição
texto = re.sub(r"([A-Z]?.*)\n\n(.*\.)",r"\1\n\2",texto)



texto = re.sub(r"\f","",texto)


texto= re.sub(r"\n\n",r"\n\n@",texto)

conceitos = re.split(r"\n\n@",texto)


def limpa_descricao(descricao):
    descricao = descricao.strip()
    descricao = re.sub(r'\n', ' ', descricao)
    return descricao

conceitos_list= []

for c in conceitos:
    if c != "":
        designacao,descricao = re.split(r"\n",c,maxsplit=1)
        descricao = limpa_descricao(descricao)
        conceitos_list.append((designacao,descricao))





def gerar_html(conceitos):
    html_header = """
        <!DOCTYPE html>
            <head>
            <meta charset="UTF-8"/>
            </head>
            <body> 
            <h3>Dicionário De Conceitos Médicos</h3>
            <p>Este dicionário foi desenvolvido para a aula de PLNEB 2024/2025</p>"""
        
    html_conceitos = ""
    for designacao, descricao in conceitos:
        html_conceitos += f"""
            <div>
            <p><b>{designacao}</b></p>
            <p>{descricao}  </p>  
            </div>
            <hr/>
        """
    
    html_footter = """
            </body>
        </html>
    """

    return html_header + html_conceitos + html_footter



html =gerar_html(conceitos_list)

f_out = open("dicionario_medico.html","w",encoding="utf-8")
f_out.write(html)
f_out.close()

file.close()