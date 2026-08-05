###########Definir todas las variables###############
text_1 = "suma 2"
text_2 = " cadenas"
number_int = 100
number_float = 100.0
value_1 = True
value_2 = False
name_list = ["Rosa", "Luis", "Carolina", "Pepe"]
number_list = [15, 26, 100, 520]

############Suma de combinacion de variables##############

##### string + string 
add_data_type = text_1 + text_2 ##### SIN ERROR



##### string + int → can only concatenate str (not "int") to str
#add_data_type = text_1 + number_int ###ERROR: can only concatenate str (not "int") to str
                                    ### NO SE PUEDE CONCATENAR 2 TIPOS DE DATOS DIFERENTES



##### int + string 
#add_data_type = number_int + text_2  ####ERROR: unsupported operand type(s) for +: 'int' and 'str'
                                    ####OPERACION NO SOPORTABLE POR SER DE DIFERENTE TIPO



##### list + list 
#add_data_type = name_list [0] + name_list [1]  ####OK, SON DEL MISMO TIPO
#add_data_type = name_list [0] + number_list [0]  ###can only concatenate str (not "int") to str
                                                  ###SOLO SE PUEDE CONCATENAR STRING CON STRING  
#add_data_type = number_list [0] + number_list [1]  ##OK, PUDO HACER LA SUMA = 41, PORQUE SON DEL MISMO TIPO



##### string + list 
#add_data_type = text_1 + number_list [0]  ###ERROR: can only concatenate str (not "int") to str
                                          ###MANDA ERROR YA QUE BUSCA QUE EL TIPO DE DATOS SEA UNA CADENA
#add_data_type = text_1 + name_list [0]   ###OK, MUESTRA suma 2Rosa,  SON DEL MISMO TIPO



##### float + int
#add_data_type = number_float + number_int   ####OK, DIO COMO RESULTADO = 200.0



##### bool + bool 
#add_data_type = value_1 + value_2  ####OK, RESULTADO = 1. HIZO LA SUMA

print (add_data_type)