from abc import ABC, abstractmethod


class Produto:
	def __init__(self, nome, preco, quantidade):
		if preco < 0:
			raise ValueError("Preço não pode ser negativo")
		if quantidade <= 0:
			raise ValueError("Quantidade deve ser maior que zero")
		self.__nome = nome
		self.__preco = preco
		self.__quantidade = quantidade

	def get_nome(self):
		return self.__nome

	def get_preco(self):
		return self.__preco

	def get_quantidade(self):
		return self.__quantidade

	def calcular_subtotal(self):
		return self.__preco * self.__quantidade


class DescontoStrategy(ABC):
	@abstractmethod
	def calcular(self, valor):
		pass


class DescontoComum(DescontoStrategy):
	def calcular(self, valor):
		return valor * 0.05


class DescontoVIP(DescontoStrategy):
	def calcular(self, valor):
		return valor * 0.10


class DescontoPremium(DescontoStrategy):
	def calcular(self, valor):
		return valor * 0.20


class DescontoEspecial(DescontoStrategy):
	def calcular(self, valor):
		return valor * 0.15


class Pedido:
	def __init__(self, desconto: DescontoStrategy):
		self.produtos = []
		self.desconto = desconto

	def adicionar_produto(self, produto: Produto):
		self.produtos.append(produto)

	def calcular_total_bruto(self):
		return sum(produto.calcular_subtotal() for produto in self.produtos)

	def calcular_total_final(self):
		bruto = self.calcular_total_bruto()
		return bruto - self.desconto.calcular(bruto)


class Comprovante(ABC):
	@abstractmethod
	def emitir(self, pedido: Pedido, total):
		pass


class ComprovanteSimples(Comprovante):
	def emitir(self, pedido, total):
		print(f"Comprovante simples - Total pago: R$ {total:.2f}")


class ComprovanteDetalhado(Comprovante):
	def emitir(self, pedido, total):
		print("Comprovante detalhado")
		for produto in pedido.produtos:
			print(
				f"  {produto.get_nome()} x{produto.get_quantidade()} "
				f"- R$ {produto.calcular_subtotal():.2f}"
			)
		print(f"  Total bruto: R$ {pedido.calcular_total_bruto():.2f}")
		print(f"  Total pago: R$ {total:.2f}")


class ComprovanteCreator(ABC):
	@abstractmethod
	def criar_comprovante(self) -> Comprovante:
		pass

	def emitir_comprovante(self, pedido, total):
		comprovante = self.criar_comprovante()
		comprovante.emitir(pedido, total)


class ComprovanteSimplesCreator(ComprovanteCreator):
	def criar_comprovante(self) -> Comprovante:
		return ComprovanteSimples()


class ComprovanteDetalhadoCreator(ComprovanteCreator):
	def criar_comprovante(self) -> Comprovante:
		return ComprovanteDetalhado()


class ProcessadorPedido:
	def __init__(self, pedido: Pedido, creator: ComprovanteCreator):
		self.pedido = pedido
		self.creator = creator

	def processar(self):
		total = self.pedido.calcular_total_final()
		self.creator.emitir_comprovante(self.pedido, total)


def montar_pedido(desconto):
	pedido = Pedido(desconto)
	pedido.adicionar_produto(Produto("Teclado", 150.0, 2))
	pedido.adicionar_produto(Produto("Mouse", 80.0, 1))
	pedido.adicionar_produto(Produto("Monitor", 900.0, 1))
	return pedido

descontos = [
	("Comum", DescontoComum()),
	("VIP", DescontoVIP()),
	("Premium", DescontoPremium()),
	("Especial 15%", DescontoEspecial()),
]

for nome, desconto in descontos:
	print(f"--- Desconto {nome} ---")
	ProcessadorPedido(montar_pedido(desconto), ComprovanteSimplesCreator()).processar()
	ProcessadorPedido(montar_pedido(desconto), ComprovanteDetalhadoCreator()).processar()
