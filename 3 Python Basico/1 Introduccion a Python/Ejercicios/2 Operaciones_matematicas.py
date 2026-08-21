Selection = """Seleccione el tipo de Operaccion a realizar:
1 Suma
2 Resta
3 Multiplicacion
4 Division"""
print(Selection)
Operation = int (input("Numero de Operaccion:"))
Value_1 = int(input("Ingrese el Valor 1: "))
Value_2 = int(input("Ingrese el Valor 2: "))
if Operation == 1:
    Result = Value_1 + Value_2
elif Operation == 2:
    Result = Value_1 - Value_2
elif Operation == 3:
    Result = Value_1 * Value_2
elif Operation == 4:
    Result = Value_1 / Value_2
else:
    Result = 0
str_Result = str(Result)
print ("El resultado de la Operaccion es: "+ str_Result)