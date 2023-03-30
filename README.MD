<center> <h1>SISTEMAS OPERATIVOS II</h1> </center> 
<center> <h3>Wander Jerez 2021-0990</h3> </center>

<br>

<center> <h1>Problema de los filósofos</h1> </center>

*Cinco filósofos se sientan alrededor de una mesa y pasan su vida cenando y pensando. Cada filósofo tiene un plato de fideos y un tenedor a la izquierda de su plato. Para comer los fideos son necesarios dos tenedores y cada filósofo sólo puede tomar los que están a su izquierda y derecha. Si cualquier filósofo toma un tenedor y el otro está ocupado, se quedará esperando, con el tenedor en la mano, hasta que pueda tomar el otro tenedor, para luego empezar a comer.* 

*Si dos filósofos adyacentes intentan tomar el mismo tenedor a una vez, se produce una condición de carrera: ambos compiten por tomar el mismo tenedor, y uno de ellos se queda sin comer.*

*Si todos los filósofos toman el tenedor que está a su derecha al mismo tiempo, entonces todos se quedarán esperando eternamente, porque alguien debe liberar el tenedor que les falta. Nadie lo hará porque todos se encuentran en la misma situación (esperando que alguno deje sus tenedores). Entonces los filósofos se morirán de hambre. Este bloqueo mutuo se denomina interbloqueo o deadlock.* 

<br>

<center> <h2>Diagrama de flujo</h2> </center>

![foto9](/imagenes/diagramadeflujo.jpg)

<center> <h2>Video del funcionamiento</h2> </center>

*Acceda al enlace para ver el video del funcionamiento y explicación de code referentes a este problema*

https://drive.google.com/file/d/15hfjM70dFfLK8KCutx3JnHIfLQrf6Xtg/view?usp=share_link

<br>

<center> <h2>Codigo utilizado</h2> </center>

*Si le interesa visualizar el codigo utilizado para la solucion de este problema detallado mediante cometarios acceda al siguiente enlace(aunque en el video ya lo explico)*

- [ANALISIS DE CODE](ANALISISDECODE.MD)

<br>
<br>
<br>
<center> <h1>Investigación</h1> </center>

##  Concurrencias
*La concurrencia se refiere a la capacidad de un sistema para realizar múltiples tareas simultáneamente. En informática, se refiere específicamente a la capacidad de un programa o sistema para manejar varias tareas concurrentemente. Esto significa que múltiples procesos o hilos de ejecución pueden estar activos y ejecutándose al mismo tiempo.*

*La concurrencia puede ser útil en una variedad de situaciones, como cuando se trabaja con grandes cantidades de datos, cuando se necesitan respuestas rápidas a solicitudes de entrada/salida, o cuando se está diseñando un sistema de procesamiento distribuido.*

*Sin embargo, la concurrencia también puede ser un desafío, ya que puede ser difícil mantener la coherencia y consistencia de los datos cuando varios procesos o hilos están accediendo y modificando la misma información al mismo tiempo. La sincronización y la gestión adecuada de la concurrencia son críticas para garantizar la integridad de los datos y evitar errores y conflictos en el sistema*

##  Diferencias entre paralelismo y concurrencia
![foto1](/imagenes/1.png)

###  Paralelismo
*El paralelismo se refiere al uso simultáneo de múltiples recursos de procesamiento para realizar una tarea. En otras palabras, se trata de dividir una tarea en partes más pequeñas y ejecutarlas simultáneamente en varios procesadores o núcleos de procesamiento. El paralelismo se utiliza comúnmente en sistemas de alta velocidad, como supercomputadoras, para realizar cálculos complejos y procesamiento de datos a alta velocidad.*

###  Concurrencia

*La concurrencia, por otro lado, se refiere a la capacidad de un sistema para realizar múltiples tareas en tiempo compartido. En otras palabras, múltiples tareas o procesos pueden estar en ejecución simultáneamente en el mismo sistema, pero no necesariamente al mismo tiempo en diferentes núcleos o procesadores, lo que significa que los procesos comparten recursos de procesamiento. La concurrencia se utiliza comúnmente en sistemas multiusuario y en aplicaciones que requieren una gran cantidad de entrada/salida, como los servidores web.*

## ¿Que son los hilos?
*Un hilo es un proceso del sistema operativo con características distintas de las de un proceso normal: Los hilos existen como subconjuntos de los procesos. Los hilos comparten memoria y recursos*

*Los hilos nos permiten aprovechar las capacidades multiprocesador de nuestras máquinas para ejecutar varias instrucciones a la vez, como subprocesos independientes.*

## Hilos implementación en Python
*En Python, los hilos se pueden implementar utilizando la biblioteca estándar threading. La biblioteca threading proporciona un conjunto de herramientas para crear y administrar hilos en un programa Python.*

*Para crear un hilo en Python, primero debe definir una función que represente la tarea que desea realizar en paralelo. Luego, puede crear una instancia de la clase Thread en la biblioteca threading y proporcionar la función como argumento.*

*A continuación, puede iniciar el hilo utilizando el método start().*
*Aquí hay un ejemplo de cómo implementar hilos en Python usando la biblioteca threading:*

```
import threading

def tarea():
    print("Hola, estoy corriendo en un hilo")

hilo = threading.Thread(target=tarea)

hilo.start()
hilo.join()

```
*En este ejemplo, se define una función tarea() que simplemente imprime un mensaje en la consola. Luego, se crea una instancia de la clase Thread y se proporciona la función como argumento. Finalmente, se inicia el hilo utilizando el método start() y se espera a que el hilo termine utilizando el método join(). Después de que el hilo termina su tarea, se imprime un mensaje en la consola.*


## Deadlock

![foto2](/imagenes/2.png)

*Un deadlock (o "bloqueo") se produce cuando dos o más procesos quedan bloqueados permanentemente mientras esperan uno al otro para liberar un recurso. En otras palabras, cada proceso está esperando a que el otro libere el recurso que necesita para continuar.*

*Un deadlock puede ocurrir en cualquier sistema que tenga recursos compartidos y múltiples procesos o hilos de ejecución que intentan acceder a ellos simultáneamente. Por ejemplo, en un sistema de bases de datos, dos transacciones pueden estar esperando mutuamente la liberación de recursos bloqueados por la otra transacción.*

*Los deadlocks son problemáticos porque los procesos bloqueados no pueden continuar, lo que lleva a una pérdida de tiempo y recursos del sistema. Además, si el deadlock no se resuelve automáticamente, puede causar un fallo en el sistema.*

*Hay varias técnicas para prevenir y resolver deadlocks, como el uso de técnicas de exclusión mutua, como semáforos y monitores, para evitar que varios procesos accedan simultáneamente a los mismos recursos. Además, los algoritmos de planificación de procesos pueden detectar y resolver los deadlocks mediante la detección de ciclos de dependencias y la liberación de recursos.*


## Exclusion mutual
![foto3](/imagenes/3.png)

*La exclusión mutua es un problema común en programación concurrente, que se refiere a la necesidad de evitar que varios procesos o hilos de ejecución accedan simultáneamente a un recurso compartido, como una sección crítica de código o un recurso físico como un archivo o un dispositivo de entrada/salida. La exclusión mutua es importante para garantizar que los procesos o hilos accedan a los recursos compartidos de manera ordenada y segura, evitando situaciones de carrera crítica y resultados no deterministas.*

*Hay varias técnicas para implementar la exclusión mutua, incluyendo el uso de semáforos, monitores y bloqueos. Por ejemplo, los semáforos son un mecanismo común de exclusión mutua que permite que solo un hilo o proceso acceda a un recurso compartido a la vez. Los semáforos tienen dos operaciones principales: wait() y signal(). Cuando un hilo desea acceder a un recurso compartido, primero llama a la operación wait() en el semáforo. Si el semáforo está en cero, lo que indica que otro hilo está utilizando el recurso, el hilo que llama a wait() se bloquea hasta que el semáforo se incremente. Cuando el hilo que está utilizando el recurso termina, llama a la operación signal() para liberar el semáforo y permitir que otro hilo acceda al recurso.*

*Otra técnica común de exclusión mutua es el uso de monitores. Un monitor es un módulo de software que encapsula un recurso compartido y los procedimientos que acceden a ese recurso. El monitor mantiene una cola de procesos o hilos que desean acceder al recurso y garantiza que solo un proceso o hilo acceda al recurso a la vez. Los monitores son una forma efectiva de implementar la exclusión mutua, ya que la lógica de sincronización se encapsula dentro del monitor y los procedimientos que acceden al recurso no necesitan preocuparse por la sincronización explícita.*

*En resumen, la exclusión mutua es un problema común en programación concurrente, que se refiere a la necesidad de evitar que varios procesos o hilos de ejecución accedan simultáneamente a un recurso compartido. Hay varias técnicas para implementar la exclusión mutua, incluyendo el uso de semáforos, monitores y bloqueos.*

## Mantenga y espere

*"Espera y mantén" es una técnica de sincronización que se utiliza para evitar condiciones de carrera crítica y garantizar la exclusión mutua en un sistema concurrente. La técnica se basa en la idea de que un proceso o hilo debe esperar a que un recurso esté disponible antes de intentar acceder a él y una vez que ha adquirido el recurso, debe mantenerlo hasta que haya terminado de usarlo y lo haya liberado.*

*En la técnica de espera y mantén, cuando un proceso desea acceder a un recurso compartido, primero verifica si el recurso está disponible. Si el recurso está disponible, el proceso lo adquiere y lo mantiene hasta que ha terminado de usarlo. Si el recurso no está disponible, el proceso se pone en espera hasta que el recurso esté disponible y luego lo adquiere y lo mantiene.*

*La técnica de espera y mantén puede ser problemática en sistemas concurrentes si no se utiliza correctamente. Si varios procesos o hilos intentan adquirir y mantener recursos simultáneamente, puede haber una condición de espera circular en la que cada proceso está esperando a que el otro libere un recurso antes de poder continuar. Esto se conoce como un deadlock y puede causar que el sistema se bloquee.*

*Para evitar deadlocks en la técnica de espera y mantén, es importante que los procesos adquieran los recursos en el mismo orden y los liberen en el orden inverso. Además, los procesos deben liberar los recursos tan pronto como sea posible después de usarlos para minimizar la cantidad de tiempo que otros procesos deben esperar para adquirirlos. También se pueden utilizar otras técnicas de sincronización, como semáforos, monitores y bloqueos, para garantizar la exclusión mutua y evitar deadlocks.*

## No preventivo
*En el contexto de la programación concurrente, "no preventivo" se refiere a un modelo en el que el sistema operativo o el lenguaje de programación no interrumpen automáticamente los procesos o hilos de ejecución en un momento determinado. En otras palabras, los procesos o hilos no son "prevenidos" de ejecutar indefinidamente sin dar paso a otros procesos.*

*En un modelo no preventivo, los procesos o hilos deben cooperar explícitamente para permitir que otros procesos o hilos obtengan acceso a los recursos compartidos y evitar bloqueos o deadlocks. Los procesos o hilos pueden suspenderse o ponerse en espera explícitamente para esperar a que otros procesos completen sus operaciones.*

*El modelo no preventivo se utiliza en muchos sistemas de tiempo real y en sistemas operativos en tiempo compartido, donde se prefiere maximizar la eficiencia del sistema y minimizar la sobrecarga de conmutación de contexto. Sin embargo, el modelo no preventivo también puede ser más difícil de programar y depurar, ya que los procesos o hilos deben cooperar explícitamente para evitar problemas de sincronización y exclusión mutua.*

*Por otro lado, el modelo preventivo, también conocido como modelo de planificación de tiempo compartido, utiliza una política de planificación en la que el sistema operativo interrumpe automáticamente los procesos o hilos en momentos determinados, llamados "quantum" o "tiempo de rebanada". Esta política de planificación se utiliza en sistemas operativos de uso general como Windows y Linux, donde la prioridad y la justicia son factores importantes.*

## Espera circular
![foto4](/imagenes/4.png)

*La espera circular es una situación en la que dos o más procesos o hilos se bloquean mutuamente, cada uno esperando que el otro libere un recurso que necesita para continuar. Esta situación puede causar un deadlock, que es un estado en el que ningún proceso puede avanzar porque están todos bloqueados esperando que se liberen los recursos que otros procesos están reteniendo.*

*Por ejemplo, supongamos que dos procesos, A y B, necesitan acceder a dos recursos diferentes, X e Y, respectivamente. Si el proceso A adquiere el recurso X y luego intenta adquirir el recurso Y, mientras que al mismo tiempo el proceso B adquiere el recurso Y y luego intenta adquirir el recurso X, puede ocurrir una espera circular. En este caso, tanto el proceso A como el proceso B se bloquean esperando que el otro libere el recurso que necesita para continuar.*

*Para evitar la espera circular y los deadlocks, es necesario utilizar técnicas de sincronización adecuadas, como exclusión mutua y espera activa. Además, es importante asegurarse de que los recursos se adquieran y liberen en el mismo orden por todos los procesos que los utilizan. De esta manera, se puede garantizar que no haya conflicto en el acceso a los recursos y se pueden evitar las situaciones de espera circular.*

## Como manejar el interbloque en sistemas operativos – Compara con el problema de los filósofos
![foto5](/imagenes/5.jpg)



*El problema del interbloque o deadlock es un problema común en sistemas operativos cuando varios procesos o hilos intentan adquirir recursos compartidos de manera exclusiva y no pueden hacerlo debido a que otros procesos o hilos están reteniendo esos recursos. Esta situación puede llevar a una condición de bloqueo mutuo en la que ningún proceso o hilo puede avanzar.*

*El problema de los filósofos es un problema clásico en el que cinco filósofos se sientan alrededor de una mesa con un plato de espaguetis y un tenedor a cada lado. Los filósofos alternan entre comer y pensar, y solo pueden comer si tienen dos tenedores. El problema surge cuando cada filósofo intenta adquirir los dos tenedores a su lado al mismo tiempo, lo que lleva a una situación de interbloque o deadlock.*

*Para manejar el problema del interbloque en sistemas operativos, se pueden utilizar diferentes técnicas, como el algoritmo del banquero, el enfoque de prevención de deadlock, la detección y recuperación de deadlock, y la exclusión mutua. El algoritmo del banquero se utiliza para evitar que los procesos soliciten más recursos de los que están disponibles, mientras que el enfoque de prevención de deadlock implica diseñar un sistema en el que no sea posible que ocurra un deadlock. La detección y recuperación de deadlock se utilizan para detectar y resolver situaciones de deadlock existentes, mientras que la exclusión mutua se utiliza para garantizar que solo un proceso tenga acceso a un recurso compartido en un momento dado.*

*En el problema de los filósofos, se pueden utilizar técnicas similares para resolver el problema de interbloque. Una solución común es utilizar exclusión mutua para garantizar que solo un filósofo tenga acceso a un tenedor en un momento dado, y luego utilizar un algoritmo de asignación de recursos, como el algoritmo del banquero, para garantizar que no se produzca una situación en la que un filósofo tenga acceso a un solo tenedor y no pueda adquirir el otro. Otras soluciones incluyen la asignación de un tenedor adicional o la introducción de una regla de espera aleatoria para evitar que los filósofos intenten adquirir los tenedores al mismo tiempo.*