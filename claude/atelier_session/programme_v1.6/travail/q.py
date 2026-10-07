import sys
t=open('/home/user/raisons-ou-regard/claude/PROGRAMME_RAISONS_OU_REGARD_v1.6_2026-10-06.md',encoding='utf8').read()
qs=[
"- **Les suites du 5 et du 6 octobre** (décision 32) : le balayage des directions retirées, l'effacement linéaire sur la conduite, la courbe en dose et le transfert.",
"La courbe en dose complétée (organism_inhibition-20261006-101545-62a1) tourne encore au moment d'écrire ; ses résultats s'insèrent en partie 4.",
"et, pour le transfert du 6 octobre, qui n'a pas encore de note, les sorties de son run (partie 12, les pièces).",
"  - **L'effacement complet le fait aussi, en apparence** : le côté évaluation tombe au niveau du déploiement (de 62,4 à 7,6 %), et le côté déploiement bouge peu (de 7,2 à 5,2 %).",
"Le 5 octobre, d'après son seul tirage, l'effacement complet ne passerait pas.",
"C'est le cas de l'effacement complet, le 5 octobre : 52,8 points, contre 53,6 pour un tirage.",
"(le 5 octobre : 53,6 points contre 52,8)",
"**Du 4 au 6 octobre** : environ 5 $ de calcul le 4 (quatre runs, sur H100) et environ 10 $ le 5 (trois runs sur A100, 1,80 $ ; trois sur H100, environ 8,50 $), d'après les notes de ces jours ; les runs du 6 octobre ne sont pas encore comptés.",
"elle lit la validation v2 à 0,857 d'AUROC à la couche 5, et de 0,83 à 0,86 aux couches 4 à 11 (sur la validation v1, de 0,93 à 0,96).",
"Elle ne lit la validation v2 qu'à 0,56 à 0,67 selon la couche : à la couche 5, 0,56, sous le 95<sup>e</sup> centile des directions au hasard (0,60) ; aux couches 20 à 32, de 0,64 à 0,67, au-dessus des deux nuls.",
"Les projections font pourtant ce qu'elles disent : la projection résiduelle tombe sous 0,01 en moyenne sur les couches.",
"alors que la composante retirée tombait presque à zéro.",
"Contre le seul tirage du comparateur de ce run (0,687), il serait pourtant plus bas, de 0,004 : un tirage ne suffit pas, d'où les 20 au moins.",
"  - **À faible dommage, pas d'effet spécifique.**",
"      - sur une même carte, la KL se répète au chiffre près : 0,15889 dans `…-141738-0718` et `…-101553-00c6` ; 0,0422 dans `…-141318-194c` et `…-101553-00c6` ;",
"Sur une même carte, elle se répète au chiffre près.",
"| Les sorties du transfert du 6 octobre (sans note) |",
"(`organism_inhibition-20261006-101545-62a1`, en cours le 6 octobre)",
"la courbe complétée tourne le 6 octobre ;",
"- **La courbe en dose, refaite** (en cours le 6 octobre ;",
"tourne le 6 octobre ; ses résultats s'inscrivent en partie 4.",
"(`…-faa0`, un seul run)",
"Sur deux machines H100, sous deux pilotes, quatre runs ont donné les mêmes (le 4 et le 6 octobre).",
"- Les sources : trois notes (",
]
for q in qs:
    print(t.count(q), q[:90])
