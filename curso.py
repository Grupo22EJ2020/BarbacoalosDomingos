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
lista_curso=[]
print ("Menu")
while True:
    print ("Este es el menu para el curso")
    opcion=int(input("Opcion [1] Agregar\n,Opcion [2] Eliminar\n,Opcion [3] Modificar\n,Opcion [4] Consultar\n,¿Cual es la opcion que eliges?\n"))
    if opcion==[1]:
        archivo= open("./archivos/cursos.txt",'a')
       
        idcurso=int(input("¿Cual es el id del curso?\n"))
        descripcion=input("¿Cual es la descripcion del curso?\n")
        idempleado=int(input("¿Cual es el id del empleado?\n"))

        curso=Curso(idcurso,descripcion,idempleado)
        info=curso.infocurso()

        archivo.write(info)

        archivo.close()
    elif opcion==[2]:
        if lista_curso==[]:
            print("Ingrese el id del curso que desea borrar")
        else:
            reg=int(input("Registros:"))
            for borrar in lista_curso:
                if borrar.idcurso==reg:
                    lista_curso.remove(Curso(reg,None,None))
                    input("El curso a sido eliminado")
                    archivo.close

















