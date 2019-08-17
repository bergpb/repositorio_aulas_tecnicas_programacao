from pessoa import Pessoa
from funcionario import Funcionario
from supervisor import Supervisor
from datetime import datetime as dt


data_nascimento = dt.strptime('2000-01-01', '%Y-%m-%d')
data_admissao =dt.strptime('2005-01-01', '%Y-%m-%d')

funcionario = Funcionario('Josh', '793.253.125-92', data_nascimento, data_admissao, 2000, 'Setor 1')

supervisor = Supervisor('Nicole', '589.365.182-21', data_nascimento, data_admissao, 2000, 'Setor 1', 500)

print('---Funcionario---')
print(funcionario)
print('Salário mensal: {}'.format(funcionario.calcula_salario_mensal()))

print('---Supervisora---')
print(supervisor)
print('Salário mensal: {}'.format(supervisor.calcula_salario_mensal()))