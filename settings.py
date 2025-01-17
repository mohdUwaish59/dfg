from os import environ

SESSION_CONFIGS = [
    {
        'name': 'T1_no_comm',
        'display_name': 'T1_no_comm',
        'num_demo_participants': 18,
        'app_sequence': ['T1_no_comm'],
    },
    {
        'name': 'T1_Chat',
        'display_name': 'T1_Chat',
        'num_demo_participants': 18,
        'app_sequence': ['introduction', 'my_app', 'post_questionnaire'],
    },
    {
        'name': 'T1_Video',
        'display_name': 'T1_Video',
        'num_demo_participants': 18,
        'app_sequence': ['introduction', 'my_app_video', 'post_questionnaire'],
    },

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.0006691297208538588, participation_fee=2.00, doc=""
)

PARTICIPANT_FIELDS = ['gender', 'age', 'education']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '7520647312265'
