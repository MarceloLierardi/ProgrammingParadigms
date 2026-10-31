from abc import ABC, abstractmethod


class Documento(ABC):
	@abstractmethod
	def gerar(self, conteudo):
		pass


class DocumentoPDF(Documento):
	def gerar(self, conteudo):
		print(f"Gerando PDF: {conteudo}")


class DocumentoTXT(Documento):
	def gerar(self, conteudo):
		print(f"Gerando TXT: {conteudo}")


class DocumentoCreator(ABC):
	@abstractmethod
	def criar_documento(self) -> Documento:
		pass

	def gerar_documento(self, conteudo):
		documento = self.criar_documento()
		documento.gerar(conteudo)


class PDFCreator(DocumentoCreator):
	def criar_documento(self) -> Documento:
		return DocumentoPDF()


class TXTCreator(DocumentoCreator):
	def criar_documento(self) -> Documento:
		return DocumentoTXT()

PDFCreator().gerar_documento("Relatório mensal")
TXTCreator().gerar_documento("Anotações da reunião")
