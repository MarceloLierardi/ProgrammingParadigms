from abc import ABC, abstractmethod


class Veiculo(ABC):
	@abstractmethod
	def mover(self):
		pass


class VeiculoCombustivel(Veiculo):
	@abstractmethod
	def abastecer(self):
		pass


class VeiculoEletrico(Veiculo):
	@abstractmethod
	def carregar(self):
		pass


class Carro(VeiculoCombustivel):
	def mover(self):
		print("Carro andando.")

	def abastecer(self):
		print("Carro abastecendo combustível...")


class Moto(VeiculoCombustivel):
	def mover(self):
		print("Moto andando.")

	def abastecer(self):
		print("Moto abastecendo combustível...")


class CarroEletrico(VeiculoEletrico):
	def mover(self):
		print("Carro elétrico andando.")

	def carregar(self):
		print("Carro elétrico carregando bateria...")

veiculos = [Carro(), Moto(), CarroEletrico()]

for veiculo in veiculos:
	veiculo.mover()

for veiculo in veiculos:
	if isinstance(veiculo, VeiculoCombustivel):
		veiculo.abastecer()
	elif isinstance(veiculo, VeiculoEletrico):
		veiculo.carregar()
