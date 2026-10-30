import json 

#3----------------------

def gravar_linhas(caminho,linhas):
    with open(caminho, "a", encoding="UTF-8") as f:
        f.writelines(f"{linha} \n" for linha in linhas )

#4------------------------------


def ler_config(caminho):
    with open(caminho, "r", encoding="UTF-8") as f:
        linhas = f.readlines()

        for linha in linhas:
            if not linha.startswith("#") and " = " in linha:
                conf  = linha.split(" = ")
                chave = conf[0].strip()
                valor = conf[1].strip.replace('\n',"")
                resultado = [chave] = valor

    with open("config.json", "w", encoding="UTF-8") as f:
        json.dump(resultado, f, indent=4)

#5-----------------------------

def normalizar(origem,destino):
   with open(origem, "r", encoding="utf-8") as f:
       linhas = f.readlines()

    resultado = []
    n = 0
    for linha in linhas:
       novalinha = linha.strip()

       if novalinha != "":
           n += 1
           resultado.append(f"{str(n).zfill(2)} {novalinha}\n")

    with open(origem, "w", encoding="utf-8") as f:
       f.writelines(resultado)

    return n 

#9---------------------------

def import_inscricoes(caminho):
    with open(caminho, "r", encoding="utf-8") as f:
        linhas= f.readlines()

    validos = []
    problematicos = []
    n = 0

    for linha in linhas:
        if linha.strip() != "":
            inscricao = linha.split(" ; ")

            try:
                validos.append(
                    {}"nome" = inscricao[0]
                    'MATRICULA' = inscricao[1]
                    "minutos" = inscricao[2]
                )}
                

        