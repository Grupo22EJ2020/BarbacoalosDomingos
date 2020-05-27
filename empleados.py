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
listaEmpleado=[]
print("Menu")
while True:
    print("Te presento el menu para Empleados")
    opcion= int(input("Opcion 1: Agregar,Opcion 2: Eliminar,4:Consultar todo Que opcion eliges:\n"))
    if opcion ==1:
        archivo= open("./archivos/empleados.txt" ,'a',encoding='utf8')

        idempleado=int(input("Cual es el id del empleado:\n"))
        nombreEmpleado=input("Cual es su nombre:\n")
        direccion=input("Cual es su direccion:\n")

        empleado= Empleados(idempleado,nombreEmpleado,direccion)
        info=empleado.infoempleado()

        archivo.write(info)

        archivo.close()
  

    elif opcion == 4:
        archivo = open("./archivos/empleados.txt","r")
        for renglon in archivo:
            datosproducto = renglon.split('|')
            print(f'Clave: {datosproducto[0]} Nombre: {datosproducto[1]} Direccion:{datosproducto[2]}')
        archivo.close()
