from abc import ABC, abstractmethod


class DescontoStrategy(ABC):
	@abstractmethod
	def aplicar(self, valor):
		pass


class DescontoComum(DescontoStrategy):
	def aplicar(self, valor):
		return valor * 0.95


class DescontoVIP(DescontoStrategy):
	def aplicar(self, valor):
		return valor * 0.90


class DescontoPremium(DescontoStrategy):
	def aplicar(self, valor):
		return valor * 0.80


class Venda:
	def __init__(self, desconto: DescontoStrategy):
		self.desconto = desconto

	def calcular_valor_final(self, valor):
		return self.desconto.aplicar(valor)

estrategias = [
	("Comum", DescontoComum()),
	("VIP", DescontoVIP()),
	("Premium", DescontoPremium()),
]

for nome, estrategia in estrategias:
	venda = Venda(estrategia)
	print(f"{nome}: R$ {venda.calcular_valor_final(500):.2f}")
