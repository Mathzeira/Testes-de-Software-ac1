def  calcular_desconto ( valor_produto ):
    se  valor_produto  <  0 :
        raise  ValueError ( 'Valor do produto inválido' )

    novo_valor  =  valor_produto  *  0,91
    valor_desconto  =  valor_produto  -  novo_valor

    retornar  novo_valor , valor_desconto
