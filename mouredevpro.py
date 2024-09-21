"""/*
 * EJERCICIO:
 * He presentado mi proyecto más importante del año: mouredev pro.
 * Un campus para la comunidad, que lanzaré en octubre, donde estudiar
 * programación de una manera diferente.
 * Cualquier persona suscrita a la newsletter de https://mouredev.pro
 * accederá a sorteos mensuales de suscripciones, regalos y descuentos.
 *
 * Desarrolla un programa que lea los registros de un fichero .csv y
 * seleccione de manera aleatoria diferentes ganadores.
 * Requisitos:
 * 1. Crea un .csv con 3 columnas: id, email y status con valor "activo"
 *    o "inactivo" (y datos ficticios).
 *    Ejemplo: 1 | test@test.com | activo
 *             2 | test2@test.com | inactivo
 *    (El .csv no debe subirse como parte de la corrección)
 * 2. Recupera los datos desde el programa y selecciona email aleatorios.
 * Acciones:
 * 1. Accede al fichero .csv y selecciona de manera aleatoria un email
 *    ganador de una suscripción, otro ganador de un descuento y un último
 *    ganador de un libro (sólo si tiene status "activo" y no está repetido).
 * 2. Muestra los emails ganadores y su id.
 * 3. Ten en cuenta que la primera fila (con el nombre de las columnas)
 *    no debe tenerse en cuenta.
 */"""
 
import csv,random
                
def cantidad_lineas():
    cantidad = 0

    with open ("mouredevpro.csv") as file:
        datos = csv.reader(file , delimiter ="|")
    
        for dato in datos:
            cantidad = cantidad + 1
        return cantidad -1 
    
def ganador(posicion):
    num = 0

    with open ("mouredevpro.csv") as file:
        lineas = csv.reader(file , delimiter ="|")
    
        for linea in lineas:
            if num == posicion:
                ganador = linea
            num = num + 1
        
        return ganador     
    
cantidad = cantidad_lineas()  

while True:
    posicion1 = random.randint (1,cantidad)
    subscripcion = ganador(posicion1)
    if subscripcion [2] == " activo":
        break

while True:
    posicion2 = random.randint (1,cantidad) 
    if not(posicion2 == posicion1):
        descuento = ganador(posicion2)
        if descuento [2] == " activo":
            break
        
while True:
    posicion3 = random.randint (1,cantidad) 
    if not(posicion3 == posicion2 or posicion3 == posicion1):
        libro = ganador (posicion3)
        if libro [2] == " activo":
            break 
         
print (f"EL GANADOR DE LA SUBSCRIPCION ES: {subscripcion[1]} . CON ID: {subscripcion[0]}.\n")
print (f"EL GANADOR DE LA DESCUENTO ES: {descuento[1]} . CON ID: {descuento[0]}.\n")
print (f"EL GANADOR DE LA LIBRO ES: {libro[1]} . CON ID: {libro[0]}.\n")
           
    