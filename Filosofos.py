import threading
import time

total_comidas_por_filosofo = [0, 0, 0, 0, 0] ##se crea una lista para llevar un registro del número total de comidas que cada filósofo ha realizado:


def piensa(numero: int):##Esta es la funcion encargada de indiciar que filosofo se encuentra pensando, y agrega un cronometro de 1.5 segundos
    print("El filósofo " + str(numero) + " está pensando...")
    time.sleep(1.5)

def come(numero: int, tenedores: list):##esta es una de las funciones principales del programa que se encarga de que el filósofo coma. 
    ##Si el filósofo ya ha comido cinco veces, se imprime un mensaje informando que no puede comer más. 
    ## De lo contrario, se determinan los tenedores que le corresponden y se intenta tomarlos
    if(total_comidas_por_filosofo[numero-1] == 5):
        print("El filosófo " + str(numero) + " ya ha comido cinco veces. Por lo que no lo hace más.")
    else:
        print("El filósofo " + str(numero) + " se prepara para comer...")
        tenedor1 = tenedores[numero-1]
        try:
            numtenedor2 = numero
            tenedor2 = tenedores[numero]
        except:
            numtenedor2 = 0
            tenedor2 = tenedores[0]
        tomar_tenedores(tenedor1, tenedor2, numero)#En esta funcion se imprime un mensaje indicando cuáles fueron los tenedores tomados
        print("Se tomaron los tenedores: " + str(numero-1) + " y " + str(numtenedor2))
        print("El filósofo " + str(numero) + " está comiendo...")
        total_comidas_por_filosofo[numero-1] += 1
        time.sleep(1.5)#se espera un tiempo 1.5 segundos) para simular el tiempo de comer y se sueltan los tenedores mediante la función soltar_tenedores
        soltar_tenedores(tenedor1, tenedor2, numero)
        total = total_comidas_por_filosofo[numero-1]#y se actualiza la lista total_comidas_por_filosofo para llevar la cuenta de que el filósofo ha comido otra vez.
        print("El filósofo " + str(numero) + " ha comido un total de: " + str(total) + " veces.")
    
def tomar_tenedores(tenedor1 : threading.Semaphore, tenedor2: threading.Semaphore, numero: int):#esta función recibe como parámetros los dos tenedores que el filósofo intentará tomar y el número del filósofo. 
    #Si ambos tenedores están disponibles el filósofo los toma y se imprime un mensaje indicando que los ha tomado. 
    # Si no pasa esto se imprime un mensaje indicando que ha habido un problema al tomar los tenedores.
    try:
        tenedor1.acquire()
        tenedor2.acquire()  
        print("El filosofo " + str(numero) + " tomó los tenedores a su izquierda y derecha...")
    except:
        print("Existió un problema al momento de tomar tenedores")


def soltar_tenedores(tenedor1 : threading.Semaphore, tenedor2: threading.Semaphore, numero:int): #Esta función recibe como parámetros los dos tenedores que el filósofo ha utilizado y el número del filósofo. 
    #tambien Se imprime un mensaje indicando que el filósofo ha terminado de comer y suelta los tenedores.
    
    try:
        print("El filósofo " + str(numero) + " terminó de comer. Ahora suelta los tenedores...")
        tenedor1.release()
        tenedor2.release()
    except:
        print("Existió un problema al momento de soltar tenedores")

def filosofo(numero:int, tenedores:list):#Esta función representa el comportamiento completo de un filósofo, el cual se resumen en pensar y comer varias veces hasta que ha comido 5 veces. 
    #Se recibe como parámetros el número que identifica al filósofo y la lista con los tenedores disponibles. 
    # Dentro de la función, se utiliza ciclo que se repetirá mientras el filósofo no haya comido 5 veces. 
    # En cada vuelta del ciclo, se llama a la función piensa() para que el filósofo piense un tiempo, y luego se llama a la función come() para que el filósofo intente comer.
    while(total_comidas_por_filosofo[numero-1] < 5):
        piensa(numero)
        come(numero, tenedores)
    print("El filosófo " + str(numero) + " ya ha comido cinco veces. Por lo que no lo hace más.")

def main(): #Esta función es otra de las principales del programa, aqui se inicializan los semáforos que representan los tenedores, los cuales son 5
    #y se crea una lista de filósofos llamada philosopher_list que se utilizará para almacenar los hilos que se crearán para cada filósofo. 
    # Luego, se crea un ciclo que se repetirá 5 veces para crear los 5 hilos que representan a los filósofos, y se agregan a la lista philosopher_list. 
    # y al final se inicia cada hilo mediante la función start().
    tenedor1 = threading.Semaphore()
    tenedor2 = threading.Semaphore()
    tenedor3 = threading.Semaphore()
    tenedor4 = threading.Semaphore()
    tenedor5 = threading.Semaphore()
    tenedores = [tenedor1, tenedor2, tenedor3, tenedor4, tenedor5]
    philosopher_list = list()
    i = 1
    while i <= 5:
        philosopher = threading.Thread(target=filosofo, args=(i,tenedores))
        philosopher_list.append(philosopher)
        time.sleep(1.5)
        i += 1
    for i in range(5):
        philosopher_list[i].start()
        
if __name__ == "__main__":
    main()