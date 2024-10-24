from pyDatalog import pyDatalog


pyDatalog.create_terms('aluno, Nota, Nome, aprovado')

def adicionar_fato_aluno(nome, nota):
    +aluno(nome, nota)

def importar_dados_do_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as file:
        linhas = file.readlines()
        for linha in linhas:
        
            if 'aluno(' in linha:
                inicio = linha.find('("') + 2
                fim = linha.find('",')
                nome = linha[inicio:fim] 

                inicio_nota = linha.find(',', fim) + 1
                fim_nota = linha.find(').')
                nota = float(linha[inicio_nota:fim_nota])

                
                adicionar_fato_aluno(nome, nota)
                print(f"Fato adicionado: aluno({nome}, {nota})")  



aprovado(Nome) <= aluno(Nome, Nota) & (Nota >= 7)


importar_dados_do_arquivo('alunos.txt')


try:
    alunos_aprovados = aprovado(Nome)
   
    print("Alunos aprovados:")
    for resultado in alunos_aprovados:
        print(resultado[0])
except AttributeError as e:
    print("Erro: ", e)
