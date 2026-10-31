from abc import ABC, abstractmethod


class PagamentoStrategy(ABC):
	@abstractmethod
	def processar(self, valor):
		pass


class Pix(PagamentoStrategy):
	def processar(self, valor):
		print(f"Pagamento via Pix de R$ {valor:.2f} processado.")


class CartaoCredito(PagamentoStrategy):
	def processar(self, valor):
		print(f"Pagamento via cartão de crédito de R$ {valor:.2f} processado.")


class Boleto(PagamentoStrategy):
	def processar(self, valor):
		print(f"Pagamento via boleto de R$ {valor:.2f} processado.")


class Checkout:
	def __init__(self, pagamento: PagamentoStrategy):
		self.pagamento = pagamento

	def trocar_pagamento(self, pagamento: PagamentoStrategy):
		self.pagamento = pagamento

	def pagar(self, valor):
		self.pagamento.processar(valor)

checkout = Checkout(Pix())
checkout.pagar(100)

checkout.trocar_pagamento(CartaoCredito())
checkout.pagar(250)

checkout.trocar_pagamento(Boleto())
checkout.pagar(80)
