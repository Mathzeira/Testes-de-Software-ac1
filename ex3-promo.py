def  calcula_promocao ( valor_produto , desconto ):
    se  valor_produto  <  0 :
        raise  ValueError ( 'Valor do produto inválido' )
    se  desconto  <  0 :
        raise  ValueError ( 'Valor do desconto inválido' )
    if  desconto  >  valor_produto :
        raise  ValueError ( 'Valor do desconto maior que o valor do produto' )

    novo_valor  =  valor_produto  -  desconto

    retornar  novo_valor
