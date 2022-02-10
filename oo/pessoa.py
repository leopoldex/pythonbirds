'''
Segundo a PEP8 o nome de uma classe deve começar com letra maiúscula
e as demais palavras devem ser íniciadas com a letra maiícula também
Ex: ExemploPessoa, AtualizarTela etc)

Ao definir um método ou função é importante ser tudo minúsculo e palavras separadas por underline
'''

class Pessoa:
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
