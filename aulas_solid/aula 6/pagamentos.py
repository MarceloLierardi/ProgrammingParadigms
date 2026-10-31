class Pagamento:
	def pagar(self, valor):
		print(f"Pagamento de R$ {valor}")


class Pix(Pagamento):
	def pagar(self, valor):
		print(f"PIX de R$ {valor}")


class Cartao(Pagamento):
	def pagar(self, valor):
		print(f"Cartão de R$ {valor}")


class Boleto(Pagamento):
	def pagar(self, valor):
		print(f"Boleto de R$ {valor}")


class PagamentoQuebrado(Pagamento):
	def pagar(self, valor):
		raise Exception("Não suportado")


def finalizar_pagamento(pagamento, valor):
	pagamento.pagar(valor)


if __name__ == "__main__":
	for pagamento in [Pagamento(), Pix(), Cartao(), Boleto()]:
		finalizar_pagamento(pagamento, 100)

	print("1. Pix pode substituir Pagamento? Sim.")
	print("2. Cartao pode substituir Pagamento? Sim.")
	print("3. Violação do LSP? Não, todas respeitam o contrato pagar(valor).")
	print("4. Uma classe que lança exceção em pagar() viola o LSP:")
	try:
		finalizar_pagamento(PagamentoQuebrado(), 100)
	except Exception as erro:
		print(f"   finalizar_pagamento quebrou: {erro}")
