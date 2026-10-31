from abc import ABC, abstractmethod


class Imprimivel(ABC):
	@abstractmethod
	def imprimir(self, documento):
		pass


class Digitalizavel(ABC):
	@abstractmethod
	def digitalizar(self, documento):
		pass


class Copiavel(ABC):
	@abstractmethod
	def copiar(self, documento):
		pass


class ImpressoraSimples(Imprimivel):
	def imprimir(self, documento):
		print(f"Impressora simples imprimindo: {documento}")


class ImpressoraMultifuncional(Imprimivel, Digitalizavel, Copiavel):
	def imprimir(self, documento):
		print(f"Multifuncional imprimindo: {documento}")

	def digitalizar(self, documento):
		print(f"Multifuncional digitalizando: {documento}")

	def copiar(self, documento):
		print(f"Multifuncional copiando: {documento}")

simples = ImpressoraSimples()
simples.imprimir("Relatório.pdf")

multifuncional = ImpressoraMultifuncional()
multifuncional.imprimir("Contrato.pdf")
multifuncional.digitalizar("Documento.pdf")
multifuncional.copiar("Documento.pdf")
