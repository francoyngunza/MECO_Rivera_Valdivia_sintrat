from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

#Socioecon
    email = models.StringField(label='Correo electrónico UP:')
    edad = models.IntegerField(label='Edad:', min=13, max=125)
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
    padrevivo = models.StringField(
        choices=['Sí','No'],
        label='Su padre está vivo:', 
    )
    madreviva = models.StringField(
        choices=['Sí','No'],
        label='Su madre está viva:', 
    )
    padre_estudios = models.StringField(
        choices=['Primaria','Secundaria','Superior técnico','Superior universitaria','Postgrado universitario'],
        label='Último año o grado de estudios que aprobó su padre:', 
    )
    madre_estudios = models.StringField(
        choices=['Primaria','Secundaria','Superior técnico','Superior universitaria','Postgrado universitario'],
        label='Último año o grado de estudios que aprobó su madre:', 
    )
    seguro = models.StringField(
        choices=['Si', 'No'],
        label='Tiene seguro de salud:',
        widget=widgets.RadioSelect,
    )
    tiposeguro = models.StringField(
        choices=['Essalud','Seguro integral de salud (SIS)','Entidad prestadora de salud (EPS)','Seguro privado de salud','No tengo seguro de salud'],
        label='Tipo de seguro de salud que tiene:', 
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
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='Creo que es mejor relacionarse con personas iguales a mí, porque tenemos más cosas en común',
        widget=widgets.RadioSelect,
    )
    discr_gral2 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='No tengo problema en que mi jefe(a) o profesor(a) sea cualquier persona mientras sea competente en su trabajo',
        widget=widgets.RadioSelect,
    )
    discr_gral3 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='Es bueno convivir y tratar personas de diferentes lugares del Perú y del mundo, aunque no tengan el mismo nivel socio económico, porque es enriquecedor para todos',
        widget=widgets.RadioSelect,
    )
    discr_gral4 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='Creo que la variedad de tipo de personas nos permite conocer y vivir nuevas experiencias',
        widget=widgets.RadioSelect,
    )
    discr_gral5 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='Me doy cuenta si una persona es capaz o no con solo verla físicamente y hablar un par de cosas con ella',
        widget=widgets.RadioSelect,
    )
    #Discriminación por raza o país
    discr_razapais1 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='Cuando veo algún venezolano procuro cuidar mis cosas y alegarme de él',
        widget=widgets.RadioSelect,
    )
    discr_razapais2 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='Creo que los norteamericanos o europeos, en su mayoría, son mejores que peruanos, porque viven en países desarrollados y cuidan mejor su imagen',
        widget=widgets.RadioSelect,
    )
    discr_razapais3 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='Jamás pensaría en ir a vivir en África por la gente, idioma y costumbres',
        widget=widgets.RadioSelect,
    )
    discr_razapais4 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='Jamás pensaría en ir a vivir en Japón por la gente, idioma y costumbres',
        widget=widgets.RadioSelect,
    )

    #Discriminación por nivel socioeconómico
    discr_soceco1 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='Creo que las personas que han estudiado en instituciones privadas están mejor preparadas que los demás',
        widget=widgets.RadioSelect,
    )
    discr_soceco2 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='Creo que el nivel socioeconómico tiene relación con el origen de las personas',
        widget=widgets.RadioSelect,
    )
    discr_soceco3 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='Preferiría relacionarme con personas de mi barrio, de mi colegio, universidad o trabajo',
        widget=widgets.RadioSelect,
    )
    discr_soceco4 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='Mis mejores amigos son de mi círculo social',
        widget=widgets.RadioSelect,
    )
    discr_soceco5 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='No me acostumbraría a vivir en otro lugar diferente al mío y menos si es otro distrito de menor categoría.',
        widget=widgets.RadioSelect,
    )
    discr_soceco6 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='Si tengo que hacer algún trabajo prefiero que sea por afinidad a que el profesor(a) forme el grupo.',
        widget=widgets.RadioSelect,
    )
    discr_soceco7 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='Los carros viejos no deberían circular por Miraflores, San Isidro, Surco, San Borja y la Molina, porque contaminan y dan mal aspecto.',
        widget=widgets.RadioSelect,
    )
    discr_soceco8 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='Preferiría trabajar en un puesto de jerarquía media en la costa, que un cargo de mayor jerarquía en una ciudad de la sierra o selva.',
        widget=widgets.RadioSelect,
    )
    discr_soceco9 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='Pienso que los alumnos de universidades estatales no están preparados ni capacitados como los de una universidad privada',
        widget=widgets.RadioSelect,
    )
    discr_soceco10 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='Estudiar y trabajar con personas como yo de mi barrio, colegio o universidad me hace sentir mejor y más realizado.',
        widget=widgets.RadioSelect,
    )

    #Discriminación por sexo
    discr_sexo1 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='Prefiero tener amigos de mí mismo sexo, porque tenemos muchas cosas en común',
        widget=widgets.RadioSelect,
    )
    discr_sexo2 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='Mi mejor amigo(a) es una persona del sexo opuesto',
        widget=widgets.RadioSelect,
    )
    discr_sexo3 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='Prefiero trabajar con personas de mí sexo porque tenemos muchas cosas en común y somos más capaces',
        widget=widgets.RadioSelect,
    )
    discr_sexo4 = models.StringField(
        choices=['Totalmente en desacuerdo', 'En desacuerdo','Ni de acuerdo, ni en desacuerdo','Totalmente de acuerdo','De acuerdo'],
        label='Pienso que hay cargos para los cuales la mujer aún no está muy preparada',
        widget=widgets.RadioSelect,
    )

# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['email','edad', 'genero','ciclo','distrito','carrera','escala','dpto','etnia','colegio','trabajo','hermanos',
                   'padrevivo','madreviva','padre_estudios','madre_estudios','seguro','tiposeguro','religion','religion_frec']


class Donacion1(Page):
    form_model = 'player'
    form_fields = ['d_positivo', 'd_oblig', 'd_fam1', 'd_fam2', 'd_donar', 'd_dni', 'd_proc']

class Donacion2(Page):
    form_model = 'player'
    form_fields = ['dc_pago', 'dc_fam', 'dc_sexo', 'dc_costo', 'dc_decision', 'dc_req']

class Racismo(Page):
    form_model = 'player'
    form_fields = ['discr_gral1', 'discr_gral2', 'discr_gral3', 'discr_gral4', 'discr_gral5', 'discr_razapais1', 'discr_razapais2'
                   , 'discr_razapais3', 'discr_razapais4', 'discr_soceco1', 'discr_soceco2', 'discr_soceco3', 'discr_soceco4', 'discr_soceco5'
                   , 'discr_soceco6', 'discr_soceco7', 'discr_soceco8', 'discr_soceco9', 'discr_soceco10', 'discr_sexo1', 'discr_sexo2'
                   , 'discr_sexo3', 'discr_sexo4']


page_sequence = [Demographics, Donacion1, Donacion2,Racismo]
