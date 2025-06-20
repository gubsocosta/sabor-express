from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_mexicano = Restaurante("nacho libre", "Mexicana")
bebida_suco = Bebida("Suco de laranja", 5.0, "grande")
prato_pastel = Prato("Pastel", 4.0, "pastel de frango")

restaurante_mexicano.adicionar_no_cardapio(bebida_suco)
restaurante_mexicano.adicionar_no_cardapio(prato_pastel)


def main():
    restaurante_mexicano.cardapio


if __name__ == "__main__":
    main()
