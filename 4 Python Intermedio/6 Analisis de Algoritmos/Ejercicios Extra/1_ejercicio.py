# Los siguientes dos algoritmos hacen lo mismo: calcular la suma de los primeros n números naturales
# Versión 1:
def manual_add(n):
    result = 0    #  O(1)
    for i in range(1, n + 1):      #  O(n)
        result += i   # O(1)
    return result     # O (1)

# Versión 2:
def add_formula(n):
    return n * (n + 1) // 2     # O(1)

# Preguntas:
# ¿Cuál es la complejidad de cada versión?
#   la primera version es O(n) ya que es un ciclo
#  En la segunda version es O(1) ya que solo ejecuta la operacion y 
#  devuelve el resultado
# ¿Qué versión usaría si number = 1 000 000 000? ¿Por qué? 
#  Usaria la version 2 ya que solo realizaria la operacion y devolveria el resultadi
# asi como el tiempo de ejecicion era muy rapido