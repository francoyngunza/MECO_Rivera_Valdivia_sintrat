from otree.api import *

doc = """
Elections
"""

class Constants(BaseConstants):
    name_in_url = 'elections'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
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

class Election(Page):
    timeout_seconds = 120

    form_model = 'player'
    form_fields = [
        'img1', 'img2', 'img3', 'img4'
    ]


class WaitForOthers(WaitPage):
    pass

    def app_after_this_page(player: Player, upcoming_apps):
        return upcoming_apps[0]

page_sequence = [Election, WaitForOthers]
