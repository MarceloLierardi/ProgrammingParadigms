from abc import ABC, abstractmethod


class Transporte(ABC):
	@abstractmethod
	def entregar(self, destino):
		pass


class Moto(Transporte):
	def entregar(self, destino):
		print(f"Moto entregando em {destino}.")


class Carro(Transporte):
	def entregar(self, destino):
		print(f"Carro entregando em {destino}.")


class Caminhao(Transporte):
	def entregar(self, destino):
		print(f"Caminhão entregando em {destino}.")


class TransporteCreator(ABC):
	@abstractmethod
	def criar_transporte(self) -> Transporte:
		pass

	def executar_entrega(self, destino):
		transporte = self.criar_transporte()
		transporte.entregar(destino)


class MotoCreator(TransporteCreator):
	def criar_transporte(self) -> Transporte:
		return Moto()


class CarroCreator(TransporteCreator):
	def criar_transporte(self) -> Transporte:
		return Carro()


class CaminhaoCreator(TransporteCreator):
	def criar_transporte(self) -> Transporte:
		return Caminhao()


if __name__ == "__main__":
	MotoCreator().executar_entrega("Centro")
	CarroCreator().executar_entrega("Zona Sul")
	CaminhaoCreator().executar_entrega("Porto")
