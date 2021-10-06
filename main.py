# -*- coding: utf-8 -*-

from operator import itemgetter
from SociosCls import SociosCls
from GUI import GUI



def main():
    global listSocios
    global listIndSocios
    listSocios = []
    listIndSocios = []
    
    dictCB = {
        "resetSocios":resetSocios,
        "addSocio":addSocio,
        "genIndexList":genIndexList,
        "punto1":punto1,
        "punto2":punto2,
        "punto3":punto3,
        "punto4":punto4,
        "punto5":punto5
        }

    app = GUI(dictCB)
    pass

def resetSocios():
    global listSocios
    listSocios = []

def addSocio(nombre,edad,equipo,estCivil,estudios):
    listSocios.append(SociosCls(nombre,edad,equipo,estCivil,estudios))

def genIndexList():
    global listIndSocios
    listIndSocios = range(len(listSocios))     

def punto1():
    return "La cantidad total de personas registradas es: " + str(len(listSocios))

def punto2():
    listRacing = list( filter(lambda ind:(listSocios[ind]).getEquipo()=="Racing",listIndSocios) )
    cantSocios = len(listRacing)
    if cantSocios != 0:
        listEdades = list( map(lambda ind:(listSocios[ind]).getEdad(),listRacing) )
        prom = (sum(listEdades)*1.0)/cantSocios
        return "El promedio de edad en los hinchas de Racing es de " + str(round(prom)) + " años"
    else:
        return "No hay hinchas de Racing registrados."

def punto3():
    listCasados = list ( filter(lambda ind:(listSocios[ind]).esCasadoUniversitario(),listIndSocios) ) [0:100]
    if len(listCasados) != 0:
        listCasados = sorted(listCasados,key=keyEdad)
        return list( map(lambda ind:(listSocios[ind]).punto3Model(),listCasados) )
    else:
        return []        
    
def keyEdad(ind):
    return listSocios[ind].getEdad()
        
def punto4():
    listRiver = list ( filter(lambda ind:listSocios[ind].getEquipo()=="River",listIndSocios) )
    dictNombres = {}
    for ind in listRiver:
        nombre = listSocios[ind].getNombre()
        dictNombres[nombre]= dictNombres.get(nombre,0) + 1
    listFreq = sorted(dictNombres.items(),key=itemgetter(1),reverse=True)
    return listFreq[0:5]

def punto5():
    dictEquipos = {}
    for Socio in listSocios:
        equipo = Socio.getEquipo()
        dictEquipos[equipo] = dictEquipos.get(equipo,0)+1
    listFreq = sorted(dictEquipos.items(),key=itemgetter(1),reverse=True)
    listResponse = []
    for i in range(len(listFreq)):
        equipo,cantSocios = listFreq[i]
        listSociosDelEquipo = list( filter(lambda ind:listSocios[ind].getEquipo()==equipo,listIndSocios) )
        listEdades = list( map(lambda ind:listSocios[ind].getEdad(),listSociosDelEquipo)  )
        edadMax = max(listEdades)
        edadMin = min(listEdades)
        listResponse.append((equipo,cantSocios,edadMax,edadMin))
    return listResponse

if __name__ == '__main__':
    main()
