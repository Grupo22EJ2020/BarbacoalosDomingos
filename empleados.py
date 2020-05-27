class Empleados:
    def __init__(self,idEmpleado,nombreEmpleado,direccion):
        self.__idEmpleado= idEmpleado
        self.__nombreEmpleado= nombreEmpleado
        self.__direccion=direccion
    
    @property
    def idEmpleado(self):
        return self.__idEmpleado

    @property
    def nombreEmpleado(self):
        return self.__nombre
    @nombreEmpleado.setter
    def nombre(self,nuevonombre):
        self.__nombre= nuevonombre

    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self,nuevadireccion):
        self.__direccion= nuevadireccion
    
    def infoempleado(self):
        return f" {self.__idEmpleado}|{self.__nombreEmpleado}|{self.__direccion}"
    
    def __eq__(self,valor):
        return self.__idEmpleado==valor.__idEmpleado

listaEmpleado=[]
print("Menu")
while True:
    print("Te presento el menu para Empleados")
    opcion= int(input("Opcion 1: Agregar,Opcion 2: Eliminar,3:Consultar todo\n"))
    if opcion ==1:
        archivo= open("./archivos/empleados.txt" ,'a',encoding='utf8')

        idEmpleado=int(input("Cual es el id del empleado:\n"))
        nombreEmpleado=input("Cual es su nombre:\n")
        direccion=input("Cual es su direccion:\n")

        empleado= Empleados(idEmpleado,nombreEmpleado,direccion)
        info=empleado.infoempleado()

        archivo.write(info)

        archivo.close()
    elif opcion ==2:
        archivo= open("./archivos/empleados.txt",'w')

        if listaEmpleado==[]:
            print("Ingrese un valor...presione enter")
        else:
            reg=int(input("Registro:"))
            for borrar in listaEmpleado:
                if borrar.idEmpleado == reg:
                    listaEmpleado.remove(Empleados(reg,None,None))
                    input("Empleado borrado")

    elif opcion==3:
        def main3():
            numero = 0
            print("Eligió la opcion de Modificar")
            print("*"*30)
            numero = input("Ingrese el numero del empleado que desea modificar: ")
            print("*"*30)
            archivoM = open("./archivos/Empleados.txt","r")
            lineas = archivoM.readlines()
            archivoM.close()
            archivoM = open("./archivos/Empleados.txt","w")

            for linea in lineas:
                if linea[0] == numero:
                    idEmpleado = (input("Ingrese su IdEmpleado nuevo: "))
                    nombre = (input("Ingrese su Nombre de Empleado nuevo: "))
                    direccion = (input("Ingrese su Direccion de Empleado nuevo: "))
                    archivoM.write(idEmpleado + "|" + nombre + "|" + direccion +"|"+ "\n")
                else:
                    archivoM.write(linea)
            archivoM.close()
        main3()
    elif opcion == 3:
        archivo = open("./archivos/empleados.txt","r")
        for renglon in archivo:
            datosproducto = renglon.split('|')
            print(f'Clave: {datosproducto[0]} Nombre: {datosproducto[1]} Direccion:{datosproducto[2]}')
        archivo.close()
