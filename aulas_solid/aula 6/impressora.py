from abc import ABC, abstractmethod


class Imprimivel(ABC):
	@abstractmethod
	def imprimir(self):
		pass


class Escaneavel(ABC):
	@abstractmethod
	def escanear(self):
		pass


class EnviaFax(ABC):
	@abstractmethod
	def enviar_fax(self):
		pass


class ImpressoraBasica(Imprimivel):
	def imprimir(self):
		print("Imprimindo...")


class ImpressoraMultifuncional(Imprimivel, Escaneavel, EnviaFax):
	def imprimir(self):
		print("Imprimindo...")

	def escanear(self):
		print("Escaneando...")

	def enviar_fax(self):
		print("Enviando fax...")


if __name__ == "__main__":
	basica = ImpressoraBasica()
	basica.imprimir()

	multifuncional = ImpressoraMultifuncional()
	multifuncional.imprimir()
	multifuncional.escanear()
	multifuncional.enviar_fax()
