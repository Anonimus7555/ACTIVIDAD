
nota1 = int(input("Ingrese su primera nota: "))
while (nota1 < 0) or (nota1 > 20):
    print("Error al ingresar la nota")
    nota1 = int(input("Ingrese su primera nota: "))
    
nota2 = int(input("Ingrese su segunda nota: "))
while (nota2 < 0) or (nota2 > 20):
    print("Error al ingresar la nota")
    nota2 = int(input("Ingrese su segunda nota: "))
 
nota3 = int(input("Ingrese su tercera nota: ")) 
while (nota3 < 0) or (nota3 > 20):
    print("Error al ingresar la nota")
    nota3 = int(input("Ingrese su tercera nota: "))
    
promedio = (nota1 + nota2 + nota3)/3

if (promedio >= 10) and (promedio < 14):
    print(f"{promedio}  es su promedio de las 3 notas")
    print(int(promedio))
    print("PUEDE DAR EXAMEN SU SUSTITUTORIO SI DESEA OBTENER SU CERTIDICADO")
    
    
elif (promedio >= 14):
    print(f"{promedio}  es su promedio de las 3 notas")
    print(int(promedio))
    print("FELICIDADES POR APROBAR EL CURSO, OBTUVO SU CERTIFICADO")
    
else:
    print(f"{promedio}  es su promedio de las 3 notas")
    print(int(promedio))
    print("DESAPROBADO!!!!!!!!!!!!!!!!!!!!!!!")
    
    