from abc import ABC, abstractmethod


class Abrivel(ABC):
	@abstractmethod
	def abrir(self):
		pass


class Editavel(ABC):
	@abstractmethod
	def editar(self):
		pass


class Imprimivel(ABC):
	@abstractmethod
	def imprimir(self):
		pass


class DocumentoPDF(Abrivel, Imprimivel):
	def __init__(self, nome):
		self.nome = nome

	def abrir(self):
		print(f"Abrindo {self.nome}")

	def imprimir(self):
		print(f"Imprimindo {self.nome}")


class DocumentoWord(Abrivel, Editavel, Imprimivel):
	def __init__(self, nome):
		self.nome = nome

	def abrir(self):
		print(f"Abrindo {self.nome}")

	def editar(self):
		print(f"Editando {self.nome}")

	def imprimir(self):
		print(f"Imprimindo {self.nome}")


class DocumentoSomenteLeitura(Abrivel):
	def __init__(self, nome):
		self.nome = nome

	def abrir(self):
		print(f"Abrindo {self.nome}")


if __name__ == "__main__":
	documentos = [
		DocumentoPDF("arquivo.pdf"),
		DocumentoWord("trabalho.docx"),
		DocumentoSomenteLeitura("contrato_protegido.pdf"),
	]

	for documento in documentos:
		documento.abrir()

	for documento in documentos:
		if isinstance(documento, Editavel):
			documento.editar()

	for documento in documentos:
		if isinstance(documento, Imprimivel):
			documento.imprimir()
