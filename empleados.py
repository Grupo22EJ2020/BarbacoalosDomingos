class Empleados:
    def __init__(self,idempleado,nombreEmpleado,direccion):
        self.__idempleado= idempleado
        self.__nombreEmpleado= nombreEmpleado
        self.__direccion=direccion
    
    @property
    def idempleado(self):
        return self.__idempleado
    
    def infoempleado(self):
        return f" {self.__idempleado}|{self.__nombreEmpleado}|{self.__direccion}"
    
agregar= open("./archivos/empleados.txt" ,'a')

idempleado=int(input("Cual es el id del empleado:\n"))
nombreEmpleado=input("Cual es su nombre:\n")
direccion=input("Cual es su direccion:\n")

empleado= Empleados(idempleado,nombreEmpleado,direccion)
info=empleado.infoempleado()

agregar.write(info)

agregar.close()


