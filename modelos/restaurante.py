from modelos.avaliacao import Avaliacao


class Restaurante:
    resturantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.resturantes.append(self)

    def __str__(self):
        return f"{self._nome} - {self._categoria}"

    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliacao'.ljust(25)} | Ativo")
        for r in Restaurante.resturantes:
            print(f"{r.nome.ljust(25)} | {r.categoria.ljust(25)} | {str(r.media_avaliacao).ljust(25)} | {r.ativo}")

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        self._avaliacao.append(Avaliacao(cliente, nota))

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        
        soma_notas = sum(avaliacao.nota for avaliacao in self.avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas/quantidade_notas, 1)

        return media

    @property
    def ativo(self):
        return "☑" if self._ativo else "☐"

    @property
    def nome(self):
        return self._nome

    @property
    def categoria(self):
        return self._categoria
    
    @property
    def avaliacao(self):
        return self._avaliacao
