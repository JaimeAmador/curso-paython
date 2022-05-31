nombre = input ("Como te llamas?")

print(f"Hola {nombre}!!")


calificacion = input("Poner tu calificacion ")

calificacion = int(calificacion)
if calificacion < 700 :
    print("Reprobado")
else: 
    print("Feliciades Aprobado")