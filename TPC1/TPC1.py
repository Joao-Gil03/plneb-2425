#1

s="ao_ao_ao"


def reverse(s):
    p=s[-1::-1]
    return p


#2

def count(s):
    m=s.lower()
    counter=0
    for l in m:
        if l =="a":
            counter+=1
    return counter

#3

def c_vowels(s):
    m=s.lower()
    counter=0
    for l in m:
        if l in ["a","e","i","o","u"]:
            counter +=1
    return counter


#4

def minuscula(s):
    return s.lower()


#5

def maiscula(s):
    return s.upper()


#6


def capicua(s):
    p=s[-1::-1]
    if p==s:
        print("A string é uma capicua")
    else:
        print("A string não é uma capicua")
        

        
        
#7

def balance(s1,s2):
    res=True
    for l1 in s1:
        if l1 not in s2: 
            res=False
    if res:
        print("As strings estão balanceadas")
    else:
        print("As strings não estão balanceadas")
                
    


#8

def ocorrencias(s1,s2):
    t = len(s1)
    count=0
    
    for i in range(0,len(s2)-t+1):
        if s1 ==s2[i:i+t]:
            count+=1
        
        
    return count
        
        

#9


def anagrama(s1,s2):
    res=True
    lista_2=list(s2)
    if len(s1) ==len(s2):
        for l1 in s1:
            if l1 not in lista_2:
                res=False
            else:
                lista_2.remove(l1)
                
                
    else:
        res =False
                
    return(res)


#10

from collections import defaultdict

def classes_anagrama(dic):
    classes = defaultdict(list)
    
    for palavra in dic:
        chave = "".join(sorted(palavra))  
        classes[chave].append(palavra)
    
    return dict(classes)


dic = ["amor", "roma", "carro", "roca", "maro", "arco"]

for chave, palavras in classes_anagrama(dic).items():
    print(f"Classe {chave}: {palavras}")
