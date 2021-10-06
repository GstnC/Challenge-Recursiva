class SociosCls:
    def __init__(self,nombre,edad,equipo,estCivil,estudios):
        self.__nombre = nombre
        self.__edad = edad
        self.__equipo = equipo
        self.__estCivil = estCivil
        self.__estudios = estudios
        pass

    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad

    def getEquipo(self):
        return self.__equipo

    def getEstCivil(self):
        return self.__estCivil
    
    def getEstudios(self):
        return self.__estudios

    def esCasadoUniversitario(self):
        return self.getEstCivil() == "Casado" and self.getEstudios() == "Universitario"

    def punto3Model(self):
        return (self.getNombre(),self.getEdad(),self.getEquipo())
    
    