importar  pytest
da  promoção  importar  calcula_promocao


def  teste_promo_valor_produto_negativo ():
    com  pytest . aumenta ( ValueError ):
        calcula_promocao ( - 1 , 1 )


def  teste_promo_desconto_negativo ():
    com  pytest . aumenta ( ValueError ):
        calcula_promocao ( 1 , - 1 )


def  test_promo_desconto_maior_que_valor_produto ():
    com  pytest . aumenta ( ValueError ):
        calcula_promocao ( 1 , 2 )


def  teste_promo_valor_produto_500_desconto_50 ():
    assert  calcula_promocao ( 500,00 , 50,00 ) ==  pytest . aproximadamente ( 450,00 , 0,01 )


def  test_promo_valor_produto_10500_desconto_500 ():
    assert  calcula_promocao ( 10500,00 , 500,00 ) ==  pytest . aproximadamente ( 10.000,00 , 0,01 )


def  teste_promo_valor_produto_90_desconto_0_80 ():
    assert  calcula_promocao ( 90,00 , 0,80 ) ==  pytest . aproximadamente ( 89,20 , 0,01 )
