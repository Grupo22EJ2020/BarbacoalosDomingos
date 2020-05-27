class Curso:
    def __init__(self,idCurso,descripcion,idempleado):
         self.__idCurso= idCurso
         self.__descripcion= descripcion
         self.__idempleado= idempleado
         
    @property 
    def idCurso(self):
         return self.__idCurso

    def infoCurso(self):
         return f"{self.__idCurso}|{self.__descripcion}|{self.__idempleado}"
    
    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def idempleado(self):
        return self.__idempelado

    @idCurso.setter
    def idCurso(self,nuevovalor):
        self.__idCurso = nuevovalor

    @descripcion.setter
    def descripcion(self,nuevadescrpcion):
        self.__descripcion = nuevadescripcion

    

lista_curso=[]
print ("Menu")
while True:
    print ("Este es el menu para el Curso")
    opcion=int(input(" Opcion [1] Agregar\n Opcion [2] Eliminar\n Opcion [3] Modificar\n Opcion [4] Consultar\n ¿Cual es la opcion que eliges?\n"))
    if opcion==1:
        archivo =open("./archivos/cursos.txt",'a') 
       
        idCurso=int(input("¿Cual es el id del curso?\n"))
        descripcion=input("¿Cual es la descripcion del curso?\n")
        idempleado=int(input("¿Cual es el id del empleado?\n"))

        curso=Curso(idCurso,descripcion,idempleado)
        info=curso.infocurso()

        archivo.write(info)

        archivo.close()
       
    elif opcion==2:
        archivo= open("./archivos/empleados.txt",'w')
        if lista_curso==[]:
            print("Ingresa el cursoa eliminar")
        else:
            reg=int(input("Registro:"))
            for borrar in lista_curso:
                if borrar.idCurso == reg:
                    lista_curso.remove(curso(reg,None,None))
                    input("Curso eliminado")

    
    elif opcion==3:
        def main3():
            numero = 0
            print("A eligido modificar")
            numero = input("Ingrese el numero del curso a modificar")
            archivo= open("./archivos/empleados.txt",'r')
            lineas = archivo.readlines()
            archivo.close
            archivo = open("./archivos/empleados.txt",'w')

            for linea in lineas:
                if linea[0] == numero:
                    idCurso=int(input("Ingrese el nuevo id del curso"))
                    descripcion=input("Ingrese la nueva descripcion")
                    idempleado=int(input("ingresa el nuevo id para el epleado"))
                    archivo.write(idCurso + "|" + descripcion) + "|" + idempleado +"|"
                else:
                    archivo.write(linea)
            archivo.close
        main3()
    elif opcion == 3:
        archivo = open("./archivos/empleados.txt",'r')