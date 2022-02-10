'''
Segundo a PEP8 o nome de uma classe deve começar com letra maiúscula
e as demais palavras devem ser íniciadas com a letra maiícula também
Ex: ExemploPessoa, AtualizarTela etc)

Ao definir um método ou função é importante ser tudo minúsculo e palavras separadas por underline
'''

class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    leopoldo = Pessoa(nome='leopoldo')
    joao = Pessoa(nome='João')

    luciano = Pessoa(leopoldo, joao, nome='Liciano')
    print(leopoldo.cumprimentar())
    print(leopoldo.nome)
    print(leopoldo.idade)
    for filho in luciano.filhos:
        print(filho.nome)
