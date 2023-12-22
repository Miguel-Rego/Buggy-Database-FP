def corrigir_palavra(palavrasurto):
    """corrigir palavra: cad. carateres -> cad. carateres

    Esta função recebe uma cadeia de carateres que representa uma palavra e
    devolve a cadeia de carateres que corresponde à aplicação da sequência
    de reduçõoes conforme descrito para obter a palavra corrigida"""

    tampalavra = len(palavrasurto)
    for i in range(1, tampalavra):  #Percorre a string inteira
        code1 = ord(palavrasurto[i - 1])  # Uso a lista ASCII para estabelecer uma correspondência entre letras minúsculas e maiúsculas
        code2 = ord(palavrasurto[i])
        if code1 == (code2 + 32) or code1 == (code2 - 32):  #Na lista ASCII, a constante que difere entre minúsculas e maiúsculas é 32
            return corrigir_palavra(palavrasurto[0:i - 1] + palavrasurto[i + 1:tampalavra])  #Divido a string para excluir as letras necessárias, e uso a recursividade das funções
    return palavrasurto


def eh_anagrama(x, n):
    """eh anagrama: cad. carateres e cad. carateres -> booleano
        esta função verifica se x e n são anagramas"""

    x = str.lower(x)
    n = str.lower(n)  #Ponho ambas as strings em minúsculas para ignorar as diferenças
    if sorted(x) == sorted(n):  #Ordeno-as igualmente para saber se são anagramas
        return True
    else:
        return False


def corrigir_doc(c):
    """corrigir doc: cad. carateres -> cad. carateres
       Esta função corrige, caso o argumento seja válido,
       os surtos de letras e os anagramas."""

    if type(c) == str:
        word_list = c.split()  #Compartimentalizar as palavras
        number_of_words = len(word_list)  #Contar as palavras
        if len(c) > 0 and c.count(" ") < number_of_words and all(x.isalpha() or x.isspace() for x in c):
            d = corrigir_palavra(c)  #Tirar os surtos de letras
            e = d.split()
            for word_1 in e:
                for word_2 in e:
                    if word_1 != word_2 and (sorted(word_1) == sorted(word_2)):  #Verificar se há anagramas
                        e.remove(word_2)  #Retirar os anagramas
            return " ".join(e)  #Juntar as palavras com espaços

        else:
            raise ValueError("corrigir_doc: argumento invalido")
    else:
        raise ValueError("corrigir_doc: argumento invalido")


def obter_posicao(cad_carateres, inteiro):
    """obter posicao: cad. carateres x inteiro -> inteiro
    Esta função recebe um movimento e um inteiro e devolve o inteiro
    após o movimento no painel de dígitos"""

    if cad_carateres == "C" and (inteiro != 1 and inteiro != 2 and inteiro != 3):  #Abro exceções para movimentos que não podem acontecer
        inteiro -= 3
    elif cad_carateres == "B" and (inteiro != 7 and inteiro != 8 and inteiro != 9):
        inteiro += 3
    elif cad_carateres == "D" and (inteiro != 3 and inteiro != 6 and inteiro != 9):
        inteiro += 1
    elif cad_carateres == "E" and (inteiro != 1 and inteiro != 4 and inteiro != 7):
        inteiro -= 1
    return inteiro


def split(word):
    """Função adicional para dividir os movimentos para a função obter_digito"""
    return [char for char in word]


def obter_digito(cad_carateres, inteiro):
    """obter digito: cad. carateres x inteiro -> inteiro
    Recebe uma sequência de movimentos e o inteiro inicial e devolve o inteiro
    resultante da sequência de movimentos"""

    for i in split(cad_carateres):  #Dividir os movimentos
        inteiro = obter_posicao(i, inteiro)  #Itero pelo loop para devolver o inteiro depois dos movimentos
    return inteiro


def check_pin(pin1):
    """Função adicional que retorna um booleano se a cadeia
    de carateres não for válida."""

    t4 = True
    for el in pin1:
        if len(el) < 1: #O comprimento não pode não ter carateres
            t4 = False
            return t4
        if type(el) != str:  #Tem de ser uma string
            t4 = False
            return t4
        for i in el:
            if not i in "CBED": #Verifica se contêm só estas letras
                t4 = False
                break

    return t4


def obter_pin(tuplo):
    """obter pin: tuplo -> tuplo
    Recebe sequências de movimentos que inicialmente começam no 5,
    e retornam o pin correspondente a essas sequências"""

    t2 = ()
    inteiro = 5
    if type(tuplo) == tuple and 4 <= len(tuplo) <= 10 and check_pin(tuplo):  #Verificar type e comprimento do tuplo
        for f in tuplo:
            inteiro = obter_digito(f, inteiro)
            t2 = t2 + (inteiro, )  #Recursividade para adicionar todos os números da sequência
        return t2
    else:
        raise ValueError("obter_pin: argumento invalido")


def has_numbers(input_string):
    """Função adicional para ver se uma string tem números."""

    return any(char.isdigit() for char in input_string)


def eh_entrada(arg):
    """eh entrada: universal -> booleano
    Função recebe um argumento de qualquer tipo e retorna True se for uma entrada válida da BDB,
    apesar de poder ser corrupta"""

    if type(arg) == tuple and len(arg) == 3:
        palavras = arg[0].split("-")
        for i in palavras:
            if len(i) < 1:  #Comprimento da string tem de ser maior do que 1
                return False
            for let in range(len(i)):
                if not i[let].isalpha():  #Verificar se a string só tem letras
                    return False
                if i[let].isupper():  #Verificar se a string tem letras maíusculas
                    return False
        checksum = arg[1]
        if type(arg[1]) == str and not has_numbers(arg[1]) and len(checksum) == 7 and checksum[1:6].lower() == checksum[1:6] and arg[1][0] == "[" and arg[1][6] == "]":
            if type(arg[2]) == tuple and len(arg[2]) >= 2:
                for p in arg[2]:
                    if type(p) != int:  #p no checksum tem de ser um número inteiro
                        return False
                    if p <= 0:  #Só podem ser números positivos
                        return False
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def listtostring(s):
    """Função adicional para tornar uma lista numa string"""
    # String vazia
    str1 = ""

    # Itero na lista
    for ele in s:
        str1 += ele

        # retorno na string
    return str1


def validar_cifra(cif, seq_cont):
    """validar cifra: cad. carateres x cad. carateres -> booleano
    Recebe a cifra e a sequência de controlo e retorna um booleano
    conforme se a cifra e a sequência forem coerentes."""

    seq_cont = seq_cont[1:-1]  #Elimino os [] da sequência de controlo
    count = {}
    for s in cif:
        if s != "-":
            if s in count:
                count[s] += 1
            else:
                count[s] = 1
    max_values = [v[0] for v in sorted(count.items(), key=lambda kv: (-kv[1], kv[0]))][:5]  #Ordena as 5 letras por uso e, caso empate, por ordem alfabética
    if listtostring(max_values) == seq_cont:  #Se esta sequência que fizemos for igual à sequência de controlo, é True
        return True
    else:
        return False


def filtrar_bdb(lista2):
    """filtrar bdb: lista -> lista
    Recebe uma lista de entradas da BDB e retorna as que apesar de serem entradas válidas,
    não são coerentes, conforme a função validar_cifra"""

    if type(lista2) == list and len(lista2) != 0:
        lista3 = []
        for i in lista2:
            if eh_entrada(i):  #Se for uma entrada válida
                if not validar_cifra(i[0], i[1]):  #Se for uma entrada não coerente # Acrescentei um "not" (tavas a dar aslistas boas e nao as erradas como o enunciado pede)
                    lista3.append(i)  #Adiciona à lista vazia
            else:
                raise ValueError("filtrar_bdb: argumento invalido")
        return lista3
    else:
        raise ValueError("filtrar_bdb: argumento invalido")


def obter_num_seguranca(tuplo3):
    """obter num seguranca: tuplo -> inteiro
    Recebe números e retorna a menor diferença entre os números"""

    min_absolute_difference = float("inf")
    sorted_tuplo_3 = sorted(tuplo3)  # Números por ordem

    for index in range(0, len(sorted_tuplo_3) - 1):
        small_num = sorted_tuplo_3[index]
        large_num = sorted_tuplo_3[index + 1]
        absolute_difference = abs(large_num - small_num)  # Módulo da diferença entre os números seguidos
        if absolute_difference <= min_absolute_difference:
            min_absolute_difference = absolute_difference

    for index in range(0, len(sorted_tuplo_3) - 1):
        small_num = sorted_tuplo_3[index]
        large_num = sorted_tuplo_3[index + 1]
        absolute_difference = abs(large_num - small_num)
        if absolute_difference == min_absolute_difference:  #Quando a diferença absoluta for igual à mínima, retorna a diferença.
            return absolute_difference


def decifrar_texto(cad_chr2, seq_inteiro):
    """decifrar texto: cad. carateres x inteiro -> cad. carateres
    Recebe uma cifra e o número de segurança e devolve o texto depois de corrigido"""

    cad_carateres = ""
    chr_frente = seq_inteiro % 26  #Resto da divisão do número de segurança pelo número de letras no alfabeto para saber quantas posições ir para a frente.
    for i in range(len(cad_chr2)):
        if cad_chr2[i] == "-":
            cad_carateres += " "  #Se há um traço, é substituído por um espaço.
        else:
            if i % 2 == 0:  #Se for par
                chr_frente2 = ord(cad_chr2[i]) + chr_frente + 1
                if chr_frente2 > 122:
                    chr_frente2 -= 26  #Caso ultrapasse na lista ASCII o índice do Z, volta ao ínicio para o A
                cad_carateres += chr(chr_frente2)
            else:  #Se for ímpar
                chr_frente2 = ord(cad_chr2[i]) + chr_frente - 1
                if chr_frente2 > 122:
                    chr_frente2 -= 26
                cad_carateres += chr(chr_frente2)
    return cad_carateres


def decifrar_bdb(list4):
    """decifrar_bdb: lista -> lista
    Recebe uma lista de entradas e devolve os textos decifrados na mesma ordem,
    caso as entradas sejam válidas."""

    list5 = []
    if type(list4) == list and len(list4) >= 1:
        for i in list4:
            if eh_entrada(i):  #Verificar se são válidas as entradas
                num_i = obter_num_seguranca(i[2])
                txt_decifrado = decifrar_texto(i[0], num_i)
                list5.append(txt_decifrado)  #Adicionar os textos à lista vazia
            else:
                raise ValueError("decifrar_bdb: argumento invalido")
        return list5
    else:
        raise ValueError("decifrar_bdb: argumento invalido")


def eh_utilizador(arg2):
    """eh utilizador: universal -> booleano
    Recebe um argumento e devolve só se verificar
    todas as condições para que seja uma entrada"""

    if type(arg2) == dict:
        if len(arg2) == 3:
            if "name" in arg2.keys() and "pass" in arg2.keys() and "rule" in arg2.keys():  #Verificar se há todas as entradas
                if type(arg2["name"]) == str and type(arg2["pass"]) == str and type(arg2["rule"]) == dict:
                    if len(arg2["name"]) > 0 and len(arg2["pass"]) > 0:
                        if "char" in arg2["rule"].keys() and "vals" in arg2["rule"].keys():
                            if type(arg2["rule"]["char"]) == str and type(arg2["rule"]["vals"]) == tuple:
                                if len(arg2["rule"]["char"]) == 1 and len(arg2["rule"]["vals"]) == 2:
                                    if arg2["rule"]["char"].islower() and type(arg2["rule"]["vals"][0]) == int and type(arg2["rule"]["vals"][1]) == int:
                                        if arg2["rule"]["vals"][0] > 0 and arg2["rule"]["vals"][1] > 0:  #Números do vals têm de ser > 0
                                            if arg2["rule"]["vals"][0] <= arg2["rule"]["vals"][1]:  #Segundo vals tem de ser > ou igual que o primeiro
                                                return True
    return False


def eh_senha_valida(chr4, dic):
    """eh_senha_valida: cad. carateres Ö dicionário -> booleano
    Recebe uma senha e um dicionário e verifica se cumpre as regras
    de definição"""

    if type(dic) == dict and type(chr4) == str:
        v = 0
        cont = 0
        for ch in chr4:
            if ch in 'aeiou':  # conta as vogais, pois têm de pelo menos haver 3
                v += 1
            if ch == dic["char"]:  #conta os carateres da letra no parâmetro "char"
                cont += 1

        if v >= 3 and dic["vals"][0] <= cont <= dic["vals"][1]:
            for i in range(len(chr4) - 1):
                if chr4[i] == chr4[i + 1]:
                    return True
    return False


def filtrar_senhas(list4):
    """filtrar senhas: lista -> lista
    Recebe uma lista contendo dicionários correpsondentes ás entradas da BDB
    e retorna os nomes dos utilizadores, caso as entradas sejam válidas"""

    if not isinstance(list4, list):  #Tem de ser uma lista
        raise ValueError("filtrar_senhas: argumento invalido")
    if len(list4) == 0:  #Tem de ter um comprimento > 0
        raise ValueError("filtrar_senhas: argumento invalido")
    for d in list4:  #Todas as iterações do for têm de ser dicionários e ter str e um tuplo nos parâmetros descritos
        if not eh_utilizador(d):
            raise ValueError("filtrar_senhas: argumento invalido")
    list5 = []
    for l in list4:
        if eh_senha_valida(l["pass"], l["rule"]) == False:
            list5.append(l["name"])
    return sorted(list5)