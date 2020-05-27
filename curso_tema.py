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

print("Menú(TemaCurso)\n1.-Agregar Tema asignado a un curso.\n2.-Borrar Tema asignado a un curso\n3.-Modificar Tema asignado a un curso\n4.-Consultar todo\n5.-Consultar un Tema asignado a un curso en específico.")
   