from abc import ABC, abstractmethod


class Repositorio(ABC):
	@abstractmethod
	def salvar(self, dados):
		pass


class MySQLRepositorio(Repositorio):
	def salvar(self, dados):
		print(f"Salvando no MySQL: {dados}")


class PostgreSQLRepositorio(Repositorio):
	def salvar(self, dados):
		print(f"Salvando no PostgreSQL: {dados}")


class RelatorioService:
	def __init__(self, repositorio: Repositorio):
		self.repositorio = repositorio

	def gerar(self):
		print("Gerando relatório...")
		self.repositorio.salvar("Relatório")


if __name__ == "__main__":
	RelatorioService(MySQLRepositorio()).gerar()
	RelatorioService(PostgreSQLRepositorio()).gerar()
