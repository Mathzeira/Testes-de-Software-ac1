importar  pytest
da  garcom  importação  calcula_gorjeta


def  teste_gorjeta_valor_despesa_negativo ():
    com  pytest . aumenta ( ValueError ):
        calcula_gorjeta ( - 1 )


def  test_gorjeta_valor_despesa_75_00 ():
    assert  calcula_gorjeta ( 75,00 ) == (
        pytest . aproximadamente ( 82,50 , 0,01 ), pytest . aproximadamente ( 7,50 , 0,01 ))


def  teste_gorjeta_valor_despesa_125 ():
    afirmar  calcula_gorjeta ( 125 ) == ( pytest.aproximadamente ( _ _
        137,50 , 0,01 ), pytest . aproximadamente ( 12,50 , 0,01 ))


def  test_gorjeta_valor_despesa_350_87 ():
    assert  calcula_gorjeta ( 350.87 ) == ( pytest.aproximadamente ( _ _
        385,96 , 0,01 ), pytest . aproximadamente ( 35,09 , 0,01 ))
