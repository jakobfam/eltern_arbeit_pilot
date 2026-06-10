from os import environ

# NOTE: The Bilendi config is listed FIRST so it is the default selection when
# creating a session in the room. If you accidentally run the Prolific config,
# the end-of-survey redirect goes to Prolific, not Bilendi.
SESSION_CONFIGS = [
    dict(
        name='pilot_survey_bilendi',
        display_name='Pilotstudie – Bilendi Panel (LIVE)',
        app_sequence=['pilot_survey'],
        num_demo_participants=1,
        prolific=False,
        # --- Bilendi / respondi (Maximiles) dynamic redirect URLs ----------
        # The panelist ID arrives in the start link as the GET parameter
        # `participant_label` (oTree stores it as participant.label) and is
        # written back here in place of %SPM_PANELIST_ID%.
        # Project p=168504. Links taken verbatim from the Bilendi setup mail.
        link_completed='https://survey.maximiles.com/complete?p=168504_895c05cb&m=%SPM_PANELIST_ID%',
        link_screen_out='https://survey.maximiles.com/screenout?p=168504_21a5bfc7&m=%SPM_PANELIST_ID%',
        link_quotas_full='https://survey.maximiles.com/quotasfull?p=168504_ecc1b96f&m=%SPM_PANELIST_ID%',
        link_quality='https://survey.maximiles.com/quality?p=168504&m=%SPM_PANELIST_ID%',
        link_speeder='https://survey.maximiles.com/speeder?p=168504&m=%SPM_PANELIST_ID%',
        link_duplicate='https://survey.maximiles.com/duplicate?p=168504&m=%SPM_PANELIST_ID%',
        link_geoip='https://survey.maximiles.com/geoip?p=168504&m=%SPM_PANELIST_ID%',
        # Optional dedicated AI/quality redirect. If Bilendi provides a specific
        # link for AI-flagged respondents, set it here; otherwise AI-flagged
        # cases fall back to link_quality above.
        # link_ai='https://survey.maximiles.com/quality?p=168504&m=%SPM_PANELIST_ID%',
        # Speeder threshold: completes faster than this (seconds) -> speeder.
        # LOI is 15 min; we flag anything under 6 min (360 s).
        speeder_threshold_seconds=360,
        # AI/paste detection: flag if total pasted chars >= this AND pasting
        # dominates typing (see check_ai_keystroke).
        ai_paste_char_threshold=120,
    ),
    dict(
        name='pilot_survey',
        display_name='Pilotstudie – Prolific (alt)',
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
