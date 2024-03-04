def  calcular_salario ( valor_hora_aula , numero_aulas , percentual_inss ):
    se  valor_hora_aula  <  0 :
        raise  ValueError ( 'Valor hora aula inválida' )
    se  numero_aulas  <  0 :
        raise  ValueError ( 'Número de aulas inválidas' )
    se  percentual_inss  <  0  ou  percentual_inss  >  100 :
        raise  ValueError ( 'Percentual INSS inválido' )

    liquido  =  valor_hora_aula  *  numero_aulas  * ( 1  -  percentual_inss  /  100 )

    devolver  líquido
