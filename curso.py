class Curso:
     def __init__(self,idcurso,descripcion,idempleado):
         self.__idcurso= idcurso
         self.__descripcion= descripcion
         self.__idempleado= idempleado

     @property   
     def idcurso(self):
         return self.__idcurso

     def infocurso(self):
         return f"{self.__idcurso}|{self.__descripcion}|{self.__idempleado}"

print ("Menu")
while True:
    print ("Este es el menu para el curso")
<<<<<<< HEAD
    opcion=int(input("Opcion 1 Agregar, ¿Cual es la opcion que eliges?\n"))
    if opcion==1:
        agregar= open
=======
    opcion=int(input("Opcion [1] Agregar\n, ¿Cual es la opcion que eliges?\n"))
    if opcion==[1]:
        agregar= open("./archivos/cursos.txt",'a')
       
    idcurso=int(input("¿Cual es el id del curso?\n"))
    descripcion=input("¿Cual es la descripcion del curso?\n")
    idempleado=int(input("¿Cual es el id del empleado?\n"))

    curso=Curso(idcurso,descripcion,idempleado)
    info=curso.infocurso()

    agregar.write(info)

    agregar.close()







>>>>>>> d81dd2d7477881fb108178f5a7cb009f6e79398d




