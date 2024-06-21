from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
    Page,  # Add this import
    WaitPage,  # Add this import
)

author = 'Your Name'

doc = """
Your experiment description
"""

class Constants(BaseConstants):
    name_in_url = 'my_app'
    players_per_group = 3
    num_rounds = 20
    num_consumers = 6
    consumer_endowment = c(100)
    exchange_rate = 1500

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    price = models.IntegerField(initial=0,
        label='What price (0-100) will you choose in this period?',
        min=0,
        max=100,
        blank=True
    )
    profit = models.CurrencyField(initial=c(0))
    total_profit = models.CurrencyField(initial=c(0))
    consumer_earnings = models.CurrencyField()
    nickname = models.StringField()

class WaitForGrouping(WaitPage):
    group_by_arrival_time = True

    @staticmethod
    def after_all_players_arrive(group: Group):
        for player in group.get_players():
            player.nickname = 'Firm ' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[player.id_in_group - 1]

class Chat(Page):
    timeout_seconds = 60

class PriceSetting(Page):
    form_model = 'player'
    form_fields = ['price']

class ResultsWaitPage(WaitPage):
    body_text = "Please wait until all other firms in your market have reached their decisions."
    after_all_players_arrive = 'set_profits'

    @staticmethod
    def set_profits(subsession):
        for group in subsession.get_groups():
            prices = [p.price or 0 for p in group.get_players()]
            min_price = min(prices)
            firms_with_min_price = [p for p in group.get_players() if p.price == min_price]
            num_firms_with_min_price = len(firms_with_min_price)

            consumers_per_firm = Constants.num_consumers // num_firms_with_min_price
            remaining_consumers = Constants.num_consumers % num_firms_with_min_price

            for player in group.get_players():
                player_price = player.price or 0
                if player_price == min_price:
                    player.profit = player_price * (consumers_per_firm + (1 if remaining_consumers else 0))
                    remaining_consumers -= 1
                else:
                    player.profit = c(0)

                player.payoff += player.profit

                player.consumer_earnings = (
                    Constants.num_consumers * (Constants.consumer_endowment - min_price)
                )

    def after_all_players_arrive(self):
        self.set_profits(self.subsession)

class ResultsPage(Page):
    def vars_for_template(self):
        lowest_price = min([p.price for p in self.group.get_players()])
        return {
            'earnings': int(self.profit),
            'each_consumer_subtracted': -lowest_price,
            'group_consumers_subtracted': -(lowest_price * Constants.num_consumers)
        }

class FinalPage(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        players = self.group.get_players()
        return {
            'payoff': int(self.payoff),
            'payoff_in_real_world_currency': self.payoff.to_real_world_currency(self.session),
        }

page_sequence = [
    WaitForGrouping,
    Chat,
    PriceSetting,
    ResultsWaitPage,
    ResultsPage,
    FinalPage,
]
