from pessoa import Pessoa
from datetime import datetime as dt


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, data_admissao, salario, lotacao):
        super().__init__(nome, cpf, data_nascimento)
        self.data_admissao = data_admissao
        self.salario = salario
        self.lotacao = lotacao

    def calcula_salario_mensal(self):
        data_hoje = dt.now()
        anos_trabalhados = int(abs((data_hoje - self.data_admissao).days / 365))
        salario_mensal = self.salario + (self.salario * anos_trabalhados) / 100
        return salario_mensal

    # representação da classe
    def __repr__(self):
        return 'Nome: {}, CPF: {}, Salário: {}'.format(self.nome, self.cpf, self.salario)