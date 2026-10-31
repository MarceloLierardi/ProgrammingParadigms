from abc import ABC, abstractmethod


class Notificador(ABC):
	@abstractmethod
	def enviar(self, mensagem):
		pass


class EmailNotificador(Notificador):
	def enviar(self, mensagem):
		print(f"Enviando email: {mensagem}")


class SMSNotificador(Notificador):
	def enviar(self, mensagem):
		print(f"Enviando SMS: {mensagem}")


class PushNotificador(Notificador):
	def enviar(self, mensagem):
		print(f"Enviando push: {mensagem}")


class TelegramNotificador(Notificador):
	def enviar(self, mensagem):
		print(f"Enviando Telegram: {mensagem}")


class VendaService:
	def __init__(self, notificador: Notificador):
		self.notificador = notificador

	def finalizar_venda(self):
		print("Venda finalizada.")
		self.notificador.enviar("Compra realizada.")


if __name__ == "__main__":
	for notificador in [EmailNotificador(), SMSNotificador(), PushNotificador(), TelegramNotificador()]:
		venda = VendaService(notificador)
		venda.finalizar_venda()
