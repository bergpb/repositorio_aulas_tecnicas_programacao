from funcionario import Funcionario


class Supervisor(Funcionario):
    def __init__(self, nome, cpf, data_nascimento, data_admissao, salario, lotacao, comissao):
        super().__init__(nome, cpf, data_nascimento, data_admissao, salario, lotacao)
        self.comissao = comissao

    # sobrescrita do metodo calcula_salario_mensal da classe funcionario
    def calcula_salario_mensal(self):
        return super().calcula_salario_mensal() + self.comissao

    # representação da classe
    def __str__(self):
        return 'Nome: {}, CPF: {}, Salário: {}, Comissão: {}'.format(self.nome, self.cpf, self.salario, self.comissao)