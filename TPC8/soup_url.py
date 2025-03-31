import requests
import json
from bs4 import BeautifulSoup


from bs4 import BeautifulSoup



from bs4 import BeautifulSoup

def extrair_informacoes(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    dados = {
        'causas': '',
        'sintomas': [],
        'tratamento': '',
        'artigos_relacionados': []
    }
    
    # Extrair "Causas"
    h2_causas = soup.find('h2', string='Causas')
    if h2_causas:
        proximo_elemento = h2_causas.find_next_sibling()
        texto_causas = []
        while proximo_elemento and proximo_elemento.name != 'h2':
            if proximo_elemento.name == 'p':
                texto_causas.append(proximo_elemento.get_text(strip=True))
            proximo_elemento = proximo_elemento.find_next_sibling()
        dados['causas'] = ' '.join(texto_causas)
    
    # Extrair "Sintomas"
    h2_sintomas = soup.find('h2', string='Sintomas')
    if h2_sintomas:
        ul_sintomas = h2_sintomas.find_next('ul')
        if ul_sintomas:
            sintomas = [li.get_text(strip=True) for li in ul_sintomas.find_all('li')]
            dados['sintomas'] = sintomas
    
    # Extrair "Tratamento"
    h2_tratamento = soup.find('h2', string='Tratamento')
    if h2_tratamento:
        proximo_elemento = h2_tratamento.find_next_sibling()
        texto_tratamento = []
        while proximo_elemento and proximo_elemento.name != 'h2':
            if proximo_elemento.name == 'p':
                texto_tratamento.append(proximo_elemento.get_text(strip=True))
            proximo_elemento = proximo_elemento.find_next_sibling()
        dados['tratamento'] = ' '.join(texto_tratamento)
    
    # Extrair "Artigos Relacionados"
    h2_artigos = soup.find('h2', string=lambda text: 'Artigos relacionados' in text if text else False)
    if h2_artigos:
        artigos = []
        for h3 in h2_artigos.find_all_next('h3'):
            link = h3.find('a')
            if link:
                artigos.append({
                    'titulo': link.get_text(strip=True),
                    'url': link.get('href')
                })
        dados['artigos_relacionados'] = artigos
    
    return dados





def get_doenca_info(url_href):    
    url_doenca="https://www.atlasdasaude.pt"+url_href
    response=requests.get(url_doenca)
    html_content = response.text
    html_content = response.text
    soup=BeautifulSoup(html_content,'html.parser')
    div_content=soup.find("div",class_="node-doencas")
    date=div_content.find("div",class_="field-name-post-date").div.div.text
    desc=div_content.find("div",class_="field-name-body").div.div.text
    info=div_content.find("div",class_="field-name-body").div.div
    note=div_content.find("div",class_="field-name-field-nota")
    if note:
        note=note.find("div",class_="field-item even").text
    else:
        note=""
    sections = extrair_informacoes(str(info))
    
    return {"data":date,"url":url_doenca,"nota":note,"descricao":desc.replace(" "," ")}|sections
    
    
    
    
def doencas_letra(letra):
    url="https://www.atlasdasaude.pt/doencasaaz/"+letra
    print(url)
    response=requests.get(url)

    html_content = response.text
    soup=BeautifulSoup(html_content,'html.parser')
    doenca = {}
    for elem in soup.find_all("div", class_="views-row"):
        
        ref =elem.div.h3.a['href']
        
        designacao = elem.div.h3.a.text.strip()
        print(designacao)
        doenca_info= get_doenca_info(ref)
        
        descricao = elem.find("div", class_="views-field-body").div
        
        if descricao.p:
            descricao= descricao.p.text.strip()
        elif descricao.div:
            descricao=descricao.div.text.strip()
        
        doenca[designacao]={"resumo":descricao.replace(" "," ")}|doenca_info
        
    return doenca


res={}
for a in range(ord("a"),ord("z")+1):
    letra= chr(a)
    res = res | doencas_letra(letra)

    
f_out=open("doenca_.json","w",encoding="utf-8")
json.dump(res,f_out,indent=4,ensure_ascii=False)
f_out.close

# TPC ir ao HTML do content ir separar por cada ponto cd




