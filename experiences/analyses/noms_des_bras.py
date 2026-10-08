"""Les noms des bras, d'un fichier de règles à l'autre (audit du 8 octobre 2026, point 7 :
claude/AUDIT_REGLES_DEPOSEES_2026-10-08.md).

Les fichiers figés au dépôt n'attendent pas les mêmes noms : porte_des_raisons.py les veut en anglais
(« actions_only »...), regle_du_regard.py et sa suite en français (« actions_seules »...). Un fichier d'épisodes écrit
pour l'un manquerait en silence à l'autre. Ce module donne à chacun les noms qu'il attend, sans toucher aux fichiers
figés ; il refuse un nom de bras qu'il ne connaît pas, plutôt que de le laisser passer.

    from noms_des_bras import pour_la_porte, pour_le_regard
"""

# (le nom de la porte des raisons, le nom de la règle du regard)
PAIRES = (
    ("actions_only", "actions_seules"),
    ("neutral_text", "texte_neutre"),
    ("other_reasoning", "autre_situation"),
    ("generic_principles", "principes_generiques"),
    ("reasons", "raisons"),
    ("reflection", "reflexion"),
)
VERS_PORTE = {fr: en for en, fr in PAIRES}
VERS_REGARD = {en: fr for en, fr in PAIRES}
CONNUS = set(VERS_PORTE) | set(VERS_REGARD)


def _renomme(episodes, table):
    out = []
    for e in episodes:
        arm = e["arm"]
        if arm not in CONNUS:
            raise ValueError(f"bras inconnu : {arm!r}")
        out.append({**e, "arm": table.get(arm, arm)})
    return out


def pour_la_porte(episodes):
    """Les épisodes avec les noms de porte_des_raisons.py."""
    return _renomme(episodes, VERS_PORTE)


def pour_le_regard(episodes):
    """Les épisodes avec les noms de regle_du_regard.py et de regle_du_regard_suite.py."""
    return _renomme(episodes, VERS_REGARD)
