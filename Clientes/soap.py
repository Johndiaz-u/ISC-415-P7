import zeep
import json

#url del servicio Web
wsdl = 'http://localhost:7777/ws/AcademicoWebService?wsdl'

#Cliente
client = zeep.Client(wsdl=wsdl)

#Lista de estudiantes
estudiantes_list = client.service.getAllEstudiante()

#Asignatura
asignatura = 20
asignatura = client.service.getAsignatura(asignatura)

#Consultando Profesor
cedula = "402-4893023-3"
profesor = client.service.getProfesor(cedula)

#Imprimiendo cada una de las consultas
print(asignatura)
print(estudiantes_list)
print(profesor)