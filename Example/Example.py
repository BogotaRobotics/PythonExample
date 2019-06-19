from datetime import datetime
#Espera del saludo del usuario
nameUser = ""
List = []


def evaluar(str):
    #Diccionario, switch case para mi
    switcher={
        "Hola": "¿que puedo hacer por ti?",
        "Dime la hora": obtenerHora(),
        "Agrega una tarea": definirTarea(),
        "Muestrame mis tareas":mostrarTareas(),
        "Cuantas tareas tengo":nTareas()
        }
    print(switcher.get(str, "Lo siento, no te entendí :(. Inténtalo de nuevo"))
    return;

#Actualiza el nombre del usuario, en caso de que ya lo haya digitado solo muestra el nombre guardado y le pregunta que quiere hacer
def setName():
    if not nameUser:
        nameUser=nameUser+input("Hola querido usuario, ¿cómo te llamas? \n")
    else:
        print("Hola!")
    out = "¿Qué puedo hacer por ti "+nameUser+"? \n"
    return out;

#Devuelve el numero de tareas
def nTareas():
    return "Tienes acutalmente "+len(List);

#Devuelve la hora en el formato HH/MM/SS
def obtenerHora():
    hora = datetime.now()
    return hora.strftime("%H:%M:%S");

#Agrega una tarea a la lista e imprime la tarea agregada
def definirTarea():
    entrada = input("Ingresa tu nueva tarea")
    List.append(entrada)
    return entrada;

#Muestra todas las tareas agregadas
def mostrarTareas():
    for i in range(0,len(List)):
        print(List[i])
    return "Estas son tus tareas";

#Se repite hasta que diga adios
while True:
    entrada = input(":D \n")
    if entrada=="Adios":
        print("Hasta luego, que estés bien. Vuelve pronto!")
        break
    else:
        evaluar(entrada)


