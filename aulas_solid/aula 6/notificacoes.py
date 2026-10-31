from abc import ABC, abstractmethod


class Notificador(ABC):
	@abstractmethod
	def enviar(self, mensagem):
		pass


class EmailService(Notificador):
	def enviar(self, mensagem):
		print(f"Email: {mensagem}")


class SMSService(Notificador):
	def enviar(self, mensagem):
		print(f"SMS: {mensagem}")


class WhatsAppService(Notificador):
	def enviar(self, mensagem):
		print(f"WhatsApp: {mensagem}")


class PedidoService:
	def __init__(self, notificador: Notificador):
		self.notificador = notificador

	def finalizar_pedido(self):
		self.notificador.enviar("Pedido realizado com sucesso!")

for notificador in [EmailService(), SMSService(), WhatsAppService()]:
	PedidoService(notificador).finalizar_pedido()
