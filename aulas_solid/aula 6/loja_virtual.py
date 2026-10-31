from abc import ABC, abstractmethod


class Pagamento(ABC):
	@abstractmethod
	def pagar(self, valor):
		pass


class Notificador(ABC):
	@abstractmethod
	def enviar(self, mensagem):
		pass


class Pix(Pagamento):
	def pagar(self, valor):
		print(f"Pagamento PIX de R$ {valor:.2f} realizado.")


class Cartao(Pagamento):
	def pagar(self, valor):
		print(f"Pagamento no cartão de R$ {valor:.2f} realizado.")


class Boleto(Pagamento):
	def pagar(self, valor):
		print(f"Pagamento por boleto de R$ {valor:.2f} gerado.")


class PayPal(Pagamento):
	def pagar(self, valor):
		print(f"Pagamento PayPal de R$ {valor:.2f} realizado.")


class EmailService(Notificador):
	def enviar(self, mensagem):
		print(f"Email: {mensagem}")


class SMSService(Notificador):
	def enviar(self, mensagem):
		print(f"SMS: {mensagem}")


class PedidoService:
	def __init__(self, pagamento: Pagamento, notificador: Notificador):
		self.pagamento = pagamento
		self.notificador = notificador

	def finalizar(self, valor):
		self.pagamento.pagar(valor)
		self.notificador.enviar("Pedido finalizado com sucesso!")


if __name__ == "__main__":
	pedido1 = PedidoService(Pix(), EmailService())
	pedido1.finalizar(150)

	pedido2 = PedidoService(Cartao(), SMSService())
	pedido2.finalizar(300)

	pedido3 = PedidoService(Boleto(), EmailService())
	pedido3.finalizar(80)

	pedido4 = PedidoService(PayPal(), SMSService())
	pedido4.finalizar(200)
