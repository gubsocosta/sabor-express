from modelos.restaurante import Restaurante

res_praca = Restaurante("praca", "gourmet")
res_mexicano = Restaurante("nacho libre", "Mexicana")
res_japa = Restaurante("nagomi", "Japonesa")

res_mexicano.receber_avaliacao('Gabriel', 9)
res_mexicano.receber_avaliacao('Fabiane', 10)

def main():
    Restaurante.listar_restaurantes()

if __name__ == "__main__":
    main()
