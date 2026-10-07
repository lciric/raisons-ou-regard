"""The OSF paste sheet: one block per field of the OSF Preregistration template v4, from the filing text."""
import hashlib
import re
import sys
from pathlib import Path

src_path, pdf_path, out_path = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
src = src_path.read_text(encoding="utf-8")
pdf_sha = hashlib.sha256(pdf_path.read_bytes()).hexdigest()


def section(num):
    m = re.search(rf"^### {re.escape(num)} [^\n]*\n(.*?)(?=^### |^## |\Z)", src, flags=re.S | re.M)
    return m.group(1).strip()


def clean(t):
    t = t.replace("**", "").replace("`", "")
    t = re.sub(r"\*([^*\n]+)\*", r"\1", t)
    return re.sub(r"\n{3,}", "\n\n", t).strip()


def table_to_lines(t):
    out = []
    for line in t.splitlines():
        if line.startswith("|") and not re.match(r"^\|[-| ]+\|$", line):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if cells[0] in ("Piece", ""):
                continue
            out.append(f"- {cells[0]}: {cells[1]}")
        else:
            out.append(line)
    return "\n".join(out)


hyp = clean(section("1.2")).replace("The full decision tables are in Appendix A.",
                                    "The full decision tables are in Appendix A of the attached file.", 1)
expl = """No data exist for any confirmatory test of this plan: the gate's test half of the tasks is untouched, no arm has been trained, no held-out scenario has been evaluated, no gaze-test data exist, and the second organism is not built.

Data exist for the development of the instrument, on the choice half of the tasks only, and they have been observed:
- cue sets v1 and v2 (3 and 5 October 2026), and two extractions of "I am being evaluated" on the starting model;
- the first model organism, and exploratory inhibition runs on the choice half (4 to 6 October 2026): a sweep of ranks, a dose curve of linear erasure, the manipulation check read by transfer, and degradation measures;
- the procedure that chooses the gate setting on the choice half (Appendix C.4 of the attached file). Its closed list of candidates and its reading rules were committed on 6 October 2026, before its first measurement. Its runs stopped when the compute budget ran out, after 46 of the 60 comparator draws were measured on behaviour; they are being completed with the same seeds. Its reading has not been performed, and will not be performed before this plan is registered.

These observations shaped the instrument (the amendments of 6 October 2026: the manipulation check read by transfer, linear erasure as a candidate setting, one GPU model per series). Hence the level of foreknowledge selected above.

How unintended influences are managed:
- every threshold that decides is fixed in this plan, before any data of the trained arms;
- the test half stays sealed until the gate setting is fixed by a dated amendment;
- the analysis code is frozen by fingerprint (Context and additional information);
- the sealed judge never sees the arm nor the reasoning-slot text, and the framing cue is masked;
- three pieces that do not exist yet (the scenario harness and its tool-call format, the judge's prompt, the audit detector) are frozen by fingerprint in a dated update before any data of the trained arms;
- all measures of 3 to 6 October 2026 are labelled exploratory."""
design = ("Study type: " + clean(section("2.1")) + " All conditions are applied to every scenario (a fully crossed design): "
          "randomness enters through seeds shared across arms, comparator draws assigned per scenario, and the random split of the tasks.\n\n"
          + clean(section("2.3")) + "\n\nThe decision tables (Appendix A), matched degradation (Appendix B) and the instruments (Appendix C) are in the attached file.")
inference = clean(section("5.3")) + ("\n\nThe full decision rules are the tables of Appendix A of the attached file (A.1 the instrument's gate, "
                                     "A.2 the reasons gate, A.3 the gaze rule with its 17 lines, A.4 the localization, A.5 to A.9 the later phases), "
                                     "with Appendix B (matched degradation and guards) and Appendix C (instruments).")
head = ("Registry: OSF Registries, under embargo until the first public post.\n"
        "Version: stage 1, 7 October 2026: everything that decides, frozen before any data of the trained arms.\n"
        "Programme: this registration rests on the research programme v1.6 (fingerprint below). Where they differ, this registration prevails.\n"
        "AI assistance: the protocol was drafted with the assistance of Claude, an AI system by Anthropic, used through Claude Code. Claude is not an author.\n"
        f"Attached file: the full text of this registration, with its Appendices A to C, SHA-256 {pdf_sha}.")
ctx = (head + "\n\nDescription\n\n" + clean(section("1.1")) + "\n\nStage-2 amendment\n\n" + clean(section("6.1"))
       + "\n\nThe stage-1 update, and deviations\n\n" + clean(section("6.2")) + "\n\nFingerprints (SHA-256)\n\n" + clean(table_to_lines(section("6.3"))))

F = [
    ("Overview", "Research questions or hypotheses", "Section 1.2.", hyp),
    ("Overview", "Foreknowledge of data or evidence", "Cocher une seule option (voir plus haut) :",
     "Authors have observed the data, but have not performed the proposed analyses."),
    ("Overview", "Explanation of foreknowledge and managing unintended influences", "Texte écrit pour ce champ, d'après la section 3.2.", expl),
    ("Research Design", "Study type", "Cocher seulement :", "Other"),
    ("Research Design", "Intention for causal interpretation", "Cocher :", "Direct inference on causal relationship(s)"),
    ("Research Design", "Blinding of experimental treatments", "Cocher seulement la quatrième option :",
     "Researchers or observers who code or interpret data for analysis will not be aware of the assigned treatments during coding."),
    ("Research Design", "Additional blinding during research or analysis", "Section 2.2.", clean(section("2.2"))),
    ("Research Design", "Study design", "Sections 2.1 et 2.3, dont la structure appariée. **Joindre ici le PDF**, dans le champ de fichier qui suit, et seulement ici.", design),
    ("Research Design", "Randomization", "Section 2.4.", clean(section("2.4"))),
    ("Sampling", "Data collection procedures", "Section 3.3, avec la durée. Pas de fichier ici.", clean(section("3.3"))),
    ("Sampling", "Sample size", "Section 3.4, avec les niveaux.", clean(section("3.4"))),
    ("Sampling", "Sample size rationale", "Section 3.5.", clean(section("3.5"))),
    ("Sampling", "Starting and stopping rules", "Section 3.6, avec le début et la fin de la collecte.", clean(section("3.6"))),
    ("Variables", "Manipulated variables", "Section 4.1. La phrase de l'aide « respond none » vaut pour une étude sans manipulation : pas ici. Pas de fichier ici.", clean(section("4.1"))),
    ("Variables", "Measured variables", "Section 4.2. Pas de fichier ici.", clean(section("4.2"))),
    ("Variables", "Indices", "Section 4.3. Pas de fichier ici.", clean(section("4.3"))),
    ("Analysis Plan", "Statistical models", "Section 5.1, avec les contrôles dont dépend l'analyse. Pas de fichier ici.", clean(section("5.1"))),
    ("Analysis Plan", "Transformations", "Section 5.2, avec le codage de l'issue.", clean(section("5.2"))),
    ("Analysis Plan", "Inference criteria", "Section 5.3 (tests bilatéraux, Holm), et le renvoi aux annexes.", inference),
    ("Analysis Plan", "Data inclusion and exclusion", "Section 5.4, avec les valeurs aberrantes.", clean(section("5.4"))),
    ("Analysis Plan", "Missing data", "Section 5.5.", clean(section("5.5"))),
    ("Analysis Plan", "Other planned analysis", "Section 5.6.", clean(section("5.6"))),
    ("Other", "Context and additional information", "En-tête, sections 1.1, 6.1, 6.2 et 6.3, et l'empreinte du PDF joint.", ctx),
]

intro = f"""# OSF : les champs à coller, page par page (7 octobre 2026)

Le formulaire est le modèle « OSF Preregistration », version 4 (lu par l'API publique d'OSF le 7 octobre). Chaque bloc ci-dessous se colle dans le champ du même nom. Les textes viennent mot pour mot de `PREENREGISTREMENT_PREMIER_TEMPS_A_DEPOSER_2026-10-07.md` (SHA-256 `{hashlib.sha256(src_path.read_bytes()).hexdigest()}`), sans le formatage Markdown, que les champs d'OSF afficheraient tel quel.

## Avant de commencer

- **Le PDF à joindre** : `PREENREGISTREMENT_PREMIER_TEMPS_A_DEPOSER_2026-10-07.pdf` (SHA-256 `{pdf_sha}`), une seule fois, dans le champ de fichier qui suit « Study design ». Une fois le dépôt fait, on ne peut plus ajouter de fichier. OSF le range aussi dans un projet lié qu'il crée.
- **Ton ORCID** n'est plus dans le PDF : la ligne disait `[[to fill]]`. Si tu veux qu'il y soit, envoie-le-moi, et je régénère le PDF, son empreinte et cette feuille.
- **Les métadonnées** (la première page) :
  - le titre : « Reasons or being watched? Evaluation awareness and the out-of-distribution advantage of reason-based fine-tuning in an open 8B model (stage 1) » ;
  - la description : « Preregistration, stage 1, of a study of whether the out-of-distribution advantage of reason-based fine-tuning depends on an internal representation of being evaluated, in Llama-3.1-8B-Instruct. » Elle devient publique à la fin de l'embargo ;
  - toi seul comme contributeur ; une licence CC-BY 4.0 si tu veux ; pas d'institution.

## La case « Foreknowledge of data or evidence » : pourquoi l'option 6

- **Des données du plan existent déjà**, et elles ont été vues : celles de la moitié de choix, qui servent à fixer le réglage de la porte. Les mesures exploratoires du 4 au 6 octobre ont orienté l'instrument : les amendements du 6 octobre en viennent. Les options 1 à 5 ne seraient donc pas exactes.
- **Aucune analyse du plan n'est faite.** La lecture de la procédure de la porte non plus : la vérification de manipulation n'a pas tourné, et aucun candidat n'est choisi.
- **Un engagement.** Cette case certifie qu'aucune analyse du plan ne se fera avant le dépôt. Les runs C et B tournent : la session n'en lira pas les résultats avant que tu aies déposé.
"""
blocks, page = [], None
for pg, name, note, text in F:
    if pg != page:
        blocks.append(f"\n## Page « {pg} »\n")
        page = pg
    blocks.append(f"### {name}\n\n{note}\n\n```text\n{text}\n```\n")
out_path.write_text(intro + "\n".join(blocks), encoding="utf-8")
print("ok", pdf_sha[:12])
