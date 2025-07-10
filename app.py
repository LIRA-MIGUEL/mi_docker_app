from datetime import datetime

nombre = input("Ingresa tu nombre: ")

fecha_str = input("Ingresa tu fecha de nacimiento (dd/mm/aaaa): ")

try:
    fecha_nacimiento = datetime.strptime(fecha_str, "%d/%m/%Y")
    hoy = datetime.now()
    
    edad = hoy.year - fecha_nacimiento.year
    if (hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1

    print("\n--- Información del Usuario ---")
    print(f"Nombre: {nombre}")
    print(f"Fecha de nacimiento: {fecha_nacimiento.strftime('%d/%m/%Y')}")
    print(f"Edad: {edad} años")

except ValueError:
    print("Fecha inválida. La fecha tiene que ser dd/mm/aaaa.")
