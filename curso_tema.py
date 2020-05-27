class CursoTema:
    def __init__ (self, idCursoTema, idCurso, idTema):
        self.__idCursoTema = idCursoTema
        self.__idCurso = idCurso
        self.__idTema = idTema
    @property
    def idCursoTema(self):
        return self.__idCursoTema
    @property
    def idCurso(self):
        return self.__idCurso
    @property
    def idTema(self):
        return self.__idTema
    @idCursoTema.setter
    def idCursoTema(self, nuevoValor):
        self.__idCursoTema = nuevoValor
    @idCurso.setter
    def idCurso(self, nuevoValor):
        self.__idCurso = nuevoValor
    @idTema.setter
    def idTema(self, nuevoValor):
        self.__idTema = nuevoValor

def validacionDeDato(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False

def main():
    print("Menú(TemaCurso)\n1.-Agregar Tema asignado a un curso.\n2.-Borrar Tema asignado a un curso.\n3.-Modificar Tema asignado a un curso.\n4.-Consultar todo.\n5.-Consultar un Tema asignado a un curso en específico.\n6.-Salir.")
    menu = int(input("Qué desea hacer?:\n"))
    while True:
        if menu == 1:
            idCursoTema = input("Coloque el idCursoTema:\n")
            while validacionDeDato(idCursoTema) == False:
                print("Valor ingresado no válido, intente de nuevo.")
                idCursoTema = input("Coloque el idCursoTema:\n")

            idCurso = input("Coloque el idCurso:\n")
            while validacionDeDato(idCurso) == False:
                print("Valor ingresado no válido, intente de nuevo.")
                idCurso = input("Coloque el idCurso:\n")

            idTema = input("Coloque el idTema:\n")
            while validacionDeDato(idTema) == False:
                print("Valor ingresado no válido, intente de nuevo.")
                idTema = input("Coloque el idTema:\n")
                
            nuevo = CursoTema(idCursoTema, idCurso, idTema)
            archivo = open("./archivos/curso_tema.txt","a")
            archivo.write(f"{nuevo.idCursoTema}|{nuevo.idCurso}|{nuevo.idTema}\n")
            archivo.close()
            print("El curso se ha agregado con éxito")
            print("\nMenú(TemaCurso)\n1.-Agregar Tema asignado a un curso.\n2.-Borrar Tema asignado a un curso.\n3.-Modificar Tema asignado a un curso.\n4.-Consultar todo.\n5.-Consultar un Tema asignado a un curso en específico.\n6.-Salir.")
            menu = int(input("Qué desea hacer?:\n"))
        if menu == 2:
            list = []
            porborrar = input("Ingrese el idCursoTema que desee borrar:\n")
            archivo = open("./archivos/curso_tema.txt","r")
            for renglon in archivo:
                if porborrar in renglon:
                    pass
                else:
                    list.append(renglon)
            archivo.close()
            archivo = open("./archivos/curso_tema.txt","w")
            for dato in list:
                archivo.write(dato)
            archivo.close()
            print("El curso se ha borrado con éxito")
            print("\nMenú(TemaCurso)\n1.-Agregar Tema asignado a un curso.\n2.-Borrar Tema asignado a un curso.\n3.-Modificar Tema asignado a un curso.\n4.-Consultar todo.\n5.-Consultar un Tema asignado a un curso en específico.\n6.-Salir.")
            menu = int(input("Qué desea hacer?:\n"))
        if menu == 3:
            list2 = []
            datoviejo= input("Coloque el idCursoTema que desee modificar:\n")
            while validacionDeDato(datoviejo) == False:
                print("Valor ingresado no válido, intente de nuevo.")
                datoviejo = input("Coloque el idCursoTema que desee modificar:\n")
            datonuevo1 = input("Coloque el nuevo valor de idCursoTema:\n")
            while validacionDeDato(datonuevo1) == False:
                print("Valor ingresado no válido, intente de nuevo.")
                datonuevo1 = input("Coloque el nuevo valor de idCursoTema:\n")
            datonuevo2 = input("Coloque el el nuevo valor de idCurso:\n")
            while validacionDeDato(datonuevo2) == False:
                print("Valor ingresado no válido, intente de nuevo.")
                datonuevo2 = input("Coloque el nuevo valor idCurso:\n")
            datonuevo3 = input("Coloque el nuevo valor de idTema:\n")
            while validacionDeDato(datonuevo3) == False:
                print("Valor ingresado no válido, intente de nuevo.")
                datonuevo3 = input("Coloque el nuevo valor de idTema:\n")
            archivo = open("./archivos/curso_tema.txt","r")
            for renglon in archivo:
                if datoviejo in renglon:
                    list2.append(f"{datonuevo1}|{datonuevo2}|{datonuevo3}\n")
                else:
                    list2.append(renglon)
            archivo.close()
            archivo = open("./archivos/curso_tema.txt","w")
            for dato in list2:
                archivo.write(dato)
            archivo.close()
            print("\nMenú(TemaCurso)\n1.-Agregar Tema asignado a un curso.\n2.-Borrar Tema asignado a un curso.\n3.-Modificar Tema asignado a un curso.\n4.-Consultar todo.\n5.-Consultar un Tema asignado a un curso en específico.\n6.-Salir.")
            menu = int(input("Qué desea hacer?:\n"))
        if menu == 6:
            break
main()
    
