from abc import ABC, abstractmethod


class Material(ABC):
	def __init__(self, titulo, autor):
		self.titulo = titulo
		self.autor = autor

	@abstractmethod
	def disponibilizar(self):
		pass

	def mensagem_confirmacao(self):
		return "Empréstimo realizado com sucesso!"


class Devolvivel(ABC):
	@abstractmethod
	def devolver(self):
		pass


class Notificador(ABC):
	@abstractmethod
	def enviar(self, mensagem):
		pass


class Livro(Material, Devolvivel):
	def disponibilizar(self):
		print(f"Livro: {self.titulo} emprestado.")

	def devolver(self):
		print(f"Livro: {self.titulo} devolvido.")


class Revista(Material, Devolvivel):
	def disponibilizar(self):
		print(f"Revista: {self.titulo} emprestada.")

	def devolver(self):
		print(f"Revista: {self.titulo} devolvida.")


class Ebook(Material):
	def disponibilizar(self):
		print(f"Ebook: {self.titulo} liberado.")

	def mensagem_confirmacao(self):
		return "Acesso digital liberado com sucesso!"


class Audiobook(Material):
	def disponibilizar(self):
		print(f"Audiobook: {self.titulo} liberado para audição.")

	def mensagem_confirmacao(self):
		return "Acesso ao áudio liberado com sucesso!"


class EmailService(Notificador):
	def enviar(self, mensagem):
		print(f"Email: {mensagem}")


class SMSService(Notificador):
	def enviar(self, mensagem):
		print(f"SMS: {mensagem}")


class EmprestimoRepository:
	def registrar(self, material, usuario):
		print(f"Empréstimo registrado para {usuario}.")


class EmprestimoService:
	def __init__(self, notificador: Notificador, repositorio: EmprestimoRepository):
		self.notificador = notificador
		self.repositorio = repositorio

	def emprestar(self, material: Material, usuario):
		material.disponibilizar()
		self.repositorio.registrar(material, usuario)
		self.notificador.enviar(material.mensagem_confirmacao())



repositorio = EmprestimoRepository()

EmprestimoService(EmailService(), repositorio).emprestar(
	Livro("Python para Iniciantes", "Autor A"), "Maria"
)
EmprestimoService(SMSService(), repositorio).emprestar(
	Revista("Tecnologia Hoje", "Editora B"), "João"
)
EmprestimoService(EmailService(), repositorio).emprestar(
	Ebook("Aprendendo POO", "Autor C"), "Ana"
)
EmprestimoService(SMSService(), repositorio).emprestar(
	Audiobook("Clean Code em Áudio", "Autor D"), "Carlos"
)
