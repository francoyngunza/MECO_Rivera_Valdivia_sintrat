import random
import time
from otree.api import *

doc = """
Juego de donación de órganos
"""

# Definición de variables globales
INICIO = True
TURNO = 1
RONDA = 1
TOTAL_RONDAS = 17 # Colocar el numero final de rondas +1
TIEMPO_PAGOS = 20 # En segundos (pagos)
TIEMPO_CORTO = 20 # En segundos (Simulación, ListaEspera, FinRonda)
TIEMPO_LARGO = 40 # En segundos (Donacion, Priorizacion)
TIEMPO_INSTRUCCIONES = 225 # En segundos (Instrucciones)
TIEMPO_DEMOGRAPHICS = 180 
TIEMPO_DONACION1 = 110 
TIEMPO_DONACION2 = 110 
TIEMPO_RACISMO = 350 

PAGO = [[0] * 25 for _ in range(25)]

# Funciones de configuraciones globales, tocar para pruebas y producción
def Total_Rondas():
    global TOTAL_RONDAS
    return TOTAL_RONDAS

def Tiempo_pagos():
    global TIEMPO_PAGOS 
    return TIEMPO_PAGOS

def Tiempo_corto():
    global TIEMPO_CORTO 
    return TIEMPO_CORTO 

def Tiempo_largo():
    global TIEMPO_LARGO
    return TIEMPO_LARGO

class C(BaseConstants):
    NAME_IN_URL = 'organ_donation'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 215
    CHANGE_COST = 0.75
    
# Subclases del juego
class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    ronda = models.IntegerField(initial=1)
    turno = models.IntegerField(initial=1)
    donaciones = models.IntegerField(initial=0)

class Player(BasePlayer):
    caso = models.CharField(initial="")
    turnos_en_espera = models.IntegerField(initial=0)
    organo_a_funcional = models.BooleanField(initial=True)
    organo_b_funcional = models.BooleanField(initial=True)
    es_donante = models.BooleanField(initial=False)
    donacion_previa = models.BooleanField(initial=False)
    en_lista_espera = models.BooleanField(initial=False)
    fuera_de_juego = models.BooleanField(initial=False)
    fin_turno = models.BooleanField(initial=False)
    pago = models.FloatField(initial=0.0)
    pago_final = models.FloatField(initial=0.0)

#Socioecon
    edad = models.IntegerField(label='Edad:', min=15, max=40)
    genero = models.StringField(
        choices=[['Masculino', 'Masculino'], ['Femenino', 'Femenino'], ['Otro', 'Otro']],
        label='Género:',
        widget=widgets.RadioSelect,
    )
    ciclo = models.StringField(
        choices=['1','2','3','4','5','6','7','8','9','10','11','12','13','14'],
        label='Último ciclo cursado:',      
    )
    distrito = models.StringField(label='Distrito de residencia:')
    carrera = models.StringField(
        choices=['Administración','Contabilidad','Derecho','Economía','Finanzas','Ing. de la Información','Ing. Empresarial','Marketing','Negocios Internacionales' ],
        label='Carrera:',      
    )
    escala = models.StringField(
        choices=['1 (S/ 1,224.64)','2 (S/ 947.03)','3 (S/ 718.08)','4 (S/ 527.05)','5 (S/ 384.75) - Escala extraordinaria','6 (S/ 283.18) - Escala extraordinaria'],
        label='Escala de pagos UP:',      
    )
    dpto = models.StringField(
        choices=['Lima','Provincia'],
        label='Lugar de nacimiento:',      
    )
    etnia = models.StringField(
        choices=['Quechua','Aimara','Blanco','Mestizo','Nativo o indígena de la Amazonía','Negro, moreno, zambo, mulato, pueblo afroperuano o afrodescendiente','Perteneciente o parte de otro pueblo indígena u originario','Otro'],
        label='Por sus costumbres y sus antepasados, usted se siente o considera:', 
    )
    colegio = models.StringField(
        choices=['Público','Privado'],
        label='Colegio de procedencia:', 
    )
    trabajo = models.StringField(
        choices=['Sector Público','Sector Privado','Organización sin fines de lucro','Organización internacional','Actualmente no trabajo ni realizo prácticas'],
        label='Sector en el que esté trabajando o haciendo prácticas:', 
    )
    hermanos = models.StringField(
        choices=['0','1','2','3 o más'],
        label='¿Cuántos hermanos tiene?', 
    )
    padresvivos = models.StringField(
        choices=['Sí, ambos padres','Solo mi madre','Solo mi padre','No'],
        label='Sus padres están vivos:', 
    )
    padre_estudios = models.StringField(
        choices=['Ninguno','Primaria','Secundaria','Superior técnico','Superior universitaria','Postgrado universitario'],
        label='Último año o grado de estudios que aprobó su padre:', 
    )
    madre_estudios = models.StringField(
        choices=['Ninguno','Primaria','Secundaria','Superior técnico','Superior universitaria','Postgrado universitario'],
        label='Último año o grado de estudios que aprobó su madre:', 
    )
    seguro = models.StringField(
        choices=['Sí, de Essalud','Sí, del Seguro integral de salud (SIS)','Sí, de la Entidad prestadora de salud (EPS)','Sí, tengo Seguro privado de salud','No tengo seguro de salud'],
        label='Tiene seguro de salud:', 
    )
    religion = models.StringField(
        choices=['Católicos','Evangélicos','Otra religión','Agnósticos o ateos'],
        label='Religión a la que pertenece:', 
    )
    religion_frec = models.StringField(
        choices=['2 veces a la semana o más','1 vez a la semana','1 vez cada 15 días','1 vez al mes','1 o 2 veces al año ','No asisto a ceremonias religiosas'],
        label='Frecuencia con la que asiste a ceremonias religiosas (por ejemplo, misa):', 
    )
#Donacion
    d_positivo = models.StringField(
        choices=['Si', 'No'],
        label='¿Crees que la donación de órganos es un acto positivo?',
        widget=widgets.RadioSelect,
    )
    d_oblig = models.StringField(
        choices=['Si', 'No'],
        label='¿Crees que la donación de órganos debería ser obligatoria?',
        widget=widgets.RadioSelect,
    )
    d_fam1 = models.StringField(
        choices=['Si', 'No'],
        label='¿Tienes algún familiar o conoces a alguien que necesita de la donación de órganos o tejidos?',
        widget=widgets.RadioSelect,
    )
    d_fam2 = models.StringField(
        choices=['Si', 'No'],
        label='¿Tienes algún familiar o conoces a alguien que haya recibido un trasplante de órganos o tejidos?',
        widget=widgets.RadioSelect,
    )
    d_donar = models.StringField(
        choices=['Si', 'No'],
        label='¿Estarías dispuesto/a a donar órganos?',
        widget=widgets.RadioSelect,
    )
    d_dni = models.StringField(
        choices=['Si', 'No'],
        label='En tu DNI, ¿apareces como donador de órganos?',
        widget=widgets.RadioSelect,
    )
    d_proc = models.StringField(
        choices=['Si', 'No'],
        label='¿Sabes el procedimiento que deberías seguir si quisieras ser donador de órganos?',
        widget=widgets.RadioSelect,
    )
    dc_pago = models.StringField(
        choices=['Verdadero', 'Falso'],
        label='Si acepto ser donante, mi familia tendrá que pagar más cuentas',
        widget=widgets.RadioSelect,
    )
    dc_fam = models.StringField(
        choices=['Verdadero', 'Falso'],
        label='Si acepto ser donante, mi familia tiene la potestad de permitir o impedir la donación',
        widget=widgets.RadioSelect,
    )
    dc_sexo = models.StringField(
        choices=['Verdadero', 'Falso'],
        label='Los órganos de un hombre pueden servir también para una mujer y viceversa.',
        widget=widgets.RadioSelect,
    )
    dc_costo = models.StringField(
        choices=['Verdadero', 'Falso'],
        label='Cambiar la decisión de donar órganos y tejidos en el DNI tiene un costo en soles',
        widget=widgets.RadioSelect,
    )
    dc_decision = models.StringField(
        choices=['Verdadero', 'Falso'],
        label='Si tengo más de 18 años, puedo decidir ser donante de órganos',
        widget=widgets.RadioSelect,
    )
    dc_req = models.StringField(
        choices=['Verdadero', 'Falso'],
        label='La muerte encefálica es el principal requisito para que una donación de órganos se haga efectiva',
        widget=widgets.RadioSelect,
    )
#Racismo
    #General
    discr_gral1 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='Creo que es mejor relacionarse con personas iguales a mí, porque tenemos más cosas en común',
        widget=widgets.RadioSelect,
    )
    discr_gral2 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='No tengo problema en que mi jefe(a) o profesor(a) sea cualquier persona mientras sea competente en su trabajo',
        widget=widgets.RadioSelect,
    )
    discr_gral3 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='Es bueno convivir y tratar personas de diferentes lugares del Perú y del mundo, aunque no tengan el mismo nivel socio económico, porque es enriquecedor para todos',
        widget=widgets.RadioSelect,
    )
    discr_gral4 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='Creo que la variedad de tipo de personas nos permite conocer y vivir nuevas experiencias',
        widget=widgets.RadioSelect,
    )
    discr_gral5 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='Me doy cuenta si una persona es capaz o no con solo verla físicamente y hablar un par de cosas con ella',
        widget=widgets.RadioSelect,
    )
    #Discriminación por raza o país
    discr_razapais1 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='Cuando veo algún venezolano procuro cuidar mis cosas y alejarme de él',
        widget=widgets.RadioSelect,
    )
    discr_razapais2 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='Creo que los norteamericanos o europeos, en su mayoría, son mejores que los peruanos, porque viven en países desarrollados y cuidan mejor su imagen',
        widget=widgets.RadioSelect,
    )
    discr_razapais3 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='Jamás pensaría en ir a vivir en África por la gente, idioma y costumbres',
        widget=widgets.RadioSelect,
    )
    discr_razapais4 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='Jamás pensaría en ir a vivir en Japón por la gente, idioma y costumbres',
        widget=widgets.RadioSelect,
    )

    #Discriminación por nivel socioeconómico
    discr_soceco1 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='Creo que las personas que han estudiado en instituciones privadas están mejor preparadas que los demás',
        widget=widgets.RadioSelect,
    )
    discr_soceco2 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='Creo que el nivel socioeconómico tiene relación con el origen de las personas',
        widget=widgets.RadioSelect,
    )
    discr_soceco3 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='Preferiría relacionarme con personas de mi barrio, de mi colegio, universidad o trabajo',
        widget=widgets.RadioSelect,
    )
    discr_soceco4 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='Mis mejores amigos son de mi círculo social',
        widget=widgets.RadioSelect,
    )
    discr_soceco5 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='No me acostumbraría a vivir en otro lugar diferente al mío y menos si es otro distrito de menor categoría.',
        widget=widgets.RadioSelect,
    )
    discr_soceco6 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='Si tengo que hacer algún trabajo prefiero que sea por afinidad a que el profesor(a) forme el grupo.',
        widget=widgets.RadioSelect,
    )
    discr_soceco7 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='Los carros viejos no deberían circular por Miraflores, San Isidro, Surco, San Borja y la Molina, porque contaminan y dan mal aspecto.',
        widget=widgets.RadioSelect,
    )
    discr_soceco8 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='Preferiría trabajar en un puesto de jerarquía media en la costa, que un cargo de mayor jerarquía en una ciudad de la sierra o selva.',
        widget=widgets.RadioSelect,
    )
    discr_soceco9 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='Pienso que los alumnos de universidades estatales no están preparados ni capacitados como los de una universidad privada',
        widget=widgets.RadioSelect,
    )
    discr_soceco10 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='Estudiar y trabajar con personas como yo de mi barrio, colegio o universidad me hace sentir mejor y más realizado.',
        widget=widgets.RadioSelect,
    )

    #Discriminación por sexo
    discr_sexo1 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='Prefiero tener amigos de mí mismo sexo, porque tenemos muchas cosas en común',
        widget=widgets.RadioSelect,
    )
    discr_sexo2 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='Mi mejor amigo(a) es una persona del sexo opuesto',
        widget=widgets.RadioSelect,
    )
    discr_sexo3 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='Prefiero trabajar con personas de mí sexo porque tenemos muchas cosas en común y somos más capaces',
        widget=widgets.RadioSelect,
    )
    discr_sexo4 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','De acuerdo','Totalmente de acuerdo'],
        label='Pienso que hay cargos para los cuales la mujer aún no está muy preparada',
        widget=widgets.RadioSelect,
    )

    #Para priorizacion
    img1 = models.StringField(
        label='Orden',
        choices=['1', '2', '3', '4']
    )

    img2 = models.StringField(
        label='Orden',
        choices=['1', '2', '3', '4']
    )

    img3 = models.StringField(
        label='Orden',
        choices=['1', '2', '3', '4']
    )

    img4 = models.StringField(
        label='Orden',
        choices=['1', '2', '3', '4']
    )

# FUNCTIONS
# PAGES
class Demographics(Page):
    timeout_seconds = TIEMPO_DEMOGRAPHICS

    form_model = 'player'
    form_fields = ['edad', 'genero','ciclo','distrito','carrera','escala','dpto','etnia','colegio','trabajo','hermanos',
                   'padresvivos','padre_estudios','madre_estudios','seguro','religion','religion_frec']
    @staticmethod
    def is_displayed(p: Player):
        return True if Ronda() == 1 and Inicio() else False


class Donacion1(Page):
    timeout_seconds = TIEMPO_DONACION1

    form_model = 'player'
    form_fields = ['d_positivo', 'd_oblig', 'd_fam1', 'd_fam2', 'd_donar', 'd_dni', 'd_proc']

    @staticmethod
    def is_displayed(p: Player):
        return True if Ronda() == 1 and Inicio() else False

class Donacion2(Page):
    timeout_seconds = TIEMPO_DONACION2

    form_model = 'player'
    form_fields = ['dc_pago', 'dc_fam', 'dc_sexo', 'dc_costo', 'dc_decision', 'dc_req']

    @staticmethod
    def is_displayed(p: Player):
        return True if Ronda() == 1 and Inicio() else False

class Racismo(Page):
    timeout_seconds = TIEMPO_RACISMO

    form_model = 'player'
    form_fields = ['discr_gral1', 'discr_gral2', 'discr_gral3', 'discr_gral4', 'discr_gral5', 'discr_razapais1', 'discr_razapais2'
                   , 'discr_razapais3', 'discr_razapais4', 'discr_soceco1', 'discr_soceco2', 'discr_soceco3', 'discr_soceco4', 'discr_soceco5'
                   , 'discr_soceco6', 'discr_soceco7', 'discr_soceco8', 'discr_soceco9', 'discr_soceco10', 'discr_sexo1', 'discr_sexo2'
                   , 'discr_sexo3', 'discr_sexo4']
    
    @staticmethod
    def is_displayed(p: Player):
        return True if Ronda() == 1 and Inicio() else False

class Instrucciones(Page):
    timeout_seconds = TIEMPO_INSTRUCCIONES

    @staticmethod
    def is_displayed(p: Player):
        return True if Ronda() == 1 and Inicio() else False

class Priorizacion(Page):
    #timeout_seconds = Tiempo_largo()

    form_model = 'player'
    form_fields = [
        'img1', 'img2', 'img3', 'img4'
    ]

    @staticmethod
    def is_displayed(p: Player):
        return Final(p)

class zFinal(Page):
        
    @staticmethod
    def is_displayed(p: Player):
        return Final(p)

# FUNCIONES

# Función para obtener pagos
def Guardar_Pago(p: Player):
    global PAGO, RONDA
    PAGO[p.id_in_group][RONDA - 1] = p.pago

def Pago_Final(p: Player):
    global PAGO, RONDA
    fila = PAGO[p.id_in_group][:RONDA - 1]
    print("Pago player {}: {}".format(p.id_in_group, fila))
    return random.choice(fila)

# Función para imprimir información del jugador
def log(p: Player, fx):
    g = p.group
    print("Player {}: {} | Donante: {} | Ronda: {} | Caso: {} | Fin Turno: {} | Pago: {}".format(
        p.id_in_group, fx, p.es_donante, Ronda(), p.caso, p.fuera_de_juego, p.pago))

# Función para resetear los campos del jugador
def ResetearJugador(p: Player):
    subsession = p.subsession
    g = p.group

    for p in subsession.get_players():
        p.caso = ""
        p.turnos_en_espera = 0
        p.organo_a_funcional = True
        p.organo_b_funcional = True
        p.es_donante = False
        p.donacion_previa = False
        p.en_lista_espera = False
        p.fuera_de_juego = False
        p.pago = 0.0
    
    g.donaciones = 0 
    g.turno = 1
    g.ronda = 1

# Función para guardar el estado del jugador y el grupo
def GuardarJugador(p: Player):
    global INICIO, TURNO, RONDA
    subsession = p.subsession
    g = p.group

    try:
        if TURNO > 1:
            for p in subsession.get_players():
                anterior = p.in_round(p.round_number - 1)
                g.donaciones = anterior.group.donaciones
                g.turno = anterior.group.turno
                g.ronda = Ronda()
                p.caso = anterior.caso
                p.turnos_en_espera = anterior.turnos_en_espera
                p.organo_a_funcional = anterior.organo_a_funcional
                p.organo_b_funcional = anterior.organo_b_funcional
                p.es_donante = anterior.es_donante
                p.donacion_previa = anterior.donacion_previa
                p.en_lista_espera = anterior.en_lista_espera
                p.fuera_de_juego = anterior.fuera_de_juego
                p.pago = anterior.pago
    except:
        INICIO = True
        TURNO = 1
        RONDA = 1

# Función para verificar si el juego está en su etapa de inicio
def Inicio():
    global INICIO
    return INICIO

# Función para obtener el número de ronda actual
def Ronda():
    global RONDA
    return RONDA

# Función para evaluar el final de una ronda
def Final(p: Player):
    g = p.group
    global RONDA
    return RONDA == Total_Rondas() and Inicio() and g.ronda > 1

# Función para evaluar el estado del juego y tomar decisiones
def Evaluar(p: Player):
    global INICIO, TURNO, RONDA
    g = p.group

    # Verificar si todos los jugadores han finalizado su turno
    if all(not p.fin_turno for p in g.subsession.get_players()):
        if not INICIO:
            g.turno += 1
            TURNO += 1

        INICIO = False
        p.fin_turno = True

    # Verificar si todos los jugadores están fuera del juego
    if all(p.fuera_de_juego for p in g.subsession.get_players()):
        ResetearJugador(p)
        g.ronda += 1
        INICIO = True
        TURNO = 1
        RONDA += 1

# Función para procesar la elección de donar del jugador
def ElegirDonar(p: Player):
    global RONDA, INICIO
    INICIO = False

    if p.es_donante:
        if RONDA <= 8:
            p.pago -= C.CHANGE_COST # Si es donante y la ronda es menor o igual a 80, se resta el costo del cambio de p.pago
    
    log(p, "ElegirDonar")

# Función para simular un caso para el jugador
def SimularCaso(p: Player):
    g = p.group
    caso = random.choices(['A', 'B', 'C'], [0.10, 0.20, 0.70])[0]
    p.caso = caso

    # Caso A: El órgano A no es funcional
    if caso == 'A':
        p.organo_a_funcional = False
        p.fuera_de_juego = True  # El jugador queda fuera del juego
        if p.es_donante:
            g.donaciones += 1  # Si el jugador es donante, se registra una donación en el grupo

    # Caso B: El órgano B no es funcional
    elif caso == 'B':
        if p.donacion_previa:
            p.fuera_de_juego = True  # Si el jugador ya realizó una donación previa, queda fuera del juego
        else:
            p.organo_b_funcional = False
            p.en_lista_espera = True  # El jugador entra en la lista de espera

    # Caso C: Ambos órganos son funcionales
    else:
        #p.organo_a_funcional = True
        #p.organo_b_funcional = True
        p.pago += 3.0  # Se incrementa el pago del jugador en 3.0 unidades

    if (p.fuera_de_juego):
        Guardar_Pago(p)

    if p.group.turno >= 10:
        p.fuera_de_juego = True #Jugador queda fuera del juego
    
    log(p, "SimularCaso")

# Función para evaluar la lista de espera del jugador
def EvaluarLista(p: Player):
    g = p.group

    # Verificar si el grupo tiene donaciones disponibles
    if g.donaciones > 0:
        g.donaciones -= 1  # Decrementar el contador de donaciones del grupo
        p.en_lista_espera = False  # El jugador ya no está en lista de espera
        p.donacion_previa = True  # Indicar que el jugador ha realizado una donación previa
        p.turnos_en_espera = 0  # Reiniciar el contador de turnos en espera

    if p.turnos_en_espera >= 5:
        p.fuera_de_juego = True  # El jugador está fuera del juego si ha estado en espera durante 5 turnos o más
    
    p.turnos_en_espera += 1  # Incrementar el contador de turnos en espera del jugador

    if (p.fuera_de_juego):
        Guardar_Pago(p)        
    log(p, "EvaluarLista")

# PÁGINAS

class Donacion(Page):
    timeout_seconds = Tiempo_largo()
    form_model = 'player'
    form_fields = ['es_donante']

    @staticmethod
    def is_displayed(p: Player):
        if not Inicio():
            GuardarJugador(p)

        return Inicio()
    
    @staticmethod
    def vars_for_template(p: Player):
        image_data = {
        'sin_tra': 1,  
        'sin_tra': 2,  
        'sin_tra': 3,
        'sin_tra': 4,
        'sin_tra': 5,
        'sin_tra': 6,
        'sin_tra': 7,
        'sin_tra': 8,
        'sin_tra': 9,
        'sin_tra': 10,
        'sin_tra': 11,
        'sin_tra': 12,
        'sin_tra': 13,
        'sin_tra': 14,
        'sin_tra': 15,
        'sin_tra': 16,
        'sin_tra': 17,
        'sin_tra': 18,
        'sin_tra': 19,
        'sin_tra': 20,
        }

        for imagen, ronda in image_data.items():
            if Ronda() <= ronda:
                image = 'SinTrat/{}.png'.format(imagen)
                break

        costo_ronda = 0.75 if Ronda() < 9 else 0
        
        return dict(
            image_path = image,
            costo_cambio = costo_ronda
        )

    @staticmethod
    def before_next_page(p: Player, timeout_happened):
        ElegirDonar(p)

class Simulacion(Page):
    timeout_seconds = Tiempo_corto()
    
    @staticmethod
    def vars_for_template(p: Player):
        return dict(
            ronda = Ronda()
        )

    @staticmethod
    def is_displayed(p: Player):
        return not p.en_lista_espera and not p.fuera_de_juego

    @staticmethod
    def before_next_page(p: Player, timeout_happened):
        SimularCaso(p)

class ListaEspera(Page):
    timeout_seconds = Tiempo_corto()

    @staticmethod
    def vars_for_template(p: Player):
        return dict(
            ronda = Ronda(),
            espera = p.turnos_en_espera
        )

    @staticmethod
    def is_displayed(p: Player):
        return p.en_lista_espera and not p.fuera_de_juego

    @staticmethod
    def before_next_page(p: Player, timeout_happened):
        EvaluarLista(p)

class EsperaJuego(WaitPage):
    @staticmethod
    def is_displayed(p: Player):
        return True if Ronda() == 1 and Inicio() else False

class Espera(WaitPage):
    @staticmethod
    def is_displayed(p: Player):
        return not p.fuera_de_juego

class FinTurno(WaitPage):
    template_name = 'orgams/FinTurno.html'

    @staticmethod
    def is_displayed(p: Player):
        return p.fuera_de_juego

class FinRonda(Page):
    timeout_seconds = Tiempo_pagos()

    @staticmethod
    def is_displayed(p: Player):
        g = p.group
        if all(p.fuera_de_juego for p in g.subsession.get_players()):
            time.sleep(3)
        Evaluar(p)
        return Ronda() == Total_Rondas()
    

    @staticmethod
    def vars_for_template(p: Player):
        p.pago_final = round((Pago_Final(p) * (1/2)), 1) + 5
        
        if p.pago_final >= 8:
            p.payoff = p.pago_final
        else:
            p.payoff = 8
            
        return dict(
            pago = p.payoff
        )
        

    #@staticmethod
    #def app_after_this_page(p: Player, upcoming_apps):
    #    return upcoming_apps[0]

page_sequence = [
    Demographics, Donacion1, Donacion2, Racismo, 
    Instrucciones,
    EsperaJuego,
    Donacion,
    Espera,
    Simulacion,
    ListaEspera,
    FinTurno,
    FinRonda,
    Priorizacion,
    zFinal,
    Espera
]
