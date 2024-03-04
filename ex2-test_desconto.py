importar  pytest
de  desconto  importação  calcular_desconto


def  teste_desconto_valor_negativo ():
    com  pytest . aumenta ( ValueError ):
        calcular_desconto ( - 1 )


def  teste_desconto_valor_100 ():
    assert  calcular_desconto ( 100 ) == (
        pytest . aprox ( 91,00 , 0,01 ), pytest . aproximadamente ( 9,00 , 0,01 ))


def  teste_desconto_valor_1500 ():
    assert  calcular_desconto ( 1500 ) == (
        pytest . aproximadamente ( 1365,00 , 0,01 ), pytest . aproximadamente ( 135,00 , 0,01 ))


def  teste_desconto_valor_60000 ():
    assert  calcular_desconto ( 60000 ) == (
        pytest . aproximadamente ( 54600,00 , 0,01 ), pytest . aprox ( 5400,00 , 0,01 ))
