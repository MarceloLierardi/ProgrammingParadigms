from abc import ABC, abstractmethod


class CalculoSalarioStrategy(ABC):
	@abstractmethod
	def calcular(self):
		pass


class SalarioCLT(CalculoSalarioStrategy):
	def __init__(self, salario_fixo):
		self.salario_fixo = salario_fixo

	def calcular(self):
		return self.salario_fixo


class SalarioFreelancer(CalculoSalarioStrategy):
	def __init__(self, valor_hora, horas_trabalhadas):
		self.valor_hora = valor_hora
		self.horas_trabalhadas = horas_trabalhadas

	def calcular(self):
		return self.valor_hora * self.horas_trabalhadas


class SalarioComissionado(CalculoSalarioStrategy):
	def __init__(self, valor_base, vendas, percentual_comissao):
		self.valor_base = valor_base
		self.vendas = vendas
		self.percentual_comissao = percentual_comissao

	def calcular(self):
		return self.valor_base + self.vendas * self.percentual_comissao


class FolhaPagamento:
	def __init__(self):
		self.funcionarios = []

	def adicionar(self, nome, calculo: CalculoSalarioStrategy):
		self.funcionarios.append((nome, calculo))

	def processar(self):
		for nome, calculo in self.funcionarios:
			print(f"{nome}: R$ {calculo.calcular():.2f}")

folha = FolhaPagamento()
folha.adicionar("Ana (CLT)", SalarioCLT(3000))
folha.adicionar("Bruno (Freelancer)", SalarioFreelancer(50, 80))
folha.adicionar("Carla (Comissionada)", SalarioComissionado(1500, 10000, 0.05))
folha.processar()
