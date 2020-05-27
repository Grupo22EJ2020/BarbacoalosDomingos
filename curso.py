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
print (" Bienvenido al menu")
while True:
    print ("Este es el menu para el curso")
    opcion=int(input(" Opcion [1] Agregar\n Opcion [2] Eliminar\n Opcion [3] Modificar\n Opcion [4] Consultar\n ¿Cual es la opcion que eliges?\n"))
    if opcion==1:
        archivo = open("./archivos/cursos.txt",'a')
       
        idCurso=int(input("¿Cual es el id del curso?\n"))
        descripcion=input("¿Cual es la descripcion del curso?\n")
        idempleado=int(input("¿Cual es el id del empleado?\n"))

        curso=Curso(idcurso,descripcion,idempleado)
        info=curso.infocurso()

        archivo.write(info)

        archivo.close()
    
    if opcion==2:
        list ==[]
        borrar=print("Ingrese el id del curso que desea borrar")
        archivo = open("./archivos/cursos.txt",'a')
        for renglon in archivo:
            R = renglon.split("|")
            if borrar == R[0]:
                 pass
            else:
                list.append(renglon) 
            archivo.close()
            archivo = open("./archivos/cursos.txt",'a')
            for curso in list:
                 archivo.write(curso)
            archivo.close()
            print("El curso fue eliminado")
   
           
    if opcion==3:
        archivo=open("./archivos/cursos.txt",'a')
        for renglon in archivo:
            infocurso=renglon.split('|')
            print(F'IdCurso: {infocurso[0]} Descripcion:{infocurso[0]} IdEmpleado: {infocurso[0]}')
            archivo.close()
            



















