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
    name_in_url = 'my_app_video'
    players_per_group = 3
    num_rounds = 20
    num_consumers = 6
    consumer_endowment = c(100)
    exchange_rate = 1500
    video_links = [
        'https://app.dyte.io/meeting/stage/nnqahd-ubgcsq?theme=preset&authToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImUzNTYxNjQxLTgyODMtNGNhMi1hYzgyLTllYTgxNjA5NjgwYSIsImxvZ2dlZEluIjp0cnVlLCJpYXQiOjE3MTg5ODk5NzEsImV4cCI6MTcyNzYyOTk3MX0.IjSMaPC6b7BiwfHG8BqpUF2DzlFimfn6W5YUDT-CeQwSri5_Q3jCbjOr1XLFw3iwm47SAbHtIBnF50nDOZayOYbt0E6_SYR5F0voIhGBJcQbMOuOBKezSXLgShVzTQloalsgvL81WHWgaU883fDJPykfjNovQ4DJp_U_JR1gomLmR8hqlTDH_q1Fs6ygokOJ7icLNy911Z2WBNsynTtD6e510pPdea_GNbRT4N2q5csr7_tKOsZrrj9Mg9bV-1LE_nxq72ykciKg2ctDnSHFhV52oGjCRHsdW9GfqJExzpchcb59DzjgNbeB2Is_fmBw3nKt_ufxIAZO98_S1gZ9-w',
        'https://app.dyte.io/meeting/stage/nghwtc-uqxeod?theme=preset&authToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImZlODczNmZlLWMwNmQtNGU3MC1iZWE1LTVlMTQ2YTgyOTI5NCIsImxvZ2dlZEluIjp0cnVlLCJpYXQiOjE3MTg5OTAwMTYsImV4cCI6MTcyNzYzMDAxNn0.WYTYCnXhkOFmNfcDXDV67CYwQJX35zi-hEfOEUp0j5ycb9pR59UaZ5U63u0IeoVz1IQ_dqiQxPW0Ue6WCoXnufX60YLjyBMqeaBW8e3jGjtLouyw2V6iaSqAUbzxt4Np3cfY4iM8HE6X7FJqQ4SOA3LfCdr48naEJ3TFbTAIMilH7k1KPqE6LpJwMmmLxA65PdQ4bKfYndc25pBvFIeXXQ6Qy-4Juvsv_7NpYT79edALqm20ZYezh8oJXxYPYw5aK4fE2jIIoM9GJEK8Rlk8cvjUs5bnOGJtJWSXZRWJ9XGek-zw_laPXJqwxUFS7vuVoUWbmTewiD7I1tSPSZ0glA',
        'https://app.dyte.io/meeting/stage/elaohq-xeredu?theme=preset&authToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjcwZWE0OTNhLTFmNmQtNDdhMy05ZGIwLTliM2M0MWU2MzBiZSIsImxvZ2dlZEluIjp0cnVlLCJpYXQiOjE3MTg5OTAwMzksImV4cCI6MTcyNzYzMDAzOX0.oayjW-wkvdGgsXAn5eaJDm71kWmZBB3UTUnqGQN92X7pV0J4_aqNEEgBl7KlFDO5EQW5i9zZOjZp-Uflt6ILAimmK_f9TwLe_WhYSahb6UTFr6C7s0_iFvShRXdpOAinQD6nfBsKkL03vrYlXyQ-EZkmhuH65AsaB9UTb-RzljsFFUgKFM5QhxZzj-M8KWRfQiN-yhvGfZy1zuo2UNNPQlRMoTjzHFVc0aKIKxTVfrY5EfRp3_5zmBEa-zI2FvvhEuJCsGs-HvuSi_FYkYDQky2uNvYMtZN2KehFrC7T-mZ6-kPzKE8nWqRE5DGmrAVQq9H72StWkcpyDd6i1txp4w',
        'https://app.dyte.io/meeting/stage/bsacjs-rhqwni?theme=preset&authToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjhjNDBkMDJmLTA1NmYtNGU0MC05Y2ZhLWM3MTIwNTU3MTFlYyIsImxvZ2dlZEluIjp0cnVlLCJpYXQiOjE3MTg5OTAwNjIsImV4cCI6MTcyNzYzMDA2Mn0.H-nFVDekPaypfRb3wdgEnznyhlvYbCK7Ya8OEdYAc9za8JYaCbOgaoS-KV7vYmcIBe7uMohbdVFG2PByPO0ZMfQf56SwfXfEBlVaPUOFNB-DoynvQAwH7_-WAuSuwq_RLFPOdOgDKVo-T4DxbFzWSKi2PxFki10mESZMe200r24yqFweg-RYawkmR0KtP1FlZC8UR6HmL1IogWnL7Ed3h3EelFuWk9zWCaIIAQuODu5rsZlaCjLXL9ul0-DX4xfxY5-n_4dOd-a0V6mLRPXGtVu9SDifx7E3i3Gs7JJWS-Fwso0fEb6ms_vbTUJS9jjCDe44M_JxTLNITnh2ItNFAw',
        'https://app.dyte.io/meeting/stage/djxvdp-mlpwdf?theme=preset&authToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjUxNTY0YTc4LThjYmYtNGEyMy05ZWYzLTBlNGUxMjM5OTg4ZiIsImxvZ2dlZEluIjp0cnVlLCJpYXQiOjE3MTg5OTAwODUsImV4cCI6MTcyNzYzMDA4NX0.vAQU14-b7wyo_IRrOjCTfYr9Oq8I0S6R48drNBIVi8PuaTntMQnKMUHav--pl8GvPeMmK2t3MJ5ssEAQyf98_MM7gud82aLmDFqb9f65ejWqBImTcKJrYg4x9p7QmSjqTGQoGQfK6q7HyRiyeLcNvamxQ6B7V7lu8E9NjcBoz5Qfo7FhI1osVWchpGsBJVG2eM1s7Rv0dN5PwzFL86EdKodE0fL1S_v9ZzS4hg5HoVaSlV55MX0aTxrqjnb7l_I8VNuqXudyZOv3s0d0UHjmzM6griLKNdIsU5ZBGz9WTASSEMCU0n_4WdvkB9t6TWWgIIHJkD1D0TfHZLuctHQ4Fg',
        'https://app.dyte.io/meeting/stage/cswdao-jjquqh?theme=preset&authToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImZlMzEzNTMzLTAyZTQtNGI4YS1iNzE5LWE5MWQxMjczYjNjNyIsImxvZ2dlZEluIjp0cnVlLCJpYXQiOjE3MTg5OTAxMDcsImV4cCI6MTcyNzYzMDEwN30.XSPk0hFBr_LfRt6-_RzKofkzPjZzk5AP9GhcIw0FA3JQgRkwu2JTYytM0avJ2-U0OY0T2JyDNxS5ShvUOIFeJcYDIrYmnOVSCKWc4JOZIwDNVX3tA6ZUVQt_kw0ZVftL1TXQPTlCczW5UStILmCizSygm2R18dbal53Gy9ntsOd7OA5hRmETIbRy5GFp8_vczhB7uTocDdil6EBEu8971IILmFYTA3OWk3yutthdryoacjC2gi8f12Dna9rUBXQ-OiJBw5xCiOX2QCLR089IazdmqVjUJy1csG_b1VKrqpNCRRabxAthdoof22ViqiaYmwXyiEuIR9J20l3a1jNcEQ',
        'https://app.dyte.io/meeting/stage/szvwvo-dacjar?theme=preset&authToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImRiZmM4MzJlLTFjMmUtNDU5OS05MmE2LWU5NTk2ZmViNTQ0YiIsImxvZ2dlZEluIjp0cnVlLCJpYXQiOjE3MTg5OTAxMzUsImV4cCI6MTcyNzYzMDEzNX0.FQccfGulfFag79wkDMLh0quTJ7yzwf3s3ShExi1RYLeuYmgLGzlvpCgwZdfwFR0VqGTnPAA6oy9dA5WKp0-HRtMVHlFYGhzNTsSnQAPwKOsYhw_l048rpA6GW4DbE2Ou7SBFbNPdPU0yq0fq6cB-7pHfiSCsS_g-dOksR0OTN4HGmuf7q3PuOeNvx9sMuPN5_SGJelN8cU-W0FmcKiTviS2QE1jZIMyajs_oM8lx9vRbU2t71XTOcwwhbcjzHTo7hYFI0ZAkfGnVjXM5QzO6PbCFdJH6BjdfT9Tz810vhPDLWPXApTmzjctu6764nqBlZoYs35MYcTuzAXIbicuq8Q',
        'https://app.dyte.io/meeting/stage/hevatk-yymacc?theme=preset&authToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY3N2I1NjUzLTJhMDItNDIwMi1iNDFiLWQ0MWI1MDVmMWE2ZSIsImxvZ2dlZEluIjp0cnVlLCJpYXQiOjE3MTg5OTAxNTksImV4cCI6MTcyNzYzMDE1OX0.Zci3gMqLpOK8vLPdQLsKeNqPTcVtrohXAHejuTLDbHNFfodGIPLR9QBAhf_qRkkr7aZKoz3zO8qrCL-x_wl2xzfLzWN2aNNvvHx3essXYz6QUohajLz5hHBtgcb-UmiBjK0wpIDRj3mX5VL8Duk7Hglgd3O3EwHsZo6M4gB6d1aPIYBeidPX9mXcAhlovU38nDmP0nt58XEj4FdP6rhinM3WnCR_Uos0nlFJKIFzYIBYNVGTfobuK4vRV45LtipvBLY-L8xL78Dx_AcQHRaX6DN4pRmF9luJ3OZCa8mnUJGKIdmjmsTx_mCzgodo8Y82LWZyJu_LB042AZp7v4gdjg',
        'https://app.dyte.io/meeting/stage/jnacvg-vsxhzq?theme=preset&authToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjhhNDM5M2NlLTQwMDEtNGQ5ZS1hYzJhLTRhNjVhNjc3NTRiMyIsImxvZ2dlZEluIjp0cnVlLCJpYXQiOjE3MTg5OTAxODgsImV4cCI6MTcyNzYzMDE4OH0.K5m4jM8SBQuwJB9PGGuhELCc84jPbaq6zp9vlxCElDQIPVm1RAtFzzP_E2x6E3QNhuYnrvrN-oC0gRmVFkoaWx6cZUW3toaVDUfNxKmcqSYA0KIqix_L35-tKBEdcyJI1LTYr_lCcV8UoixqySfFSpReEGiZhOBIlvO0hY318EBkqzIBaCTOO3ai3YD-Yaz_audoO2XYGHp3SXFJXK3VnKhzkWDB9Cn5zvkmtc3emzfKGlic7CNWvJ7E2cH28Wr-nSWMnPxUIHOqRThS4FLZQxM9TjXqy72RD8tNnR_dd0F6V1fUMM-K75uC548NHyt8Tuxk8ZzHO5EpN-DpnN6koA',
        'https://app.dyte.io/meeting/stage/jjxbha-uevlmm?theme=preset&authToken=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjIxODY3ZWQ1LTZlNmEtNDMzOS05OTBhLWMwMjI4YzBkN2I0NSIsImxvZ2dlZEluIjp0cnVlLCJpYXQiOjE3MTg5OTAyMTIsImV4cCI6MTcyNzYzMDIxMn0.NGRAGnU-wPzKs6bU_ocgSDBgGcBtyo5lR1F7TNmOsyqUDXzNUiCU3kGe04enh9Nh_f40bZ756l3LOy8-j3uIEHK1yio9ehskubuipQKbh_3pVZ1Wg4ajwc2d84rXfLzqyTFKkmCUeRPObo4eSUx2-BEYki4cKm5nGmImo09OHQGa5R5WytBG_f2dKdAhIRMddH1CYbBBoPrcjC6XpUZKa6C8f0zLmmbmxksgOCGFlTfdUKU_FiHP_3GXNb4tzWJDw-eNJxakJA2ItqlPhkZB9iWUqctW7SAqcbhqnrhgIcQmPKEIj-cuTzI2obXkwN9vhzmfGavNImDMhX74q4a4-Q',
        
    ]
    
class Subsession(BaseSubsession):
    def creating_session(self):
        for i, group in enumerate(self.get_groups()):
            if i < len(Constants.video_links):
                group.video_link = Constants.video_links[i]
            else:
                group.video_link = ""
            print(f"Debug: Assigned video link {group.video_link} to group {group.id_in_subsession}")

class Group(BaseGroup):
    video_link = models.StringField(initial="")

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

class VideoLinkPage(Page):
    form_model = 'player'
    form_fields = []

    def vars_for_template(self):
        video_link = self.group.video_link
        print(f"Debug: Video link for group {self.group.id_in_subsession}: {video_link}")
        return {
            'video_link': video_link,
        }


class WaitForGrouping(WaitPage):
    group_by_arrival_time = True

    '''@staticmethod
    def after_all_players_arrive(group: Group):
        for player in group.get_players():
            player.nickname = 'Firm ' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[player.id_in_group - 1]'''
            
    def after_all_players_arrive(self):
        # Ensure video links are assigned after grouping
        for i, group in enumerate(self.subsession.get_groups()):
            if i < len(Constants.video_links):
                group.video_link = Constants.video_links[i]
            else:
                group.video_link = ""
            print(f"Debug: Assigned video link {group.video_link} to group {group.id_in_subsession}")


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
    #Chat,
    VideoLinkPage,
    PriceSetting,
    ResultsWaitPage,
    ResultsPage,
    FinalPage,
]
