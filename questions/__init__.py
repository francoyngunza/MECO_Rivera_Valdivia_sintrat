from otree.api import *

doc = """
Questions
"""

class Constants(BaseConstants):
    name_in_url = 'questions'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    email = models.StringField(
        label='Email',
        )
    sexo = models.StringField(
        label='Sexo',
        choices=['Masculino', 'Femenino'],
        widget=widgets.RadioSelectHorizontal,
    )
    edad = models.IntegerField(
        label='Edad',
        min=18,
        max=70,
    )
    ultimo_ciclo = models.IntegerField(
        label='Último ciclo cursado',
        min=1,
        max=14,
    )
    distrito_residencia = models.StringField(
        label='Distrito de residencia',
        choices=['Lima norte', 'Lima centro', 'Lima sur', 'Lima este', 'Callao'],
        widget=widgets.RadioSelectHorizontal
    )
    carrera = models.StringField(
        label='Carrera',
        choices=[
            'Administración', 'Contabilidad', 'Derecho', 'Economía', 'Finanzas',
            'Ingeniería de la Información', 'Ingeniería Empresarial', 'Marketing',
            'Negocios Internacionales'
        ],
        widget=widgets.RadioSelectHorizontal
    )
    escala_pagos = models.IntegerField(
        label='Escala de pagos UP',
        choices=[
            (1, '1 (S/ 1,224.64)'), (2, '2 (S/ 947.03)'), (3, '3 (S/ 718.08)'),
            (4, '4 (S/ 527.05)'), (5, '5 (S/ 384.75) - Escala extraordinaria'),
            (6, '6 (S/ 283.18) - Escala extraordinaria')
        ],
        widget=widgets.RadioSelectHorizontal
    )
    lugar_nacimiento = models.StringField(
        label='Lugar de nacimiento',
        choices=['Lima', 'Provincia'],
        widget=widgets.RadioSelectHorizontal
    )
    autodeterminacion_etnica = models.StringField(
        label='Autodeterminación étnica',
        choices=[
            'Quechua', 'Aimara', 'Blanco', 'Mestizo', 'Nativo o indígena de la Amazonía',
            'Negro, moreno, zambo, mulato, pueblo afroperuano o afrodescendiente',
            'Perteneciente o parte de otro pueblo indígena u originario', 'Otro'
        ],
        widget=widgets.RadioSelectHorizontal
    )
    colegio_procedencia = models.StringField(
        label='Colegio de procedencia',
        choices=['Público', 'Privado'],
        widget=widgets.RadioSelectHorizontal
    )
    sector_trabajo = models.StringField(
        label='Sector en el que esté trabajando o haciendo prácticas',
        choices=['Sector Público', 'Sector Privado', 'Investigación', 'No trabajo o realizo prácticas'],
        widget=widgets.RadioSelectHorizontal
    )
    num_hermanos = models.IntegerField(
        label='Cuántos hermanos tiene',
        choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3 o más')],
        widget=widgets.RadioSelectHorizontal
    )
    padre_vivo = models.BooleanField(label='Su padre está vivo', choices=[(True, 'Sí'), (False, 'No')], widget=widgets.RadioSelectHorizontal)
    madre_viva = models.BooleanField(label='Su madre está viva', choices=[(True, 'Sí'), (False, 'No')], widget=widgets.RadioSelectHorizontal)
    grado_padre = models.StringField(
        label='Último año o grado de estudios que aprobó su padre',
        choices=[
            'Ninguno', 'Educación inicial / preescolar', 'Primaria', 'Secundaria',
            'Superior técnico', 'Superior universitaria', 'Postgrado universitario'
        ],
        widget=widgets.RadioSelectHorizontal
    )
    grado_madre = models.StringField(
        label='Último año o grado de estudios que aprobó su madre',
        choices=[
            'Ninguno', 'Educación inicial / preescolar', 'Primaria', 'Secundaria',
            'Superior técnico', 'Superior universitaria', 'Postgrado universitario'
        ],
        widget=widgets.RadioSelectHorizontal
    )
    seguro_salud = models.BooleanField(label='Tiene seguro de salud', choices=[(True, 'Sí'), (False, 'No')], widget=widgets.RadioSelectHorizontal)
    tipo_seguro_salud = models.StringField(
        label='Tipo de seguro de salud que tiene',
        choices=[
            'Essalud', 'Seguro integral de salud (SIS)', 'Entidad prestadora de salud (EPS)',
            'Seguro privado de salud', 'Otro tipo de seguro de salud', 'No tengo seguro de salud'
        ],
        widget=widgets.RadioSelectHorizontal
    )
    padres_separados = models.BooleanField(
        label='Es hijo de padres separados/divorciados',
        choices=[(True, 'Sí'), (False, 'No')],
        widget=widgets.RadioSelectHorizontal
    )
    religion = models.StringField(
        label='Religión a la que pertenece',
        choices=['Católicos', 'Evangélicos', 'Otra religión', 'Agnósticos o ateos'],
        widget=widgets.RadioSelectHorizontal
    )
    asistencia_religiosa = models.StringField(
        label='Frecuencia con la que asiste a ceremonias religiosas (por ejemplo, Misa)',
        choices=[
            '2 veces a la semana o más', '1 vez a la semana', '1 vez cada 15 días',
            '1 vez al mes', '1 o 2 veces al año', 'No asisto a ceremonias religiosas'
        ],
        widget=widgets.RadioSelectHorizontal
    )

class Questions(Page):
    timeout_seconds = 120

    form_model = 'player'
    form_fields = [
        'email', 'sexo', 'edad', 'ultimo_ciclo', 'distrito_residencia', 'carrera',
        'escala_pagos', 'lugar_nacimiento', 'autodeterminacion_etnica', 'colegio_procedencia',
        'sector_trabajo', 'num_hermanos', 'padre_vivo', 'madre_viva', 'grado_padre',
        'grado_madre', 'seguro_salud', 'tipo_seguro_salud', 'padres_separados', 'religion',
        'asistencia_religiosa'
    ]


class WaitForOthers(WaitPage):
    pass

    def app_after_this_page(player: Player, upcoming_apps):
        return upcoming_apps[0]

page_sequence = [Questions, WaitForOthers]
