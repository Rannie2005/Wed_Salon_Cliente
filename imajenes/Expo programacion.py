import random
import re
import math 
from typing import List, Dict, Any


def saludo_personalizado():
    """1. Saludo Personalizado."""
    try:
        print("\n--- 1: Saludo Personalizado ---")
        nombre = input("Por favor, pon tu nombre: ").strip()
        print(f"¡Klk, {nombre}! Welcome a este programa.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def convertir_kilometros_a_millas():
    """2. Convertir Kilómetros a Millas."""
    try:
        print("\n--- 2: Convertir Kilómetros a Millas ---")
        kilometros = float(input("Poner la cantidad de kilómetros: "))
        millas = kilometros * 0.621371
        print(f"{kilometros} km equivalen a {millas:.2f} millas.")
    except ValueError:
        print("Error: Ingresa un número válido para los kilómetros.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def determinar_par_o_impar():
    """3. Determinar Par o Impar."""
    try:
        print("\n--- 3: Determinar Par o Impar ---")
        numero = int(input("Ponga un número: "))
        if numero % 2 == 0:
            print(f"{numero} es par.")
        else:
            print(f"{numero} es impar.")
    except ValueError:
        print("Error: Ingresa un número entero válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def calcular_area_triangulo():
    """4. Calcular Área de un Triángulo."""
    try:
        print("\n--- 4: Calcular Área de un Triángulo ---")
        base = float(input("Ingresar la base del triángulo: "))
        altura = float(input("Ingresar la altura del triángulo: "))
        area = (base * altura) / 2
        print(f"El área del triángulo es {area:.2f} unidades cuadradas.")
    except ValueError:
        print("Error: Ingresa números válidos para la base y la altura.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def tabla_multiplicar():
    """5. Tabla de Multiplicar."""
    try:
        print("\n--- 5: Tabla de Multiplicar ---")
        numero = int(input("Ingresar un número para su tabla de multiplicar: "))
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")
    except ValueError:
        print("Error: Ingresa un número entero válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def suma_numeros_pares():
    """6. Suma de Números Pares del 1 al 100."""
    try:
        print("\n--- 6: Suma de Números Pares del 1 al 100 ---")
        suma = sum(i for i in range(2, 101, 2))
        print(f"La suma de los números pares del 1 al 100 es: {suma}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def adivina_numero():
    """7. Adivina el Número."""
    try:
        print("\n--- 7: Adivina el Número ---")
        numero_secreto = random.randint(1, 100)
        intentos = 0
        print("Estoy pensando en un número entre 1 y 100.")
        while True:
            intento = int(input("Adivina el número: "))
            intentos += 1
            if intento == numero_secreto:
                print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
                break
            elif intento < numero_secreto:
                print("Demasiado bajo, vuelve a intentarlo.")
            else:
                print("Demasiado alto, vuelve a intentarlo.")
    except ValueError:
        print("Error: Ingresa un número entero válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def promedio_numeros():
    """8. Promedio de Números."""
    try:
        print("\n--- 8: Promedio de Números ---")
        numeros_str = input("Ingresa los números separados por espacios: ")
        numeros = [float(x.strip()) for x in numeros_str.split()]
        if not numeros:
            print("No ingresaste números válidos.")
            return
        promedio = sum(numeros) / len(numeros)
        print(f"El promedio de los números es: {promedio:.2f}")
    except ValueError:
        print("Error: Ingresa solo números válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def contar_palabra_en_frase():
    """9. Contar Palabra en Frase."""
    try:
        print("\n--- 9: Contar Palabra en Frase ---")
        frase = input("Ingresa una frase: ").lower()
        palabra = input("Ingresa la palabra a contar: ").lower()
        conteo = frase.split().count(palabra)
        print(f"La palabra '{palabra}' aparece {conteo} veces en la frase.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def ordenar_numeros():
    """10. Ordenar Números."""
    try:
        print("\n--- 10: Ordenar Números ---")
        numeros_str = input("Ingresa números separados por espacios: ")
        numeros = [float(x.strip()) for x in numeros_str.split()]
        if not numeros:
            print("No ingresaste números válidos.")
            return
        numeros.sort()
        print(f"Lista ordenada: {numeros}")
    except ValueError:
        print("Error: Ingresa solo números válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def convertir_grados():
    """11. Convertir Celsius a Fahrenheit y Viceversa."""
    try:
        print("\n--- 11: Convertir Grados ---")
        print("1. Celsius a Fahrenheit")
        print("2. Fahrenheit a Celsius")
        opcion = input("Elige una opción (1 o 2): ")
        if opcion == "1":
            celsius = float(input("Ingresa los grados Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C = {fahrenheit:.2f}°F")
        elif opcion == "2":
            fahrenheit = float(input("Ingresa los grados Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F = {celsius:.2f}°C")
        else:
            print("Opción inválida.")
    except ValueError:
        print("Error: Ingresa un número válido para los grados.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def calculadora_basica():
    """12. Calculadora Básica."""
    try:
        print("\n--- 12: Calculadora Básica ---")
        while True:
            print("\n1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Salir de la calculadora")
            opcion = input("Elige una operación (1-5): ")
            if opcion == "5":
                print("Saliendo de la calculadora...")
                break
            if opcion in ("1", "2", "3", "4"):
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
                if opcion == "1":
                    print(f"{num1} + {num2} = {num1 + num2}")
                elif opcion == "2":
                    print(f"{num1} - {num2} = {num1 - num2}")
                elif opcion == "3":
                    print(f"{num1} * {num2} = {num1 * num2}")
                elif opcion == "4":
                    if num2 != 0:
                        print(f"{num1} / {num2} = {num1 / num2}")
                    else:
                        print("Error: No se puede dividir por cero.")
            else:
                print("Opción inválida.")
    except ValueError:
        print("Error: Ingresa números válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def verificar_palindromo():
    """13. Verificar Palíndromo."""
    try:
        print("\n--- 13: Verificar Palíndromo ---")
        texto = input("Ingresa una palabra o frase: ").lower().replace(" ", "")
        if texto == texto[::-1]:
            print(f"'{texto}' es un palíndromo.")
        else:
            print(f"'{texto}' no es un palíndromo.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def sucesion_fibonacci():
    """14. Sucesión de Fibonacci."""
    try:
        print("\n--- 14: Sucesión de Fibonacci ---")
        limite = int(input("Ingresa el límite para la sucesión de Fibonacci: "))
        a, b = 0, 1
        fibonacci = []
        if limite >= 0:
            fibonacci.append(a)
        while b <= limite:
            fibonacci.append(b)
            a, b = b, a + b
        print(f"Sucesión de Fibonacci hasta {limite}: {fibonacci}")
    except ValueError:
        print("Error: Ingresa un número entero válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def calcular_factorial():
    """15. Calcular Factorial."""
    try:
        print("\n--- 15: Calcular Factorial ---")
        def factorial(n):
            if n < 0:
                return "Error: No se puede calcular el factorial de un número negativo."
            if n == 0 or n == 1:
                return 1
            return n * factorial(n - 1)

        numero = int(input("Ingresa un número para calcular su factorial: "))
        resultado = factorial(numero)
        print(f"El factorial de {numero} es: {resultado}")
    except ValueError:
        print("Error: Ingresa un número entero válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")


def N16_mayor_menor():
    """16. Encuentra el número mayor y menor en una lista."""
    try:
        print("\n--- 16: Mayor y Menor en Lista ---")
        numeros_str = input("Ingresa números separados por espacios: ")
        numeros = [float(num.strip()) for num in numeros_str.split()]
        
        if not numeros:
            print("No ingresaste números válidos.")
            return
        
        mayor = max(numeros)
        menor = min(numeros)
        
        print(f"Lista: {numeros}")
        print(f"Número mayor: {mayor}")
        print(f"Número menor: {menor}")
        
    except ValueError:
        print("Error: Ingresa solo números válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def N17_numero_primo():
    """17. Verifica si un número es primo."""
    try:
        print("\n--- 17: Verificar Número Primo ---")
        numero = int(input("Ingresa un número: "))
        
        if numero < 2:
            print(f"{numero} no es un número primo.")
            return
        
        es_primo = True
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                es_primo = False
                break
        
        if es_primo:
            print(f"{numero} es un número primo.")
        else:
            print(f"{numero} no es un número primo.")
            
    except ValueError:
        print("Error: Ingresa un número entero válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def N18_cajero_automatico():
    """18. Simula un cajero automático con saldo y retiros."""
    try:
        print("\n--- 18: Cajero Automático ---")
        saldo = 1000.0  # Saldo inicial
        
        while True:
            print(f"\nSaldo actual: ${saldo:.2f}")
            print("1. Consultar saldo")
            print("2. Depositar")
            print("3. Retirar")
            print("4. Salir")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                print(f"Tu saldo actual es: ${saldo:.2f}")
                
            elif opcion == "2":
                deposito = float(input("Cantidad a depositar: $"))
                if deposito > 0:
                    saldo += deposito
                    print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
                else:
                    print("La cantidad debe ser mayor a 0.")
                    
            elif opcion == "3":
                retiro = float(input("Cantidad a retirar: $"))
                if retiro > 0 and retiro <= saldo:
                    saldo -= retiro
                    print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
                elif retiro > saldo:
                    print("Fondos insuficientes.")
                else:
                    print("La cantidad debe ser mayor a 0.")
                    
            elif opcion == "4":
                print("Gracias por usar el cajero automático.")
                break
                
            else:
                print("Opción inválida.")
                
    except ValueError:
        print("Error: Ingresa un número válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def N19_diccionario_estudiantes():
    """19. Crea un diccionario de estudiantes con sus calificaciones."""
    try:
        print("\n--- 19: Diccionario de Estudiantes ---")
        estudiantes = {}
        
        while True:
            print("\n1. Agregar estudiante")
            print("2. Ver todos los estudiantes")
            print("3. Buscar estudiante")
            print("4. Calcular promedio de un estudiante")
            print("5. Salir")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                nombre = input("Nombre del estudiante: ").strip()
                calificaciones_str = input("Calificaciones separadas por espacios: ")
                calificaciones = [float(cal.strip()) for cal in calificaciones_str.split()]
                estudiantes[nombre] = calificaciones
                print(f"Estudiante {nombre} agregado exitosamente.")
                
            elif opcion == "2":
                if estudiantes:
                    print("\nEstudiantes registrados:")
                    for nombre, calificaciones in estudiantes.items():
                        print(f"{nombre}: {calificaciones}")
                else:
                    print("No hay estudiantes registrados.")
                    
            elif opcion == "3":
                nombre = input("Nombre del estudiante a buscar: ").strip()
                if nombre in estudiantes:
                    print(f"{nombre}: {estudiantes[nombre]}")
                else:
                    print("Estudiante no encontrado.")
                    
            elif opcion == "4":
                nombre = input("Nombre del estudiante: ").strip()
                if nombre in estudiantes:
                    if estudiantes[nombre]:
                        promedio = sum(estudiantes[nombre]) / len(estudiantes[nombre])
                        print(f"Promedio de {nombre}: {promedio:.2f}")
                    else:
                        print(f"El estudiante {nombre} no tiene calificaciones registradas.")
                else:
                    print("Estudiante no encontrado.")
                    
            elif opcion == "5":
                break
                
            else:
                print("Opción inválida.")
                
    except ValueError:
        print("Error: Ingresa calificaciones válidas.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def N20_tienda_productos():
    """20. Simula una tienda que permita agregar productos y calcular el total."""
    try:
        print("\n--- 20: Tienda Virtual ---")
        productos = []
        
        while True:
            print("\n1. Agregar producto")
            print("2. Ver carrito")
            print("3. Calcular total")
            print("4. Vaciar carrito")
            print("5. Salir")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                nombre = input("Nombre del producto: ").strip()
                precio = float(input("Precio del producto: $"))
                cantidad = int(input("Cantidad: "))
                
                if precio <= 0 or cantidad <= 0:
                    print("El precio y la cantidad deben ser mayores a 0.")
                    continue

                productos.append({
                    'nombre': nombre,
                    'precio': precio,
                    'cantidad': cantidad
                })
                print(f"Producto '{nombre}' agregado al carrito.")
                
            elif opcion == "2":
                if productos:
                    print("\nCarrito de compras:")
                    for i, producto in enumerate(productos, 1):
                        print(f"{i}. {producto['nombre']} - ${producto['precio']:.2f} x {producto['cantidad']}")
                else:
                    print("El carrito está vacío.")
                    
            elif opcion == "3":
                if productos:
                    total = sum(p['precio'] * p['cantidad'] for p in productos)
                    print(f"\nTotal a pagar: ${total:.2f}")
                else:
                    print("El carrito está vacío.")
                    
            elif opcion == "4":
                productos.clear()
                print("Carrito vaciado.")
                
            elif opcion == "5":
                break
                
            else:
                print("Opción inválida.")
                
    except ValueError:
        print("Error: Ingresa valores numéricos válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def N21_contar_vocales():
    """21. Lee una frase y muestra cuántas vocales tiene."""
    try:
        print("\n--- 21: Contador de Vocales ---")
        frase = input("Ingresa una frase: ").lower()
        
        vocales = "aeiouáéíóúü"
        contador = 0
        detalle_vocales = {}
        
        for char in frase:
            if char in vocales:
                contador += 1
                detalle_vocales[char] = detalle_vocales.get(char, 0) + 1
        
        print(f"La frase tiene {contador} vocales en total.")
        print("Detalle por vocal:")
        for vocal, cantidad in detalle_vocales.items():
            print(f"  {vocal}: {cantidad}")
            
    except Exception as e:
        print(f"Error inesperado: {e}")

def N22_eliminar_duplicados():
    """22. Elimina los duplicados de una lista de números."""
    try:
        print("\n--- 22: Eliminar Duplicados ---")
        numeros_str = input("Ingresa números separados por espacios: ")
        numeros = [float(num.strip()) for num in numeros_str.split()]
        
        print(f"Lista original: {numeros}")
        
        sin_duplicados_set = list(set(numeros))
        print(f"Sin duplicados (Ordenado por valor): {sorted(sin_duplicados_set)}") 
        
        sin_duplicados_orden = []
        for num in numeros:
            if num not in sin_duplicados_orden:
                sin_duplicados_orden.append(num)
        
        print(f"Sin duplicados (preservando orden original): {sin_duplicados_orden}")
        
    except ValueError:
        print("Error: Ingresa solo números válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def N23_validar_contraseña():
    """23. Valida una contraseña con reglas mínimas (longitud, número, mayúscula)."""
    try:
        print("\n--- 23: Validador de Contraseña ---")
        contraseña = input("Ingresa una contraseña: ")
        
        criterios = {
            'longitud': len(contraseña) >= 8,
            'mayuscula': any(c.isupper() for c in contraseña),
            'minuscula': any(c.islower() for c in contraseña),
            'numero': any(c.isdigit() for c in contraseña),
            'caracter_especial': any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in contraseña)
        }
        
        print("\nValidación de contraseña:")
        print(f"✓ Longitud mínima 8 caracteres: {'SÍ' if criterios['longitud'] else 'NO'}")
        print(f"✓ Contiene mayúscula: {'SÍ' if criterios['mayuscula'] else 'NO'}")
        print(f"✓ Contiene minúscula: {'SÍ' if criterios['minuscula'] else 'NO'}")
        print(f"✓ Contiene número: {'SÍ' if criterios['numero'] else 'NO'}")
        print(f"✓ Contiene carácter especial: {'SÍ' if criterios['caracter_especial'] else 'NO'}")
        
        if all(criterios.values()):
            print("\n🎉 ¡Contraseña SEGURA!")
        else:
            print("\n⚠️  Contraseña NO cumple todos los criterios.")
            
    except Exception as e:
        print(f"Error inesperado: {e}")

def N24_agenda_contactos():
    """24. Crea una agenda de contactos que permita agregar y buscar por nombre."""
    try:
        print("\n--- 24: Agenda de Contactos ---")
        contactos = {}
        
        while True:
            print("\n1. Agregar contacto")
            print("2. Buscar contacto")
            print("3. Mostrar todos los contactos")
            print("4. Eliminar contacto")
            print("5. Salir")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                nombre = input("Nombre del contacto: ").strip()
                if not nombre:
                    print("El nombre no puede estar vacío.")
                    continue
                telefono = input("Teléfono: ").strip()
                email = input("Email (opcional): ").strip()
                
                contactos[nombre] = {
                    'telefono': telefono if telefono else "No especificado",
                    'email': email if email else "No especificado"
                }
                print(f"Contacto '{nombre}' agregado exitosamente.")
                
            elif opcion == "2":
                nombre = input("Nombre del contacto a buscar: ").strip()
                if nombre in contactos:
                    print(f"\nContacto encontrado:")
                    print(f"Nombre: {nombre}")
                    print(f"Teléfono: {contactos[nombre]['telefono']}")
                    print(f"Email: {contactos[nombre]['email']}")
                else:
                    print("Contacto no encontrado.")
                    
            elif opcion == "3":
                if contactos:
                    print("\nTodos los contactos:")
                    for nombre, info in contactos.items():
                        print(f"Nombre: {nombre}, Teléfono: {info['telefono']}, Email: {info['email']}")
                else:
                    print("No hay contactos registrados.")
                    
            elif opcion == "4":
                nombre = input("Nombre del contacto a eliminar: ").strip()
                if nombre in contactos:
                    del contactos[nombre]
                    print(f"Contacto '{nombre}' eliminado.")
                else:
                    print("Contacto no encontrado.")
                    
            elif opcion == "5":
                break
                
            else:
                print("Opción inválida.")
                
    except Exception as e:
        print(f"Error inesperado: {e}")

def N25_menu_opciones():
    """25. Simula un menú de opciones (saludar, calcular, salir)."""
    try:
        print("\n--- 25: Menú de Opciones ---")
        
        def saludar():
            nombre = input("¿Cómo te llamas? ")
            print(f"¡Hola, {nombre}! Es un placer conocerte.")
        
        def calcular():
            try:
                a = float(input("Ingresa el primer número: "))
                operador = input("Ingresa el operador (+, -, *, /): ")
                b = float(input("Ingresa el segundo número: "))
                
                if operador == "+":
                    resultado = a + b
                elif operador == "-":
                    resultado = a - b
                elif operador == "*":
                    resultado = a * b
                elif operador == "/":
                    if b != 0:
                        resultado = a / b
                    else:
                        print("Error: División por cero.")
                        return
                else:
                    print("Operador inválido.")
                    return
                
                print(f"Resultado: {a} {operador} {b} = {resultado}")
                
            except ValueError:
                print("Error: Ingresa números válidos.")
        
        while True:
            print("\n1. Saludar")
            print("2. Calcular")
            print("3. Salir del submenú")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                saludar()
            elif opcion == "2":
                calcular()
            elif opcion == "3":
                break
            else:
                print("Opción inválida.")
                
    except Exception as e:
        print(f"Error inesperado: {e}")

def N26_clase_persona():
    """26. Crea una clase Persona con atributos nombre y edad, e imprime sus datos."""
    try:
        print("\n--- 26: Clase Persona ---")
        
        class Persona:
            def __init__(self, nombre, edad):
                self.nombre = nombre
                self.edad = edad
            
            def mostrar_datos(self):
                print(f"Nombre: {self.nombre}")
                print(f"Edad: {self.edad} años")
            
            def saludar(self):
                print(f"¡Hola! Mi nombre es {self.nombre} y tengo {self.edad} años")

        print("=== Crear una Persona ===")
        nombre = input("Ingresa el nombre: ")
        edad = int(input("Ingresa la edad: "))

        persona = Persona(nombre, edad)

        print("\n--- Datos de la persona ---")
        persona.mostrar_datos()

        print("\n--- Saludo ---")
        persona.saludar()
        
    except ValueError:
        print("Error: Ingresa una edad válida.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def N27_cuenta_bancaria():
    """27. Implementa una clase CuentaBancaria con métodos para depositar y retirar."""
    try:
        print("\n--- 27: Cuenta Bancaria ---")
        
        class CuentaBancaria:
            def __init__(self, titular, saldo_inicial=0):
                self.titular = titular
                self.saldo = saldo_inicial
                self.historial = []
            
            def depositar(self, cantidad):
                if cantidad > 0:
                    self.saldo += cantidad                    
                    self.historial.append(f"Depósito: +${cantidad:.2f}")
                    print(f"Depósito exitoso. Nuevo saldo: ${self.saldo:.2f}")
                else:
                    print("La cantidad debe ser mayor a 0.")
            
            def retirar(self, cantidad):
                if cantidad > 0:
                    if cantidad <= self.saldo:
                        self.saldo -= cantidad
                        self.historial.append(f"Retiro: -${cantidad:.2f}")
                        print(f"Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}")
                    else:
                        print("Fondos insuficientes.")
                else:
                    print("La cantidad debe ser mayor a 0.")
            
            def consultar_saldo(self):
                print(f"Saldo actual: ${self.saldo:.2f}")
                return self.saldo
            
            def mostrar_historial(self):
                print(f"\nHistorial de transacciones de {self.titular}:")
                if self.historial:
                    for transaccion in self.historial:
                        print(f"  {transaccion}")
                else:
                    print("  No hay transacciones.")
        
        titular = input("Nombre del titular: ").strip()
        saldo_inicial = float(input("Saldo inicial: $"))
        
        cuenta = CuentaBancaria(titular, saldo_inicial)
        
        while True:
            print(f"\n--- Cuenta de {titular} ---")
            print("1. Consultar saldo")
            print("2. Depositar")
            print("3. Retirar")
            print("4. Ver historial")
            print("5. Salir del submenú")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                cuenta.consultar_saldo()
            elif opcion == "2":
                cantidad = float(input("Cantidad a depositar: $"))
                cuenta.depositar(cantidad)
            elif opcion == "3":
                cantidad = float(input("Cantidad a retirar: $"))
                cuenta.retirar(cantidad)
            elif opcion == "4":
                cuenta.mostrar_historial()
            elif opcion == "5":
                break
            else:
                print("Opción inválida.")
                
    except ValueError:
        print("Error: Ingresa valores numéricos válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def N28_producto_impuestos():
    """28. Diseña una clase Producto que calcule el total con impuestos."""
    try:
        print("\n--- 28: Producto con Impuestos ---")
        
        class Producto:
            def __init__(self, nombre, precio, impuesto_porcentaje=16):
                self.nombre = nombre
                self.precio = precio  
                self.impuesto_porcentaje = impuesto_porcentaje
                self.descuento_porcentaje = 0  
    
            def calcular_impuesto(self):
                return self.precio * (self.impuesto_porcentaje / 100)
    
            def calcular_descuento(self):
                return self.precio * (self.descuento_porcentaje / 100)
    
            def calcular_total(self):
                precio_con_impuesto = self.precio + self.calcular_impuesto()
                return precio_con_impuesto - self.calcular_descuento()
    
            def mostrar_detalle(self):
                print(f"\nDetalle del producto:")
                print(f"Nombre: {self.nombre}")
                print(f"Precio base: ${self.precio:.2f}")
                print(f"Impuesto ({self.impuesto_porcentaje}%): ${self.calcular_impuesto():.2f}")
                if self.descuento_porcentaje > 0:
                    print(f"Descuento ({self.descuento_porcentaje}%): -${self.calcular_descuento():.2f}")
                print(f"Total: ${self.calcular_total():.2f}")
    
            def aplicar_descuento(self, descuento_porcentaje):
                if 0 <= descuento_porcentaje <= 100:
                    self.descuento_porcentaje = descuento_porcentaje
                    print(f"Descuento del {descuento_porcentaje}% aplicado.")
                else:
                    print("El porcentaje de descuento debe estar entre 0 y 100.")
    
            def quitar_descuento(self):
                self.descuento_porcentaje = 0
                print("Descuento removido.")
            
            def cambiar_impuesto(self, nuevo_impuesto):
                if nuevo_impuesto >= 0:
                    self.impuesto_porcentaje = nuevo_impuesto
                    print(f"Impuesto actualizado a {nuevo_impuesto}%.")
                else:
                    print("El porcentaje de impuesto no puede ser negativo.")

        print("=== Crear un Producto ===")
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del producto: $"))
        impuesto_input = input("Porcentaje de impuesto (Enter para 16%): ")
        impuesto = float(impuesto_input) if impuesto_input else 16.0

        producto = Producto(nombre, precio, impuesto)

        while True:
            print(f"\n--- Producto: {nombre} ---")
            print("1. Mostrar detalle")
            print("2. Aplicar descuento")
            print("3. Quitar descuento")
            print("4. Cambiar impuesto")
            print("5. Salir del submenú")
    
            opcion = input("Selecciona una opción: ")
    
            if opcion == "1":
                producto.mostrar_detalle()
            elif opcion == "2":
                descuento = float(input("Porcentaje de descuento: "))
                producto.aplicar_descuento(descuento)
            elif opcion == "3":
                producto.quitar_descuento()
            elif opcion == "4":
                nuevo_impuesto = float(input("Nuevo porcentaje de impuesto: "))
                producto.cambiar_impuesto(nuevo_impuesto)
            elif opcion == "5":
                break
            else:
                print("Opción inválida.")
                
    except ValueError:
        print("Error: Ingresa valores numéricos válidos.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def N29_rectangulo():
    """29. Crea una clase Rectángulo que calcule el área y el perímetro."""
    try:
        print("\n--- 29: Clase Rectángulo ---")
        
        class Rectangulo:
            def __init__(self, largo, ancho):
                if largo <= 0 or ancho <= 0:
                    raise ValueError("Largo y ancho deben ser valores positivos.")
                self.largo = largo
                self.ancho = ancho
            
            def calcular_area(self):
                return self.largo * self.ancho
            
            def calcular_perimetro(self):
                return 2 * (self.largo + self.ancho)
            
            def es_cuadrado(self):
                return self.largo == self.ancho
            
            def mostrar_info(self):
                print(f"\nInformación del rectángulo:")
                print(f"Largo: {self.largo}")
                print(f"Ancho: {self.ancho}")
                print(f"Área: {self.calcular_area():.2f}")
                print(f"Perímetro: {self.calcular_perimetro():.2f}")
                print(f"Es cuadrado: {'Sí' if self.es_cuadrado() else 'No'}")
            
            def cambiar_dimensiones(self, nuevo_largo, nuevo_ancho):
                if nuevo_largo <= 0 or nuevo_ancho <= 0:
                    print("Error: Largo y ancho deben ser valores positivos.")
                    return
                self.largo = nuevo_largo
                self.ancho = nuevo_ancho
                print(f"Dimensiones actualizadas: {self.largo} x {self.ancho}")
        
        largo = float(input("Ingresa el largo del rectángulo: "))
        ancho = float(input("Ingresa el ancho del rectángulo: "))
        
        rectangulo = Rectangulo(largo, ancho)
        
        while True:
            print(f"\n--- Rectángulo {rectangulo.largo} x {rectangulo.ancho} ---")
            print("1. Mostrar información")
            print("2. Cambiar dimensiones")
            print("3. Salir del submenú")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                rectangulo.mostrar_info()
            elif opcion == "2":
                nuevo_largo = float(input("Nuevo largo: "))
                nuevo_ancho = float(input("Nuevo ancho: "))
                rectangulo.cambiar_dimensiones(nuevo_largo, nuevo_ancho)
            elif opcion == "3":
                break
            else:
                print("Opción inválida.")
                
    except ValueError as ve:
        print(f"Error: {ve}. Ingresa valores numéricos válidos y positivos.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def N30_clase_libro():
    """30. Implementa una clase Libro con atributos título, autor y año."""
    try:
        print("\n--- 30: Clase Libro ---")
        
        class Libro:
            def __init__(self, titulo, autor, año):
                self.titulo = titulo
                self.autor = autor
                self.año = año
                self.disponible = True
            
            def mostrar_info(self):
                print(f"\nInformación del libro:")
                print(f"Título: {self.titulo}")
                print(f"Autor: {self.autor}")
                print(f"Año: {self.año}")
                print(f"Disponible: {'Sí' if self.disponible else 'No'}")
            
            def prestar(self):
                if self.disponible:
                    self.disponible = False
                    print(f"El libro '{self.titulo}' ha sido prestado.")
                else:
                    print(f"El libro '{self.titulo}' no está disponible.")
            
            def devolver(self):
                if not self.disponible:
                    self.disponible = True
                    print(f"El libro '{self.titulo}' ha sido devuelto.")
                else:
                    print(f"El libro '{self.titulo}' ya está disponible.")
            
            def antiguedad(self):
                año_actual = 2025
                return año_actual - self.año
            
            def es_clasico(self):
                return self.antiguedad() > 50
        
        # Crear libro
        titulo = input("Título del libro: ").strip()
        autor = input("Autor del libro: ").strip()
        año = int(input("Año de publicación: "))
        
        libro = Libro(titulo, autor, año)
        
        while True:
            print(f"\n--- Libro: {libro.titulo} ---")
            print("1. Mostrar información")
            print("2. Prestar libro")
            print("3. Devolver libro")
            print("4. Verificar si es clásico")
            print("5. Salir")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                libro.mostrar_info()
                print(f"Antigüedad: {libro.antiguedad()} años")
            elif opcion == "2":
                libro.prestar()
            elif opcion == "3":
                libro.devolver()
            elif opcion == "4":
                if libro.es_clasico():
                    print(f"'{libro.titulo}' es un libro clásico ({libro.antiguedad()} años).")
                else:
                    print(f"'{libro.titulo}' no es considerado un clásico aún.")
            elif opcion == "5":
                break
            else:
                print("Opción inválida.")
                
    except ValueError:
        print("Error: Ingresa un año válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def N31_clase_vehiculo():
    """31. Diseña una clase Vehículo con subclases Auto y Moto."""
    try:
        print("\n--- 31: Clase Vehículo (Auto y Moto) ---")
        class Vehiculo:
            def __init__(self, marca, modelo):
                self.marca = marca
                self.modelo = modelo

            def mostrar_info(self):
                print(f"Marca: {self.marca}")
                print(f"Modelo: {self.modelo}")

        class Auto(Vehiculo):
            def tipo(self):
                return "Auto"

        class Moto(Vehiculo):
            def tipo(self):
                return "Moto"

        print("\n--- Crear un Auto ---")
        marca_auto = input("Marca del auto: ")
        modelo_auto = input("Modelo del auto: ")
        auto1 = Auto(marca_auto, modelo_auto)
        print("\nInformación del Auto:")
        auto1.mostrar_info()
        print("Tipo:", auto1.tipo())

        print("\n--- Crear una Moto ---")
        marca_moto = input("Marca de la moto: ")
        modelo_moto = input("Modelo de la moto: ")
        moto1 = Moto(marca_moto, modelo_moto)
        print("\nInformación de la Moto:")
        moto1.mostrar_info()
        print("Tipo:", moto1.tipo())
    except Exception as e:
        print(f"Error inesperado: {e}")

def N32_clase_estudiante():
    """32. Crea una clase Estudiante con método para calcular promedio de notas."""
    try:
        print("\n--- 32: Clase Estudiante ---")
        class Estudiante:
            def __init__(self, nombre, notas):
                self.nombre = nombre
                self.notas = notas  
                
            def calcular_promedio(self):
                if not self.notas:
                    return 0
                return sum(self.notas) / len(self.notas)

            def mostrar_info(self):
                print(f"Estudiante: {self.nombre}")
                print(f"Notas: {self.notas}")
                print(f"Promedio: {self.calcular_promedio():.2f}")

        nombre_est = input("Nombre del estudiante: ")
        notas_str = input("Ingresa las notas separadas por espacios (ej: 85 90 78): ")
        notas = [float(n.strip()) for n in notas_str.split()]
        
        est1 = Estudiante(nombre_est, notas)
        print("\nInformación del estudiante:")
        est1.mostrar_info()
    except ValueError:
        print("Error: Ingresa notas válidas (números).")
    except Exception as e:
        print(f"Error inesperado: {e}")

def N33_clase_tienda():
    """33. Implementa una clase Tienda que almacene productos en un diccionario."""
    try:
        print("\n--- 33: Clase Tienda ---")
        class Tienda:
            def __init__(self):
                self.productos = {}

            def agregar_producto(self, nombre, precio):
                if precio <= 0:
                    print("Error: El precio debe ser mayor a 0.")
                    return
                self.productos[nombre] = precio
                print(f"Producto '{nombre}' agregado con precio RD${precio}.")

            def eliminar_producto(self, nombre):
                if nombre in self.productos:
                    del self.productos[nombre]
                    print(f"Producto '{nombre}' eliminado.")
                else:
                    print(f"El producto '{nombre}' no existe.")

            def mostrar_productos(self):
                if not self.productos:
                    print("La tienda no tiene productos.")
                else:
                    print("Productos disponibles:")
                    for nombre, precio in self.productos.items():
                        print(f"- {nombre}: RD${precio}")

            def obtener_precio(self, nombre):
                return self.productos.get(nombre, "Producto no encontrado.")

        tienda = Tienda()
        
        while True:
            print("\n--- Gestión de Tienda ---")
            print("1. Agregar producto")
            print("2. Eliminar producto")
            print("3. Mostrar productos")
            print("4. Obtener precio de un producto")
            print("5. Salir del submenú")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                nombre = input("Nombre del producto a agregar: ")
                precio = float(input("Precio del producto: RD$"))
                tienda.agregar_producto(nombre, precio)
            elif opcion == "2":
                nombre = input("Nombre del producto a eliminar: ")
                tienda.eliminar_producto(nombre)
            elif opcion == "3":
                tienda.mostrar_productos()
            elif opcion == "4":
                nombre = input("Nombre del producto para obtener precio: ")
                precio = tienda.obtener_precio(nombre)
                print(f"Precio de {nombre}: {precio}")
            elif opcion == "5":
                break
            else:
                print("Opción inválida.")
    except ValueError:
        print("Error: Ingresa un precio válido (número).")
    except Exception as e:
        print(f"Error inesperado: {e}")

def N34_clase_empleado():
    """34. Crea una clase Empleado y calcula su salario neto con descuentos."""
    try:
        print("\n--- 34: Clase Empleado ---")
        class Empleado:
            def __init__(self, nombre, salario_bruto, descuento):
                self.nombre = nombre
                self.salario_bruto = salario_bruto
                self.descuento = descuento 

            def calcular_salario_neto(self):
                descuento_monto = self.salario_bruto * (self.descuento / 100)
                salario_neto = self.salario_bruto - descuento_monto
                return salario_neto

            def mostrar_info(self):
                print(f"Empleado: {self.nombre}")
                print(f"Salario bruto: RD${self.salario_bruto}")
                print(f"Descuento aplicado: {self.descuento}%")
                print(f"Salario neto: RD${self.calcular_salario_neto():.2f}")

        nombre_emp = input("Nombre del empleado: ")
        salario_bruto = float(input("Salario bruto: RD$"))
        descuento_porc = float(input("Porcentaje de descuento (ej: 12 para 12%): "))
        
        if salario_bruto < 0 or not (0 <= descuento_porc <= 100):
            print("Error: Salario bruto no puede ser negativo y el descuento debe ser entre 0 y 100.")
            return

        empleado1 = Empleado(nombre_emp, salario_bruto, descuento_porc)
        print("\nInformación del empleado:")
        empleado1.mostrar_info()
    except ValueError:
        print("Error: Ingresa valores numéricos válidos para salario y descuento.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def N35_clase_factura():
    """35. Diseña una clase Factura que permita registrar productos y calcular el total."""
    try:
        print("\n--- 35: Clase Factura ---")
        class Factura:
            def __init__(self):
                self.productos = []

            def agregar_producto(self, nombre, precio, cantidad):
                if precio <= 0 or cantidad <= 0:
                    print("Error: Precio y cantidad deben ser mayores a 0.")
                    return
                producto = {
                    "nombre": nombre,
                    "precio": precio,
                    "cantidad": cantidad
                }
                self.productos.append(producto)
                print(f"'{nombre}' x {cantidad} agregado a la factura.")

            def mostrar_productos(self):
                if not self.productos:
                    print("La factura no tiene productos.")
                    return
                print("Productos en la factura:")
                for producto in self.productos:
                    print(f"- {producto['nombre']}: RD${producto['precio']} x {producto['cantidad']}")

            def calcular_total(self):
                total = sum(p['precio'] * p['cantidad'] for p in self.productos)
                return total

        factura = Factura()
        
        while True:
            print("\n--- Gestión de Factura ---")
            print("1. Agregar producto a la factura")
            print("2. Mostrar productos en la factura")
            print("3. Calcular total de la factura")
            print("4. Salir del submenú")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio unitario: RD$"))
                cantidad = int(input("Cantidad: "))
                factura.agregar_producto(nombre, precio, cantidad)
            elif opcion == "2":
                factura.mostrar_productos()
            elif opcion == "3":
                total = factura.calcular_total()
                print(f"Total a pagar: RD$ {total:.2f}")
            elif opcion == "4":
                break
            else:
                print("Opción inválida.")
    except ValueError:
        print("Error: Ingresa valores numéricos válidos para precio y cantidad.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def N36_clase_figura():
    """36. Programa una clase Figura con método calcular_area y subclases Círculo y Cuadrado."""
    try:
        print("\n--- 36: Clase Figura (Círculo y Cuadrado) ---")
        class Figura:
            def calcular_area(self):
                pass

        class Circulo(Figura):
            def __init__(self, radio):
                if radio <= 0:
                    raise ValueError("El radio debe ser un valor positivo.")
                self.radio = radio

            def calcular_area(self):
                return math.pi * self.radio ** 2

        class Cuadrado(Figura):
            def __init__(self, lado):
                if lado <= 0:
                    raise ValueError("El lado debe ser un valor positivo.")
                self.lado = lado

            def calcular_area(self):
                return self.lado ** 2

        print("\n--- Calcular Área de Círculo ---")
        radio = float(input("Ingresa el radio del círculo: "))
        c = Circulo(radio)
        print(f"Área del círculo: {c.calcular_area():.2f}")

        print("\n--- Calcular Área de Cuadrado ---")
        lado = float(input("Ingresa el lado del cuadrado: "))
        q = Cuadrado(lado)
        print(f"Área del cuadrado: {q.calcular_area():.2f}")
    except ValueError as ve:
        print(f"Error: {ve}. Ingresa valores numéricos válidos y positivos.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def N37_clase_agenda():
    """37. Crea una clase Agenda con métodos para agregar, eliminar y buscar contactos."""
    try:
        print("\n--- 37: Clase Agenda ---")
        class Agenda:
            def __init__(self):
                self.contactos = {}

            def agregar(self, nombre, telefono):
                if not nombre or not telefono:
                    print("Error: Nombre y teléfono no pueden estar vacíos.")
                    return
                self.contactos[nombre] = telefono
                print(f"Contacto '{nombre}' agregado.")

            def eliminar(self, nombre):
                if nombre in self.contactos:
                    del self.contactos[nombre]
                    print(f"Contacto '{nombre}' eliminado.")
                else:
                    print(f"El contacto '{nombre}' no existe.")

            def buscar(self, nombre):
                return self.contactos.get(nombre, "No encontrado")
            
            def mostrar_todos(self):
                if not self.contactos:
                    print("La agenda está vacía.")
                    return
                print("Contactos en la agenda:")
                for nombre, telefono in self.contactos.items():
                    print(f"- {nombre}: {telefono}")

        agenda = Agenda()
        
        while True:
            print("\n--- Gestión de Agenda ---")
            print("1. Agregar contacto")
            print("2. Eliminar contacto")
            print("3. Buscar contacto")
            print("4. Mostrar todos los contactos")
            print("5. Salir del submenú")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                nombre = input("Nombre del contacto: ")
                telefono = input("Teléfono del contacto: ")
                agenda.agregar(nombre, telefono)
            elif opcion == "2":
                nombre = input("Nombre del contacto a eliminar: ")
                agenda.eliminar(nombre)
            elif opcion == "3":
                nombre = input("Nombre del contacto a buscar: ")
                telefono = agenda.buscar(nombre)
                print(f"Teléfono de {nombre}: {telefono}")
            elif opcion == "4":
                agenda.mostrar_todos()
            elif opcion == "5":
                break
            else:
                print("Opción inválida.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def N38_clase_animal():
    """38. Diseña una clase Animal con subclases Perro y Gato que implementen el método hacer_sonido()."""
    try:
        print("\n--- 38: Clase Animal (Perro y Gato) ---")
        class Animal:
            def hacer_sonido(self):
                pass

        class Perro(Animal):
            def hacer_sonido(self):
                return "Guau"

        class Gato(Animal):
            def hacer_sonido(self):
                return "Miau"

        perro = Perro()
        gato = Gato()

        print(f"El perro hace: {perro.hacer_sonido()}")
        print(f"El gato hace: {gato.hacer_sonido()}")
    except Exception as e:
        print(f"Error inesperado: {e}")

def N39_clase_juego():
    """39. Crea una clase Juego con un método que indique si el jugador ha ganado."""
    try:
        print("\n--- 39: Clase Juego ---")
        class Juego:
            def __init__(self, estado_objetivo):
                self.estado_objetivo = estado_objetivo 
                self.estado_actual = None

            def actualizar_estado(self, nuevo_estado):
                self.estado_actual = nuevo_estado
                print(f"Estado actual del juego: {self.estado_actual}")

            def ha_ganado(self):
                return self.estado_actual == self.estado_objetivo

        estado_ganar = input("Define el estado para ganar (ej: 'victoria', 'ganado'): ")
        juego = Juego(estado_objetivo=estado_ganar)
        
        while True:
            print("\n--- Gestión de Juego ---")
            print("1. Actualizar estado del juego")
            print("2. Verificar si ha ganado")
            print("3. Salir del submenú")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                nuevo_estado = input("Ingresa el nuevo estado del juego: ")
                juego.actualizar_estado(nuevo_estado)
            elif opcion == "2":
                if juego.ha_ganado():
                    print("¡Felicidades! El jugador ha ganado.")
                else:
                    print("El jugador aún no ha ganado.")
            elif opcion == "3":
                break
            else:
                print("Opción inválida.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def N40_clase_sensor_temperatura():
    """40. Implementa una clase SensorTemperatura que registre lecturas y calcule la media."""
    try:
        print("\n--- 40: Clase SensorTemperatura ---")
        class SensorTemperatura:
            def __init__(self):
                self.lecturas = []

            def registrar(self, temperatura):
                self.lecturas.append(temperatura)
                print(f"Temperatura {temperatura}°C registrada.")

            def calcular_media(self):
                if not self.lecturas:
                    return 0 
                return sum(self.lecturas) / len(self.lecturas)

        sensor = SensorTemperatura()
        
        while True:
            print("\n--- Gestión de Sensor de Temperatura ---")
            print("1. Registrar temperatura")
            print("2. Calcular media de temperaturas")
            print("3. Salir del submenú")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == "1":
                temp = float(input("Ingresa la temperatura a registrar (°C): "))
                sensor.registrar(temp)
            elif opcion == "2":
                media = sensor.calcular_media()
                print(f"Media de temperatura: {media:.2f} °C")
            elif opcion == "3":
                break
            else:
                print("Opción inválida.")
    except ValueError:
        print("Error: Ingresa un valor numérico válido para la temperatura.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def preguntar_continuar():
    """Pregunta al usuario si desea continuar con el menú principal."""
    while True:
        try:
            respuesta = input("\n¿Deseas continuar con el menú principal? (s/n): ").lower().strip()
            if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
                return True
            elif respuesta in ['n', 'no']:
                return False
            else:
                print("Por favor, ingresa 's' para sí o 'n' para no.")
        except Exception:
            print("Error al leer la respuesta. Por favor, intenta nuevamente.")

def menu_principal():
    """Menú principal para ejecutar todos los proyectos."""
    proyectos = {
        1: saludo_personalizado,
        2: convertir_kilometros_a_millas,
        3: determinar_par_o_impar,
        4: calcular_area_triangulo,
        5: tabla_multiplicar,
        6: suma_numeros_pares,
        7: adivina_numero,
        8: promedio_numeros,
        9: contar_palabra_en_frase,
        10: ordenar_numeros,
        11: convertir_grados,
        12: calculadora_basica,
        13: verificar_palindromo,
        14: sucesion_fibonacci,
        15: calcular_factorial,
        16: N16_mayor_menor,
        17: N17_numero_primo,
        18: N18_cajero_automatico,
        19: N19_diccionario_estudiantes,
        20: N20_tienda_productos,
        21: N21_contar_vocales,
        22: N22_eliminar_duplicados,
        23: N23_validar_contraseña,
        24: N24_agenda_contactos,
        25: N25_menu_opciones,
        26: N26_clase_persona,
        27: N27_cuenta_bancaria,
        28: N28_producto_impuestos,
        29: N29_rectangulo,
        30: N30_clase_libro, 
        31: N31_clase_vehiculo,
        32: N32_clase_estudiante,
        33: N33_clase_tienda,
        34: N34_clase_empleado,
        35: N35_clase_factura,
        36: N36_clase_figura,
        37: N37_clase_agenda,
        38: N38_clase_animal,
        39: N39_clase_juego,
        40: N40_clase_sensor_temperatura
    }
    
    while True:
        print("\n" + "="*50)
        print("                 MENÚ PRINCIPAL")
        print("="*50)
        print(" 1. Saludo Personalizado")
        print(" 2. Convertir Kilómetros a Millas")
        print(" 3. Determinar Par o Impar")
        print(" 4. Calcular Área de un Triángulo")
        print(" 5. Tabla de Multiplicar")
        print(" 6. Suma de Números Pares del 1 al 100")
        print(" 7. Adivina el Número")
        print(" 8. Promedio de Números")
        print(" 9. Contar Palabra en Frase")
        print("10. Ordenar Números")
        print("11. Convertir Celsius a Fahrenheit y Viceversa")
        print("12. Calculadora Básica")
        print("13. Verificar Palíndromo")
        print("14. Sucesión de Fibonacci")
        print("15. Calcular Factorial")
        print("16. Encuentra el número mayor y menor en una lista")
        print("17. Verifica si un número es primo")
        print("18. Simula un cajero automático con saldo y retiros")
        print("19. Crea un diccionario de estudiantes con sus calificaciones")
        print("20. Simula una tienda que permita agregar productos y calcular el total")
        print("21. Lee una frase y muestra cuántas vocales tiene")
        print("22. Elimina los duplicados de una lista de números")
        print("23. Valida una contraseña con reglas mínimas")
        print("24. Crea una agenda de contactos que permita agregar y buscar por nombre")
        print("25. Simula un menú de opciones (saludar, calcular, salir)")
        print("26. Crea una clase Persona con atributos nombre y edad")
        print("27. Implementa una clase CuentaBancaria con métodos para depositar y retirar")
        print("28. Diseña una clase Producto que calcule el total con impuestos")
        print("29. Crea una clase Rectángulo que calcule el área y el perímetro")
        print("30. Implementa una clase Libro con atributos título, autor y año")
        print("31. Diseña una clase Vehículo con subclases Auto y Moto")
        print("32. Crea una clase Estudiante con método para calcular promedio de notas")
        print("33. Implementa una clase Tienda que almacene productos en un diccionario")
        print("34. Crea una clase Empleado y calcula su salario neto con descuentos")
        print("35. Diseña una clase Factura que permita registrar productos y calcular el total")
        print("36. Programa una clase Figura con método calcular_area y subclases Círculo y Cuadrado")
        print("37. Crea una clase Agenda con métodos para agregar, eliminar y buscar contactos")
        print("38. Diseña una clase Animal con subclases Perro y Gato que implementen el método hacer_sonido()")
        print("39. Crea una clase Juego con un método que indique si el jugador ha ganado")
        print("40. Implementa una clase SensorTemperatura que registre lecturas y calcule la media")
        print("0. Salir del programa")
        print("="*50)
        
        try:
            opcion = int(input("Selecciona una opción (0-40): "))
            
            if opcion == 0:
                print("¡Gracias por usar nuestros servicios! ¡Hasta luego!")
                break
            elif opcion in proyectos:
                print(f"\n🚀 Ejecutando opción {opcion}...")
                proyectos[opcion]()
                
                if opcion != 0 and not preguntar_continuar():
                    print("¡Gracias por usar nuestros servicios! ¡Hasta luego!")
                    break
            else:
                print("Opción inválida. Por favor selecciona una opción entre 0 y 40.")
                
        except ValueError:
            print("Error: Ingresa un número válido.")
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"Error inesperado en el menú principal: {e}")

if __name__ == "__main__":
    menu_principal()
