from abc import ABC, abstractmethod


class Relatorio(ABC):
	@abstractmethod
	def gerar(self, dados):
		pass


class RelatorioFinanceiro(Relatorio):
	def gerar(self, dados):
		print(f"Relatório financeiro: {dados}")


class RelatorioEstoque(Relatorio):
	def gerar(self, dados):
		print(f"Relatório de estoque: {dados}")


class RelatorioVendas(Relatorio):
	def gerar(self, dados):
		print(f"Relatório de vendas: {dados}")


class RelatorioClientes(Relatorio):
	def gerar(self, dados):
		print(f"Relatório de clientes: {dados}")


class RelatorioCreator(ABC):
	@abstractmethod
	def criar_relatorio(self) -> Relatorio:
		pass

	def executar_relatorio(self, dados):
		relatorio = self.criar_relatorio()
		relatorio.gerar(dados)


class FinanceiroCreator(RelatorioCreator):
	def criar_relatorio(self) -> Relatorio:
		return RelatorioFinanceiro()


class EstoqueCreator(RelatorioCreator):
	def criar_relatorio(self) -> Relatorio:
		return RelatorioEstoque()


class VendasCreator(RelatorioCreator):
	def criar_relatorio(self) -> Relatorio:
		return RelatorioVendas()


class ClientesCreator(RelatorioCreator):
	def criar_relatorio(self) -> Relatorio:
		return RelatorioClientes()


if __name__ == "__main__":
	FinanceiroCreator().executar_relatorio("receitas e despesas")
	EstoqueCreator().executar_relatorio("1200 itens")
	VendasCreator().executar_relatorio("350 vendas")
	ClientesCreator().executar_relatorio("80 clientes ativos")
