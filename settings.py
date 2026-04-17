from os import environ

SESSION_CONFIGS = [
    dict(
        name='pilot_survey',
        display_name='Pilotstudie – Was sollten werdende Eltern wissen?',
        app_sequence=['pilot_survey'],
        num_demo_participants=1,
        prolific=True,
        # Prolific completion URLs — replace these with the actual URLs from the Prolific study setup
        link_completed='https://app.prolific.com/submissions/complete?cc=C1N5RAH6',
        link_no_consent='https://app.prolific.com/submissions/complete?cc=C11JQHIK',
        link_no_attention='https://app.prolific.com/submissions/complete?cc=C1P0U9NC',
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0,
    participation_fee=0,
)

# Display language
LANGUAGE_CODE = 'de'

# Required for oTree 5
PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

ROOMS = [
    dict(
        name='pilot',
        display_name='Pilotstudie – Eltern & Arbeit',
    ),
]

ADMIN_USERNAME = 'hjkbkjn'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = ''

SECRET_KEY = '{{ secret_key }}'
