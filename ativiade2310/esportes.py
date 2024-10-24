from pyDatalog import pyDatalog


pyDatalog.create_terms('gosta_de, Pessoa1, Pessoa2, Esporte, compartilham_esporte')


def adicionar_fato_gosta_de(pessoa, esporte):

    +gosta_de(pessoa, esporte)


def importar_dados_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        linhas = file.readlines()
        for linha in linhas:
         
            if 'gosta_de(' in linha:
                inicio_pessoa = linha.find('("') + 2
                fim_pessoa = linha.find('",')
                pessoa = linha[inicio_pessoa:fim_pessoa] 

                inicio_esporte = linha.find('",', fim_pessoa) + 3
                fim_esporte = linha.find('").')
                esporte = linha[inicio_esporte:fim_esporte] 


                adicionar_fato_gosta_de(pessoa, esporte)
                print(f"Fato adicionado: gosta_de({pessoa}, {esporte})") 


compartilham_esporte(Pessoa1, Pessoa2, Esporte) <= (gosta_de(Pessoa1, Esporte)) & (gosta_de(Pessoa2, Esporte)) & (Pessoa1 != Pessoa2)


importar_dados_do_arquivo('esportes.txt')


pares_interessados = compartilham_esporte(Pessoa1, Pessoa2, Esporte)


print("Pares de pessoas que compartilham o mesmo interesse esportivo:")
for resultado in pares_interessados:
    print(f"{resultado[0]} e {resultado[1]} gostam de {resultado[2]}")
