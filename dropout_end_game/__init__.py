from otree.api import *


doc = """
Dropout detection for multiplayer game (end the game)
"""


class C(BaseConstants):
    NAME_IN_URL = 'dropout_end_game'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    has_dropout = models.BooleanField(initial=False)


class Player(BasePlayer):
    is_dropout = models.BooleanField()


class Game(Page):
    timeout_seconds = 10


class DropoutTest(Page):
    timeout_seconds = 10

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        group = player.group
        if timeout_happened:
            group.has_dropout = True
            player.is_dropout = True


class WaitForOthers(WaitPage):
    pass


class DropoutHappened(Page):
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return group.has_dropout

    @staticmethod
    def app_after_this_page(player: Player, upcoming_apps):
        return upcoming_apps[0]


page_sequence = [Game, DropoutTest, WaitForOthers, DropoutHappened]