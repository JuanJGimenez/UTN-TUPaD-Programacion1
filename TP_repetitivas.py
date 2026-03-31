# Ejercicio 1 — “Caja del Kiosco”

nombre_cliente = input("Ingrese su nombre: ")

while nombre_cliente == "" or not nombre_cliente.isalpha():
    nombre_cliente = input("Ingrese un nombre valido: ")

cant_productos = int(input("Ingrese la cantidad de productos: "))

while not str(cant_productos).isdigit() or cant_productos == 0:
    cant_productos = int(input("Ingrese una cantidad de productos valida: "))

total_sin_descuento = 0
total_con_descuento = 0

for i in range(cant_productos):
    precio_producto = input(f"Ingrese el precio del producto número {i+1}: ")
    while not precio_producto.isdigit():
        precio_producto = input("Ingrese un precio valido: ")

    precio_producto = int(precio_producto)
    descuento_producto = input("Tiene descuento S/N?: ").lower()
    while descuento_producto not in ["s" , "n"]:
        descuento_producto = input("Ingrese S para si o N para no: ").lower()
    if descuento_producto == "s":
        total_con_descuento += precio_producto * 0.90

    total_sin_descuento += precio_producto

ahorro = total_sin_descuento - total_con_descuento 
promedio = (total_sin_descuento + total_con_descuento) / 3

print(f"Cliente: {nombre_cliente}")
print(f"Cantidad de productos: {cant_productos}")
print(f"Total sin descuento: {total_sin_descuento}")
print(f"Total con descuento: {total_con_descuento}")
print(f"Ahorro: {ahorro}")
print(f"Promedio: {promedio:.2f}")


# Ejercicio 2  — “Acceso al Campus y Menú Seguro” ---------------------------------------------------------------

usuario_correcto = "alumno" 
clave_correcta = "python123"
acceso = False
intentos = 3

for i in range(3):
    usuario = input("Ingrese el usuario: ")
    clave = input("Ingrese la clave: ")
    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("Acceso permitido")
        break
    else:
        intentos += -1
        print(f"Credenciales incorrectas. Le quedan {intentos} intentos.")

if not acceso:
    print("Cuenta bloqueada.")
else:
    opcion = 0
    while opcion != 4:
        print("1 - Ver estado de inscripcion.")
        print("2 - Cambiar clave.")
        print("3 - Mostrar mensaje motivacional.")
        print("4 - Salir.")
        opcion = input("Elija una opcion: ")
        if str(opcion).isdigit():
            match opcion:
                case "1":
                    print("Inscripto.")
                case "2":
                    clave = input("Nueva clave: ")
                    while len(clave) < 6:
                        print("Error: minimo 6 caracteres.")
                        clave = input("Nueva clave: ")
                    clave_confirm = input("Vuelva a ingresar la clave: ")
                    while clave != clave_confirm:
                        print("Las claves deben coincidir.")
                        clave_confirm = input("Vuelva a ingresar la clave: ")
                case "3":
                    print("Cumple sus sueios quien resiste!.")
                case "4":
                    break
                case _:
                    print("Error: opcion fuera de rango.")
        else:
            print("Error: ingrese un número valido.")

# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

nombre_operador = input("Ingrese el nombre del operador: ")
while not nombre_operador.isalpha():
    nombre_operador = input("Ingrese un nombre valido (solo letras): ")

opcion = 0
lunes_t1 = ""
lunes_t2 = ""
lunes_t3 = ""
lunes_t4 = ""
martes_t1 = ""
martes_t2 = ""
martes_t3 = ""

while opcion != 5:
        print("1 - Reservar turno.")
        print("2 - Cancelar turno.")
        print("3 - Ver agenda del día.")
        print("4 - Ver resumen general.")
        print("5 - Cerrar sistema.")
        opcion = input("Elija una opcion: ")
        if str(opcion).isdigit():
            match opcion:
                case "1":
                    dia_turno = int(input("Que dia desea reservar (1 - Lunes / 2 - Martes): "))
                    nombre_paciente = input("Ingrese el nomre del paciente: ")
                    while not nombre_paciente.isalpha():
                        nombre_paciente = input("Ingrese un nombre valido (solo letras): ")
                    if dia_turno == 1:
                        if lunes_t1 == nombre_paciente or lunes_t2 == nombre_paciente or lunes_t3 == nombre_paciente or lunes_t4 == nombre_paciente:
                            print(f"El paciente {nombre_paciente} ya tiene asignado un turno el dia lunes.")
                        elif lunes_t1 == "":
                            lunes_t1 = nombre_paciente
                            print(f"Se reservo el primer turno para el dia lunes. Paciente {nombre_paciente}")
                        elif lunes_t2 == "":
                            lunes_t2 = nombre_paciente
                            print(f"Se reservo el segundo turno para el dia lunes. Paciente {nombre_paciente}")
                        elif lunes_t3 == "":
                            lunes_t3 = nombre_paciente
                            print(f"Se reservo el tercer turno para el dia lunes. Paciente {nombre_paciente}")
                        elif lunes_t4 == "":
                            lunes_t4 = nombre_paciente
                            print(f"Se reservo el cuarto turno para el dia lunes. Paciente {nombre_paciente}")
                        else: 
                            print("No hay turnos disponibles para el dia lunes.")
                    if dia_turno == 2:
                        if martes_t1 == nombre_paciente or martes_t2 == nombre_paciente or martes_t3 == nombre_paciente:
                            print(f"El paciente {nombre_paciente} ya tiene asignado un turno el dia martes.")
                        elif martes_t1 == "":
                            martes_t1 = nombre_paciente
                            print(f"Se reservo el primer turno para el dia martes. Paciente {nombre_paciente}")
                        elif martes_t2 == "":
                            martes_t2 = nombre_paciente
                            print(f"Se reservo el segundo turno para el dia martes. Paciente {nombre_paciente}")
                        elif martes_t3 == "":
                            martes_t3 = nombre_paciente
                            print(f"Se reservo el tercer turno para el dia martes. Paciente {nombre_paciente}")
                        else: 
                            print("No hay turnos disponibles para el dia martes.")
                case "2":
                    dia_turno = int(input("Que dia desea cancelar? (1 - lunes / 2 - martes: "))
                    nombre_paciente = input("Ingrese el nombre del paciente: ")
                    while not nombre_paciente.isalpha():
                        nombre_paciente = input("Ingrese un nombre valido (solo letras): ")
                    if dia_turno == 1:
                        if nombre_paciente == lunes_t1:
                            lunes_t1 = ""
                        elif nombre_paciente == lunes_t2:
                            lunes_t2 = ""
                        elif nombre_paciente == lunes_t3:
                            lunes_t3 = ""
                        elif nombre_paciente == lunes_t4:
                            lunes_t4 = ""
                        else:
                            print("Turno inexistente.")
                    if dia_turno == 2:
                        if nombre_paciente == martes_t1:
                            martes_t1 = ""
                        elif nombre_paciente == martes_t2:
                            martes_t2 = ""
                        elif nombre_paciente == martes_t3:
                            martes_t3 = ""
                        else:
                            print("Turno inexistente.")
                case "3":
                    dia_turno = int(input("Que dia desea consultar? 1 - lunes / 2 - martes: "))
                    if dia_turno == 1:
                        print(f"Lunes primer turno: {lunes_t1 if lunes_t1 != "" else "Libre"}")
                        print(f"Lunes segundo turno: {lunes_t2 if lunes_t2 != "" else "Libre"}")
                        print(f"Lunes tercer turno: {lunes_t3 if lunes_t3 != "" else "Libre"}")
                        print(f"Lunes cuarto turno: {lunes_t4 if lunes_t4 != "" else "Libre"}")
                    if dia_turno == 2:
                        print(f"Martes primer turno: {martes_t1 if martes_t1 != "" else "Libre"}")
                        print(f"Martes segundo turno: {martes_t2 if martes_t2 != "" else "Libre"}")
                        print(f"Martes tercer turno: {martes_t3 if martes_t3 != "" else "Libre"}")
                case "4":
                    disponible = 0
                    if lunes_t1 == "": disponible += 1
                    if lunes_t2 == "": disponible += 1
                    if lunes_t3 == "": disponible += 1
                    if lunes_t4 == "": disponible += 1
                    disponible_lunes = disponible
                    print(f"Turnos disponibles para el dia lunes: {disponible}")
                    disponible = 0
                    if martes_t1 == "": disponible += 1
                    if martes_t2 == "": disponible += 1
                    if martes_t3 == "": disponible += 1
                    print(f"Turnos disponibles para el dia martes: {disponible}")
                    if disponible_lunes == disponible:
                        print(f"Turnos disponibles lunes y martes: {disponible}")
                case "5":
                    break
                case _:
                    print("Error: opcion fuera de rango.")
        else:
            print("Error: ingrese un número valido.")


# Ejercicio 4  — “Escape Room: La Bóveda”

energia = 100
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = ""
opcion = 0
forzar_cont = 0

nombre_agente = input("Ingrese el nombre del agente: ")
while not nombre_agente.isalpha():
    nombre_agente = input("Ingrese un nombre valido (solo letras): ")
        
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:
        
        if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
            print("Sistema bloqueado. DERROTA.")
            break

        print(f"Energial actual: {energia}. Tiempo restante: {tiempo}. Cerraduras abiertas: {cerraduras_abiertas}.")
        print("1 - Forzar cerradura. (costo: -20 energía, -2 tiempo)")
        print("2 - Hackear panel. (costo: -10 energía, -3 tiempo)")
        print("3 - Descansar. (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra)")
        opcion = input("Elija una opcion: ")

        while not opcion.isdigit():
            opcion = input("Ingrese un numero valido: ")
            
        match opcion:
            case "1":
                energia -= 20
                tiempo -= 2
                forzar_cont += 1 
                if forzar_cont == 3:
                    alarma = True
                    print("Forzaste 3 veces seguidas. La cerradura se trabó y activó la alarma.")
                elif energia < 40:
                    numero = input("Riesgo de alarma. Ingrese un numero del 1 al 3: ")
                    while not numero.isdigit():
                        numero = input("Ingrese un numero valido: ")
                    if numero == 3:
                        alarma = True
                        print("Activaste la alarma!.")
                    else:
                        cerraduras_abiertas += 1
                        print(f"cerradura abierta {cerraduras_abiertas}")
            case "2":
                forzar_cont_cont = 0
                energia -= 10
                tiempo -= 3
                for i in range  (1, 4):
                    print(f"Progreso: {i}")
                    codigo_parcial += input("Escriba el codigo: ")
                if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                    erraduras_abiertas += 1
                    print("Código completado. Cerradura abierta.")
            case "3":
                forzar_cont = 0
                tiempo -= 1
                if energia <= 75:
                    if alarma:
                        energia -= 10
                    else:
                        energia += 15
                print("Ya descansaste.")
            case _:
                print("Numero fuera de rango. Ingrese un numero del 1 al 3: ")

        # Resultado final
        if cerraduras_abiertas == 3:
            print("VICTORIA: Abriste la bóveda.")
        elif energia <= 0 or tiempo <= 0:
            print("DERROTA: Te quedaste sin recursos.")


# Ejercicio 5  — “Escape Room:"La Arena del Gladiador"
# En este ejercicio realmente me ayude con la IA un poco. Es un ejercicio que realizamos en el ingreso. Estoy atrasado con los ejercicios y necesito seguir avanzando.


nombre = input("Nombre del Gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

# Inicialización de variables
vida_jugador = 100          # int
vida_enemigo = 100          # int
pociones = 3                # int
danio_pesado = 15           # int
danio_enemigo = 12          # int
turno_jugador = True        # boolean

print("\n=== INICIO DEL COMBATE ===")

# Paso 3: Ciclo de combate
while vida_jugador > 0 and vida_enemigo > 0:

    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

    # MENÚ
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = input("Opción: ")
    while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    # Uso de match-case
    match opcion:

        # ACCIÓN 1: ATAQUE PESADO
        case 1:
            if vida_enemigo < 20:
                danio = danio_pesado * 1.5   # float
                print("\n>> ¡Golpe crítico!")
            else:
                danio = danio_pesado

            vida_enemigo -= danio
            print(f">> ¡Atacaste al enemigo por {danio} puntos de daño!")

        # ACCIÓN 2: RÁFAGA VELOZ
        case 2:
            print("\n>> ¡Inicias una ráfaga de golpes!")
            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        # ACCIÓN 3: CURAR
        case 3:
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("\n>> Usaste una poción. Recuperaste 30 HP.")
            else:
                print("\n>> ¡No quedan pociones!")

    # Turno del enemigo
    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f">> ¡El enemigo te atacó por {danio_enemigo} puntos de daño!")

# Paso 4: Resultado final
print("\n=== FIN DEL COMBATE ===")
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")



    
