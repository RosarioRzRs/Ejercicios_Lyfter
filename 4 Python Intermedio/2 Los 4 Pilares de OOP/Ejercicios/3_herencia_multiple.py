# La herencia múltiple permite que una clase herede atributos y métodos de dos o más clases padre al mismo tiempo.
# Usos principales:
# Creación de Mixins: Son clases pequeñas con una sola función (como guardar registros o exportar a JSON).
# Otras clases las usan para sumar esa habilidad sin enredar la jerarquía.
# Combinar dominios: Sirve para unir características de dos mundos distintos 
# en un objeto final que necesita ambas funciones.
# Reutilizar código: Evita repetir funciones cuando un objeto nuevo comparte comportamientos de 
# familias de clases totalmente diferentes.


class Tradicional:
    def show_hour(self):
        print("Mostrando hora ")

    def create_alarm(self, hour):
        print(f"Alarma programada a las {hour}")

    def create_timer(self):
        print("temporizador activo")


class Salud:
    def monitor_ritmo_cardiaco(self):
        print("Monitoreando ritmo cardiaco")

    def monitor_oxygen_saturation(self):
        print("Monitoreando saturacion de oxigeno")

    def monitor_stress_level(self):
        print("Monitoreando nivel de estres")


class Smartwatch (Tradicional, Salud):
    def sychronize(self):
        print("Sincronizando notificaciones")

#Creando el objeto y llamando los metodos de cada clase
smartwatch = Smartwatch()
smartwatch.show_hour()
smartwatch.create_alarm(5)
smartwatch.create_timer()
smartwatch.monitor_ritmo_cardiaco()
smartwatch.monitor_oxygen_saturation()
smartwatch.monitor_stress_level()
smartwatch.sychronize()
