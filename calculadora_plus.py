import sys

# NOME
print("CALCULADORA+ 1.0V\n")


# CALCULADORA
class calculadora:
    # falsa ajuda
    def ajuda(self=""):
        print("Este programa vai realizar as operações aritméticas que você desejar com os valores fornecidos\n\n"
              "Possibilidades de argumentos:\n"
              "-h, --help : Vai exibir este banner de ajuda\n"
              "-v1, --valor1 : Primeiro valor\n"
              "-v2, --valor2 : Segundo valor\n\n"
              "Operações possíveis:\n"
              "| somar | subtrair | dividir | resto | multiplicar | elevar |")
        exit()

        # checagem parametros

    def checagem_argumentos(argumentos):
        # captando primeiro valor
        if "-v1" in argumentos or "--valor1" in argumentos:
            try:
                v1 = argumentos[argumentos.index("--valor1") + 1]
            except:
                v1 = argumentos[argumentos.index("-v1") + 1]
            finally:
                try:
                    valor1 = v1
                except:
                    print("ERROR[é necessário que o valor tenha algum valor quando mencionado]")
                    exit()
        else:
            valor1 = 0
        # fim da recepção do valor

        # captando segundo valor
        if "-v2" in argumentos or "--valor2" in argumentos:
            try:
                v2 = argumentos[argumentos.index("--valor2") + 1]
            except:
                v2 = argumentos[argumentos.index("-v2") + 1]
            finally:
                try:
                    valor2 = v2
                except:
                    print("ERROR[é necessário que o valor tenha algum valor quando mencionado]")
                    exit()
        else:
            valor2 = 0
        # fim da recepção do valor

        return {"valor1": valor1, "valor2": valor2}

    def soma(valor1, valor2):
        return int(valor1) + int(valor2)

    def subtracao(valor1, valor2):
        return int(valor1) - int(valor2)

    def multiplicar(valor1, valor2):
        return int(valor1) * int(valor2)

    def resto(valor1, valor2):
        try:
            return int(valor1) // int(valor2)
        except:
            return "Valor nulo/inexistente"

    def divisao(valor1, valor2):
        try:
            return int(valor1) / int(valor2)
        except:
            return "Valor nulo/inexistente"

    def elevar(valor1, valor2):
        return int(valor1) ** int(valor2)


class funcoes:
    def ajuda(self=""):
        print("Este programa vai te ajudar no processo de esconder arquivos dentro de outros(esteganografia)\n\n"
              "Possibilidades de argumentos:\n"
              "?h, ?help : Vai exibir este banner de ajuda\n"
              "-f, --file : Indicacao de qual o arquivo tera o segredo oculto ou que ja possui\n"
              "-i, --insercao : Arquivo que sera ocultado dentro de outro\n\n"
              "Modos de agir:\n"
              "inserir - Vai inserir o arquivo dentro de outro\n"
              "retirada - Comando para retirar o segredo\n")
        exit()

    def easter_egg(argumentos):
        try:
            teste = argumentos[2]
        except:
            print("Talvez você esteja se perguntado o porquê do nome deste programa ou qual sua funcionalidade.\n"
                  "Bem, não é complicado, a principal funcionalidade dele é o processo de esteganografia\n"
                  "porém, como se você veio atrás deste processo é porque procura privacidade e esconder algo,\n"
                  "por este motivo, criei a funcionalidade de uma calculadora para ser mais discreto.\n"
                  "Espero que lhe sirva\n\n\n"
                  "~Feito por: 5H4D0W")

    def checagem_argumentos(argumentos):
        calculo = True
        if "-f" in argumentos or "--file" in argumentos:
            try:
                f = argumentos[argumentos.index("--file") + 1]
            except:
                f = argumentos[argumentos.index("-f") + 1]
            finally:
                try:
                    file = f
                    calculo = False
                except:
                    print("ERROR[é necessário que o file tenha algum valor quando mencionado]")
                    exit()
        else:
            file = ""
        if "-i" in argumentos or "--inserction" in argumentos:
            try:
                i = argumentos[argumentos.index("--insercao") + 1]
            except:
                i = argumentos[argumentos.index("-i") + 1]
            finally:
                try:
                    insercao = i
                except:
                    print("ERROR[é necessário que o insercao tenha algum valor quando mencionado]")
                    exit()
        else:
            insercao = ""
        if "-c" in argumentos or "--crypt" in argumentos:
            try:
                k = argumentos[argumentos.index("--crypt") + 1]
            except:
                k = argumentos[argumentos.index("-c") + 1]
            finally:
                try:
                    key = k
                except:
                    print("ERROR[é necessário que o insercao tenha algum valor quando mencionado]")
                    exit()
        else:
            key = ""
        if "?h" in argumentos or "?help" in argumentos:
            funcoes.ajuda()
        return {"file": file, "insercao": insercao, "crypt": key, "calcular": calculo}


# SISTEMA DE AJUDA
argumentos = sys.argv
# ajuda falsa
if "-h" in argumentos or "--help" in argumentos:
    calculadora.ajuda()
    # ajuda esteganografia
if "?h" in argumentos or "?help" in argumentos:
    funcoes.ajuda()
    # easter egg
if argumentos[1] == "?":
    funcoes.easter_egg(argumentos)


# FIM SISTEMA AJUDA

# INSERINDO SEGREDO
def inserindo(file, insercao):
    print("Escondendo arquivo")
    # print(insercao[::-1][:3][::-1])
    try:
        with open(file, "ab") as f:
            with open(insercao, "rb") as i:
                f.write(i.read())
    except Exception as e:
        print(f"ERROR[{e}]")
    else:
        print("Esteganografia completa")


# FIM DA INSERÇÃO

# RETIRADA DO SEGREDO
def retirada(file, crypt_key):
    nome = "arquivo_retirado"
    try:
        with open(file, "rb") as f:
            content = f.read()
            # extensão do file
            if "jpg" in file or "jpeg" in file:
                extensao_file = "jpg"
            elif "png" in file:
                extensao_file = "png"
            if extensao_file == "jpg":
                offset = content.index(bytes.fromhex("FFD9"))
            elif extensao_file == "png":
                offset = content.index(bytes.fromhex("6082"))

                # capturando o conteúdo escondido
            print("Capturando o conteúdo escondido")
            f.seek(offset + 2)
            retorno = content[:offset + 2]
            # print(retorno)
            conteudo_img_new = f.read()
            # print(conteudo_img_new)
            extensao = conteudo_img_new[:10]

            # recebendo a extensao do escondido

            print("Recebendo a extensao do escondido")
            if b"JPG" in extensao or b"JFIF" in extensao:
                extensao = "jpg"
            elif b"PNG" in extensao:
                extensao = "png"
            elif b"PK" in extensao:
                extensao = "zip"
            else:
                extensao = "txt"
            nome = nome + '.' + str(extensao)
            if conteudo_img_new != b"":
                new_file = open(nome, "ab")
                new_file.write(conteudo_img_new)
                print("Recriando o arquivo")
            else:
                print(f"Não existe nenhum arquivo inserido em {file}")
                exit()

            # retirando o segredo do arquivo original
        with open(file, "wb") as f:
            f.write(retorno)
            print("Retirando o segredo do arquivo original")
        print("Retirada concluída com sucesso")
    except Exception as e:
        print(f"ERROR[{e}]")


# FIM DA RETIRADA

# CHECAGEM PARA ESTEGNOGRAFIA
if "inserir" in argumentos:
    resultados = funcoes.checagem_argumentos(argumentos)
    # print(resultados["file"], resultados["insercao"])
    if resultados["calcular"]:
        exit()
    else:
        inserindo(resultados["file"], resultados["insercao"])
elif "retirar" in argumentos:
    resultados = funcoes.checagem_argumentos(argumentos)
    # print(resultados["file"])
    if resultados["calcular"]:
        exit()
    else:
        retirada(resultados["file"], resultados["crypt"])
else:
    # CHECAGEM PARA CALCULADORA
    resultados = calculadora.checagem_argumentos(argumentos)
    valor1 = resultados["valor1"]
    valor2 = resultados["valor2"]
    print("Este é o resultado da(o) sua/seu: ", end="")
    if "somar" in argumentos:
        print("soma")
        print(calculadora.soma(valor1, valor2))
    elif "subtrair" in argumentos:
        print("subtração")
        print(calculadora.subtracao(valor1, valor2))
    elif "multiplicar" in argumentos:
        print("multiplicação")
        print(calculadora.multiplicar(valor1, valor2))
    elif "resto" in argumentos:
        print("resto")
        print(calculadora.resto(valor1, valor2))
    elif "dividir" in argumentos:
        print("divisão")
        print(calculadora.divisao(valor1, valor2))
    elif "elevar" in argumentos:
        print("exponenciação")
        print(calculadora.elevar(valor1, valor2))

# inserindo("dados_copy.png","testezip.zip")
# retirada("dados_copy.png")
