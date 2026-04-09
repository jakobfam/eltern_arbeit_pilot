from otree.api import *

doc = """
Pilotstudie: Was sollten werdende Eltern wissen?
A survey for mothers in Germany on financial experiences of parenthood.
Pages: Intro → A0 (demographics) → A (work) → B (finances) → C (advice) → D (knowledge) → Results
"""


class C(BaseConstants):
    NAME_IN_URL = 'pilot_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # ── Section A0: Demographics ───────────────────────────────────────

    a0_1_birth_year = models.IntegerField(
        label='<b>A0.1.</b> In welchem Jahr wurde Ihr erstes Kind geboren?',
        min=1980,
        max=2026,
    )

    a0_2_income = models.IntegerField(
        label='<b>A0.2.</b> Wie hoch ist das ungefähre jährliche Bruttoeinkommen Ihres Haushalts?',
        choices=[
            [1, 'Unter 30.000 €'],
            [2, '30.000 € – 50.000 €'],
            [3, '50.000 € – 80.000 €'],
            [4, '80.000 € – 120.000 €'],
            [5, 'Über 120.000 €'],
            [6, 'Möchte ich nicht angeben'],
        ],
        widget=widgets.RadioSelect,
    )

    a0_3_activity = models.IntegerField(
        label='<b>A0.3.</b> Was ist Ihre aktuelle Haupttätigkeit?',
        choices=[
            [1, 'Vollzeitbeschäftigt'],
            [2, 'Teilzeitbeschäftigt'],
            [3, 'Selbstständig / freiberuflich tätig'],
            [4, 'In Elternzeit'],
            [5, 'Hausfrau / zu Hause bei den Kindern'],
            [6, 'Arbeitslos und auf Stellensuche'],
            [7, 'Arbeitslos und nicht auf Stellensuche'],
            [8, 'Studentin / in Ausbildung'],
            [9, 'Sonstiges'],
        ],
        widget=widgets.RadioSelect,
    )

    a0_3_activity_other = models.StringField(
        label='Falls „Sonstiges": bitte angeben',
        blank=True,
    )

    # Conditional on any current or past paid employment (shown via JS in template)
    a0_3b_sector = models.IntegerField(
        label='<b>A0.3b.</b> In welchem Bereich sind oder waren Sie erwerbstätig?',
        choices=[
            [1, 'Öffentlicher Dienst / Beamtenstatus'],
            [2, 'Gesundheitswesen oder Soziale Arbeit'],
            [3, 'Bildung oder Wissenschaft'],
            [4, 'Wirtschaft, Finanzen oder Beratung'],
            [5, 'Technologie, Ingenieurwesen oder Naturwissenschaften'],
            [6, 'Handwerk, Produktion oder Logistik'],
            [7, 'Handel, Gastronomie oder Dienstleistungen'],
            [8, 'Sonstiges'],
        ],
        widget=widgets.RadioSelect,
        blank=True,
    )

    a0_3b_sector_other = models.StringField(
        label='Falls „Sonstiges": bitte angeben',
        blank=True,
    )

    a0_4_thoughts_before = model.LongStringField(
        label ='Was waren die <b>dre wichtigsten Themen</b> über die sie sich <b>vor</b> der Geburt Gedanken gemacht haben?'
    )

    a0_5_thoughts_wish = model.LongStringField(
        label ='Was waren die <b>dre wichtigsten Themen</b> über die sie sich <b>gewünscht hätten</b>, dass Sie sich vor der Geburt Gedanken gemacht haben?'
    )


    # ── Section A: Return to Work ──────────────────────────────────────

    a1_work_experience = models.LongStringField(
        label=(
            '<b>A1.</b> Denken Sie an die Zeit nach der Geburt Ihres ersten Kindes: '
            'Wie hat sich die Elternschaft auf Ihr Berufsleben ausgewirkt? '
            'Was hat sich verändert, welche Herausforderungen gab es, und wie haben Sie entschieden, '
            'ob, wann und wie viel Sie arbeiten?'
        ),
    )

    # A2: Ranking question — each item receives a rank of 1, 2, or 3 (or blank).
    # Participants must assign each rank at most once; validated in error_message.
    a2_rank_childcare = models.IntegerField(
        label='Kinderbetreuung war nicht verfügbar, zu teuer oder passte nicht zu meinen Arbeitszeiten',
        choices=[[1, '1'], [2, '2'], [3, '3']],
        blank=True, widget=widgets.RadioSelectHorizontal,
    )
    a2_rank_taxbenefit = models.IntegerField(
        label='Mehr zu arbeiten hätte sich finanziell kaum gelohnt (wegen Steuern und wegfallender Leistungen)',
        choices=[[1, '1'], [2, '2'], [3, '3']],
        blank=True, widget=widgets.RadioSelectHorizontal,
    )
    a2_rank_employer = models.IntegerField(
        label='Mein Arbeitgeber bot nicht die Flexibilität oder Arbeitszeiten, die ich brauchte',
        choices=[[1, '1'], [2, '2'], [3, '3']],
        blank=True, widget=widgets.RadioSelectHorizontal,
    )
    a2_rank_partner = models.IntegerField(
        label='Die Arbeitssituation meines Partners erschwerte eine gleichmäßige Aufteilung der Kinderbetreuung',
        choices=[[1, '1'], [2, '2'], [3, '3']],
        blank=True, widget=widgets.RadioSelectHorizontal,
    )
    a2_rank_confidence = models.IntegerField(
        label='Nach der Auszeit fehlte mir berufliches Selbstvertrauen',
        choices=[[1, '1'], [2, '2'], [3, '3']],
        blank=True, widget=widgets.RadioSelectHorizontal,
    )
    a2_rank_recovery = models.IntegerField(
        label='Die körperliche oder seelische Erholung nach der Geburt dauerte länger als erwartet',
        choices=[[1, '1'], [2, '2'], [3, '3']],
        blank=True, widget=widgets.RadioSelectHorizontal,
    )
    a2_rank_preference = models.IntegerField(
        label='Ich wollte mehr Zeit mit meinem Kind verbringen und habe mich bewusst gegen eine (frühere) Rückkehr entschieden',
        choices=[[1, '1'], [2, '2'], [3, '3']],
        blank=True, widget=widgets.RadioSelectHorizontal,
    )
    a2_rank_nodifficulty = models.IntegerField(
        label='Insgesamt hatte ich keine größeren Schwierigkeiten beim Wiedereinstieg',
        choices=[[1, '1'], [2, '2'], [3, '3']],
        blank=True, widget=widgets.RadioSelectHorizontal,
    )
    a2_other_text = models.StringField(
        label='Sonstiges (bitte angeben):',
        blank=True,
    )
    a2_rank_other = models.IntegerField(
        label='Rang für „Sonstiges"',
        choices=[[1, '1'], [2, '2'], [3, '3']],
        blank=True, widget=widgets.RadioSelectHorizontal,
    )

    # Conditional: shown only when A0.3 is not homemaker (5) or not-seeking-unemployed (7)
    a3_wishes = models.LongStringField(
        label=(
            '<b>A3.</b> Was hätten Sie sich beim Wiedereinstieg anders gewünscht – '
            'egal ob er schon hinter Ihnen liegt oder noch bevorsteht? '
            'Das kann etwas Eigenes sein, etwas vom Arbeitgeber oder etwas am System.'
        ),
        blank=True,
    )

    a4_expectation = models.IntegerField(
        label=(
            '<b>A4.</b> Wie hat sich Ihr Berufsleben nach der Geburt im Vergleich zu Ihren Erwartungen entwickelt?'
        ),
        choices=[
            [1, 'Ungefähr so, wie ich es erwartet hatte'],
            [2, 'Ich bin früher als gedacht zurückgekehrt'],
            [3, 'Ich bin später als gedacht zurückgekehrt'],
            [4, 'Ich hatte erwartet zurückzukehren, bin es aber bisher nicht'],
            [5, 'Ich hatte nicht vor zurückzukehren – und bin es auch nicht'],
            [6, 'Ich hatte vorher keine konkreten Erwartungen'],
        ],
        widget=widgets.RadioSelect,
    )

    a4_reason = models.LongStringField(
        label='Falls Ihre Situation anders verlaufen ist als erwartet: Was war der Hauptgrund?',
        blank=True,
    )

    # ── Section B: Financial Surprises ────────────────────────────────

    b1_biggest_surprise = models.LongStringField(
        label=(
            '<b>B1.</b> Was war die größte finanzielle Überraschung für Sie, nachdem Sie Mutter geworden sind? '
            'Das kann etwas Positives oder Negatives sein – alles, was Sie nicht erwartet haben.'
        ),
    )

    # B2: Ranking question — same pattern as A2
    b2_rank_income_drop = models.IntegerField(
        label='Der Einkommensrückgang während der Elternzeit',
        choices=[[1, '1'], [2, '2'], [3, '3']],
        blank=True, widget=widgets.RadioSelectHorizontal,
    )
    b2_rank_tax_work = models.IntegerField(
        label='Der Einfluss von Steuern und Sozialleistungen darauf, ob sich Mehrarbeit lohnt',
        choices=[[1, '1'], [2, '2'], [3, '3']],
        blank=True, widget=widgets.RadioSelectHorizontal,
    )
    b2_rank_pension = models.IntegerField(
        label='Die Auswirkung von Teilzeitarbeit auf meine spätere Rente',
        choices=[[1, '1'], [2, '2'], [3, '3']],
        blank=True, widget=widgets.RadioSelectHorizontal,
    )
    b2_rank_childcare_cost = models.IntegerField(
        label='Die Kosten und Verfügbarkeit von Kinderbetreuung',
        choices=[[1, '1'], [2, '2'], [3, '3']],
        blank=True, widget=widgets.RadioSelectHorizontal,
    )
    b2_rank_career = models.IntegerField(
        label='Der Einfluss eines Kindes auf meinen beruflichen Werdegang und mein Gehalt',
        choices=[[1, '1'], [2, '2'], [3, '3']],
        blank=True, widget=widgets.RadioSelectHorizontal,
    )
    b2_rank_daily_costs = models.IntegerField(
        label='Die alltäglichen Kosten mit Kind (Ausstattung, Aktivitäten, Essen)',
        choices=[[1, '1'], [2, '2'], [3, '3']],
        blank=True, widget=widgets.RadioSelectHorizontal,
    )
    b2_rank_insurance = models.IntegerField(
        label='Änderungen bei Versicherungen und Gesundheitsversorgung für die Familie',
        choices=[[1, '1'], [2, '2'], [3, '3']],
        blank=True, widget=widgets.RadioSelectHorizontal,
    )
    b2_rank_elterngeld = models.IntegerField(
        label='Wie Elterngeld und ElterngeldPlus in der Praxis tatsächlich funktionieren',
        choices=[[1, '1'], [2, '2'], [3, '3']],
        blank=True, widget=widgets.RadioSelectHorizontal,
    )
    b2_rank_prepared = models.IntegerField(
        label='Insgesamt hat mich davon nichts besonders überrascht',
        choices=[[1, '1'], [2, '2'], [3, '3']],
        blank=True, widget=widgets.RadioSelectHorizontal,
    )
    b2_other_text = models.StringField(
        label='Sonstiges (bitte angeben):',
        blank=True,
    )
    b2_rank_other = models.IntegerField(
        label='Rang für „Sonstiges"',
        choices=[[1, '1'], [2, '2'], [3, '3']],
        blank=True, widget=widgets.RadioSelectHorizontal,
    )

    b3_preparedness = models.IntegerField(
        label=(
            '<b>B3.</b> Wie gut fühlten Sie sich vor der Geburt Ihres ersten Kindes '
            'auf die finanziellen Veränderungen durch die Elternschaft vorbereitet?'
        ),
        choices=[
            [1, 'Überhaupt nicht vorbereitet'],
            [2, 'Kaum vorbereitet'],
            [3, 'Einigermaßen vorbereitet'],
            [4, 'Gut vorbereitet'],
            [5, 'Sehr gut vorbereitet'],
        ],
        widget=widgets.RadioSelectHorizontal,
    )

    b4_planning_horizon = models.IntegerField(
        label=(
            '<b>B4.</b> Als Sie sich finanziell auf Ihr erstes Kind vorbereitet haben, '
            'wie weit haben Sie dabei hauptsächlich in die Zukunft gedacht?'
        ),
        choices=[
            [1, 'Hauptsächlich an die Schwangerschaft und die Geburt selbst'],
            [2, 'Die Elternzeit (ungefähr die ersten 1–2 Jahre)'],
            [3, 'Die frühe Kindheit (bis zum Schulalter)'],
            [4, 'Langfristig (Karriereweg, Rente, Familienfinanzen über viele Jahre)'],
            [5, 'Ich habe mir vor der Geburt nicht viel über die finanzielle Seite Gedanken gemacht'],
        ],
        widget=widgets.RadioSelect,
    )

    b4b_regret = models.IntegerField(
        label='<b>B4b.</b> Rückblickend: Hätten Sie gerne weiter in die Zukunft geplant?',
        choices=[
            [1, 'Ja, auf jeden Fall – die langfristigen Auswirkungen habe ich unterschätzt'],
            [2, 'Ein bisschen – die grobe Richtung stimmte, aber die Details haben mich überrascht'],
            [3, 'Nein – mein Planungshorizont war passend'],
        ],
        widget=widgets.RadioSelect,
    )

    # ── Section C: Advice ─────────────────────────────────────────────

    c1_advice = models.LongStringField(
        label=(
            '<b>C1.</b> Eine enge Freundin erzählt Ihnen, dass sie ihr erstes Kind erwartet. '
            'Welchen finanziellen Ratschlag würden Sie ihr geben?'
        ),
    )

    # C2: Multi-select (1–3) — implemented as 9 BooleanFields rendered as checkboxes
    c2_elterngeld = models.BooleanField(
        label='Wie Elterngeld und ElterngeldPlus funktionieren (Beträge, Dauer, Antragstellung)',
        widget=widgets.CheckboxInput, blank=True, initial=False,
    )
    c2_tax = models.BooleanField(
        label='Steuerliche Auswirkungen verschiedener Arbeitszeitmodelle (Steuerklassenwahl, Ehegattensplitting)',
        widget=widgets.CheckboxInput, blank=True, initial=False,
    )
    c2_pension = models.BooleanField(
        label='Wie sich Teilzeitarbeit langfristig auf die Rentenansprüche auswirkt',
        widget=widgets.CheckboxInput, blank=True, initial=False,
    )
    c2_childcare = models.BooleanField(
        label='Kinderbetreuung: Verfügbarkeit, Kosten und rechtzeitige Platzsuche',
        widget=widgets.CheckboxInput, blank=True, initial=False,
    )
    c2_career = models.BooleanField(
        label='Beruflich auf Kurs bleiben während und nach der Elternzeit',
        widget=widgets.CheckboxInput, blank=True, initial=False,
    )
    c2_insurance = models.BooleanField(
        label='Versicherungs- und Gesundheitsänderungen (Familienversicherung, Zusatzversicherung)',
        widget=widgets.CheckboxInput, blank=True, initial=False,
    )
    c2_budget = models.BooleanField(
        label='Haushalten mit weniger Einkommen',
        widget=widgets.CheckboxInput, blank=True, initial=False,
    )
    c2_savings = models.BooleanField(
        label='Langfristige Spar- und Investitionsplanung als Familie',
        widget=widgets.CheckboxInput, blank=True, initial=False,
    )
    c2_legal = models.BooleanField(
        label='Rechtliche Rechte und Schutzmaßnahmen (Mutterschutz, Kündigungsschutz, Elternzeit)',
        widget=widgets.CheckboxInput, blank=True, initial=False,
    )

    c3_plan_importance = models.IntegerField(
        label=(
            '<b>C3.</b> Wie wichtig ist es Ihrer Erfahrung nach, schon vor der Geburt '
            'einen Plan für den beruflichen Wiedereinstieg zu haben?'
        ),
        choices=[
            [1, 'Sehr wichtig – ein Plan hat mir geholfen (oder ich wünschte, ich hätte einen gehabt)'],
            [2, 'Etwas wichtig – ein guter Ausgangspunkt, aber man muss flexibel bleiben'],
            [3, 'Nicht sehr wichtig – die Realität nach der Geburt war zu anders, als dass ein Plan viel geholfen hätte'],
            [4, 'Bin nicht sicher'],
        ],
        widget=widgets.RadioSelect,
    )

    c3b_return_tip = models.LongStringField(
        label=(
            '<b>C3b.</b> Wenn Sie Ihrer Freundin einen Tipp zur Planung ihrer Rückkehr in den Beruf geben könnten, '
            'was wäre das?'
        ),
        blank=True,
    )

    # ── Section D: Knowledge Check ─────────────────────────────────────

    d1_pension_knowledge = models.IntegerField(
        label=(
            '<b>D1.</b> Angenommen, eine Frau verdient Vollzeit 3.000 € brutto im Monat. '
            'Sie arbeitet nach der Geburt ihres ersten Kindes 10 Jahre lang Teilzeit (20 Stunden/Woche). '
            'Um wie viel Euro pro Monat wird ihre gesetzliche Rente dadurch ungefähr geringer sein?'
        ),
        choices=[
            [1, 'Unter 50 € pro Monat'],
            [2, '50 – 100 € pro Monat'],
            [3, '150 – 250 € pro Monat'],
            [4, '300 – 500 € pro Monat'],
            [5, 'Weiß ich nicht / bin nicht sicher'],
        ],
        widget=widgets.RadioSelect,
    )

    d2_splitting_knowledge = models.IntegerField(
        label=(
            '<b>D2.</b> Für welche Art von Paar bringt das Ehegattensplitting '
            'den größten Steuervorteil?'
        ),
        choices=[
            [1, 'Zwei Partner mit in etwa gleichem Einkommen'],
            [2, 'Zwei Partner, bei denen einer deutlich mehr verdient als der andere'],
            [3, 'Der Vorteil ist unabhängig von der Einkommensverteilung gleich'],
            [4, 'Weiß ich nicht / bin nicht sicher'],
        ],
        widget=widgets.RadioSelect,
    )


# ══════════════════════════════════════════════════════════════════════
# Pages
# ══════════════════════════════════════════════════════════════════════

class Intro(Page):
    """Welcome screen with study purpose and instructions."""
    pass


class PageA0(Page):
    """Section A0: Demographics."""
    form_model = 'player'
    form_fields = [
        'a0_1_birth_year',
        'a0_2_income',
        'a0_3_activity',
        'a0_3_activity_other',
        'a0_3b_sector',
        'a0_3b_sector_other',
        'a0_4_thoughts_before',
        'a0_5_thoughts_wish'
    ]


class PageA_Work(Page):
    """Section A: Return to work — includes ranking A2 and conditional A3."""
    form_model = 'player'
    form_fields = [
        'a1_work_experience',
        # A2 ranking items
        'a2_rank_childcare', 'a2_rank_taxbenefit', 'a2_rank_employer',
        'a2_rank_partner', 'a2_rank_confidence', 'a2_rank_recovery',
        'a2_rank_preference', 'a2_rank_nodifficulty',
        'a2_other_text', 'a2_rank_other',
        # A3 (conditional — blank=True, JS hides it for homemaker/not-seeking)
        'a3_wishes',
        # A4
        'a4_expectation', 'a4_reason',
    ]

    @staticmethod
    def vars_for_template(player):
        # Pass activity code so the template can show/hide A3 via JavaScript
        return dict(activity=player.a0_3_activity)

    @staticmethod
    def error_message(player, values):
        # Validate A2: 1–3 items ranked, each rank used at most once
        a2_fields = [
            'a2_rank_childcare', 'a2_rank_taxbenefit', 'a2_rank_employer',
            'a2_rank_partner', 'a2_rank_confidence', 'a2_rank_recovery',
            'a2_rank_preference', 'a2_rank_nodifficulty', 'a2_rank_other',
        ]
        ranks = [values.get(f) for f in a2_fields if values.get(f) is not None]
        if len(ranks) < 1:
            return 'Bitte wählen Sie bei Frage A2 mindestens einen Faktor aus.'
        if len(ranks) > 3:
            return 'Bitte wählen Sie bei Frage A2 höchstens drei Faktoren aus.'
        if len(set(ranks)) != len(ranks):
            return 'Bitte vergeben Sie bei Frage A2 jeden Rang nur einmal.'


class PageB_Finance(Page):
    """Section B: Financial surprises — includes ranking B2."""
    form_model = 'player'
    form_fields = [
        'b1_biggest_surprise',
        # B2 ranking items
        'b2_rank_income_drop', 'b2_rank_tax_work', 'b2_rank_pension',
        'b2_rank_childcare_cost', 'b2_rank_career', 'b2_rank_daily_costs',
        'b2_rank_insurance', 'b2_rank_elterngeld', 'b2_rank_prepared',
        'b2_other_text', 'b2_rank_other',
        # B3, B4, B4b
        'b3_preparedness', 'b4_planning_horizon', 'b4b_regret',
    ]

    @staticmethod
    def error_message(player, values):
        # Validate B2: 1–3 items ranked, each rank used at most once
        b2_fields = [
            'b2_rank_income_drop', 'b2_rank_tax_work', 'b2_rank_pension',
            'b2_rank_childcare_cost', 'b2_rank_career', 'b2_rank_daily_costs',
            'b2_rank_insurance', 'b2_rank_elterngeld', 'b2_rank_prepared',
            'b2_rank_other',
        ]
        ranks = [values.get(f) for f in b2_fields if values.get(f) is not None]
        if len(ranks) < 1:
            return 'Bitte wählen Sie bei Frage B2 mindestens ein Thema aus.'
        if len(ranks) > 3:
            return 'Bitte wählen Sie bei Frage B2 höchstens drei Themen aus.'
        if len(set(ranks)) != len(ranks):
            return 'Bitte vergeben Sie bei Frage B2 jeden Rang nur einmal.'


class PageC_Advice(Page):
    """Section C: Advice for expectant parents — includes C2 multi-select (max 3)."""
    form_model = 'player'
    form_fields = [
        'c1_advice',
        # C2 checkboxes (up to 3)
        'c2_elterngeld', 'c2_tax', 'c2_pension', 'c2_childcare', 'c2_career',
        'c2_insurance', 'c2_budget', 'c2_savings', 'c2_legal',
        # C3, C3b
        'c3_plan_importance', 'c3b_return_tip',
    ]

    @staticmethod
    def error_message(player, values):
        # Validate C2: at most 3 topics selected
        c2_fields = [
            'c2_elterngeld', 'c2_tax', 'c2_pension', 'c2_childcare', 'c2_career',
            'c2_insurance', 'c2_budget', 'c2_savings', 'c2_legal',
        ]
        selected = sum(1 for f in c2_fields if values.get(f))
        if selected < 1:
            return 'Bitte wählen Sie bei Frage C2 mindestens 1 Thema aus.'
        if selected > 3:
            return 'Bitte wählen Sie bei Frage C2 maximal 3 Themen aus.'


class PageD_Knowledge(Page):
    """Section D: Knowledge check — two factual multiple-choice questions."""
    form_model = 'player'
    form_fields = ['d1_pension_knowledge', 'd2_splitting_knowledge']


class Results(Page):
    """Thank-you page shown after survey completion."""
    pass


page_sequence = [
    Intro,
    PageA0,
    PageA_Work,
    PageB_Finance,
    PageC_Advice,
    PageD_Knowledge,
    Results,
]
