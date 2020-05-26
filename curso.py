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
    opcion=int(input("Opcion 1 Agregar, ¿Cual es la opcion que eliges?\n"))
    if opcion==1
    agregar= open




