'''
Segundo a PEP8 o nome de uma classe deve começar com letra maiúscula
e as demais palavras devem ser íniciadas com a letra maiícula também
Ex: ExemploPessoa, AtualizarTela etc)

Ao definir um método ou função é importante ser tudo minúsculo e palavras separadas por underline
'''

class Pessoa:
    olhos = 2
    ''' atributo de classe, default, que será igual para todos os objetos. 
                 Declarando dessa maneira o python não precisa alocar varios espaços de 
                 memória de valores iguais para objetos diferentes. Dessa forma é possível acessar
                 o valor de olhos diretamente na classe e também nos objetos'''

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    @staticmethod #decorator
    def metodo_estatico(): #independe do objeto, pode ser acessado diretamente pela classe
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

    def cumprimentar(self):
        return f'Olá {id(self)}'

class Homem(Pessoa):
    pass


if __name__ == '__main__':
    leopoldo = Homem(nome='leopoldo')
    joao = Pessoa(nome='João')
    luciano = Pessoa(leopoldo, joao, nome='Liciano')
    print(leopoldo.cumprimentar())
    print(leopoldo.nome)
    print(leopoldo.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'
    luciano.olhos = 1
    leopoldo.olhos = 1
    del luciano.olhos
    del luciano.sobrenome
    print(luciano.__dict__) #exibe todos os atributos de instância e não os atributos de classe. Apenas quando houver alteração direta do atributo ele aparecerá aqui.
    print(leopoldo.__dict__)
    print(Pessoa.olhos)
    print(leopoldo.olhos)
    print(luciano.olhos)
    print(Pessoa.metodo_estatico(), leopoldo.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe(), leopoldo.nome_e_atributo_de_classe())
