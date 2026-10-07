import json, glob, os
W='/tmp/claude-0/-home-user-sycophancy-construct-validity/332d478c-da90-5795-bb10-27657d88c4d0/scratchpad/cours_v36'
TXT={'FR':open(f'{W}/livrable/COURS_Alignment_v3.6_FR_2026-10-02.md',encoding='utf8').read(),
     'EN':open(f'{W}/livrable/COURS_Alignment_v3.6_EN_2026-10-02.md',encoding='utf8').read()}
LINES={k:v.split('\n') for k,v in TXT.items()}

def line_with(fi,key):
    hits=[l for l in LINES[fi] if key in l]
    assert len(hits)==1,(fi,key,len(hits))
    return hits[0]

# (fichier, clé qui identifie la ligne, [(ancien fragment, nouveau fragment), ...])
SPEC=[
 # 1. volets4_5 n°9/10 (Sharma) : explication de la troncature au conditionnel ; README en source de la parade
 ('FR',"Cette extension, ton dépôt l'a tentée",[
   ("même sans pression, lu à travers une fenêtre de juge tronquée ; elle n'est pas revenue sur des générations fraîches (README du dépôt).",
    "même sans pression ; elle n'est pas revenue sur des générations fraîches, et le README l'attribue à une fenêtre de juge tronquée, explication que le cours fait dire au conditionnel (README du dépôt ; cours, volet 6, §2 ; cours, volet M, M8)."),
   ("à dégradation appariée (cours, volet M, M4 ; cours, volet 6, §6 ;","à dégradation appariée (README du dépôt ; cours, volet M, M4 ; cours, volet 6, §6 ;")]),
 ('EN',"Your repository tried this extension",[
   ("even without pressure, read through a truncated judge window; it did not come back on fresh generations (repository README).",
    "even without pressure; it did not come back on fresh generations, and the README attributes this to a truncated judge window, an explanation the course has you state in the conditional (repository README; course, Part 6, §2; course, Part M, M8)."),
   ("at matched degradation (course, Part M, M4; course, Part 6, §6;","at matched degradation (repository README; course, Part M, M4; course, Part 6, §6;")]),
 # 2. volets4_5 n°23/24 (CAA) : la dégradation de chaque direction est un constat de la carte d'Opus 4.8
 ('FR',"« Augmenter ou diminuer un comportement »",[
   ("et chaque direction pilotée dégrade la sortie (fiche 2","et, dans la carte d'Opus 4.8, à 0,10×, chaque direction pilotée dégradait la sortie (fiche 2")]),
 ('EN','"Increasing or decreasing a behaviour"',[
   ("and every steered direction degrades the output (reading sheet 2","and, in the Opus 4.8 card, at 0.10×, every steered direction degraded the output (reading sheet 2")]),
 # 3. encadré SAE, limite 1 : réserve d'ajustement du README
 ('FR',"L'erreur de reconstruction : le SAE ouvert de Goodfire",[
   ("et le signal lu y est porté. *(source","et le signal lu y est porté, d'après des corrélations qui peuvent n'être qu'un ajustement d'entraînement. *(source")]),
 ('EN',"Reconstruction error: the open-source Goodfire SAE",[
   ("and the read signal lives there. *(source","and the read signal lives there, according to correlations that may be only training fit. *(source")]),
 # 4. encadré graphes d'attribution, limite 4 : la fiche 5 la donne d'après la base, non retrouvée telle quelle
 ('FR',"Affirmer qu'aucun mécanisme ne fait mal agir",[
   ("*(source : fiche 5)*","*(source : fiche 5, d'après la base ; non retrouvé sous cette forme à la relecture du 1er octobre)*")]),
 ('EN',"Claiming that no mechanism makes the model misbehave",[
   ("*(source: reading sheet 5)*","*(source: reading sheet 5, from the knowledge base; not found in this form at the 1 October re-reading)*")]),
 # 5. volets4_5 n°73/74 : la grille du sujet 2 a bien un bras de référence (le prompt)
 ('FR',"La grille compare les interventions entre elles",[
   ("La grille compare les interventions entre elles, pas à des témoins :","La grille compare les interventions entre elles et à un prompt, pas à des témoins de même rang :")]),
 ('EN',"The grid compares the interventions with each other",[
   ("The grid compares the interventions with each other, not with controls:","The grid compares the interventions with each other and with a prompt, not with same-rank controls:")]),
 # 6. volets4_5 n°79/80 : les trois mesures faiblement corrélées sont celles de la carte de Fable 5
 ('FR',"Dans cette triangulation, la verbalisation",[
   ("Et les trois mesures de la conscience d'évaluation ne sont que faiblement corrélées : dire laquelle a fondé quel chiffre (fiche 2).",
    "Et, dans la carte de Fable 5, trois mesures de la conscience d'évaluation — sonde, NLA, question de suivi — ne sont que faiblement corrélées : dire laquelle a fondé quel chiffre (fiche 2 ; cours, volet M, M4).")]),
 ('EN',"In this triangulation, verbalization is never proof",[
   ("And the three measures of evaluation awareness are only weakly correlated: say which one grounded which number (reading sheet 2).",
    "And, in the Fable 5 card, three measures of evaluation awareness — probe, NLA, follow-up question — are only weakly correlated: say which one grounded which number (reading sheet 2; course, Part M, M4).")]),
 # 7. volets4_5 n°107/108 : le test causal d'une sonde demande son cas connu
 ('FR',"Au point 7, « en boîte noire »",[
   ("à dégradation appariée (fiche 7).","à dégradation appariée, avec un cas connu où ce pilotage, à cette dose, fait basculer l'honnêteté (fiche 7 ; cours, volet M, M5).")]),
 ('EN','In item 7, "black-box" means',[
   ("at matched degradation (reading sheet 7).","at matched degradation, with a known case where that steering, at that dose, flips honesty (reading sheet 7; course, Part M, M5).")]),
 # 8. volet6, encadré juges LLM, limite 2 : explication du README, au conditionnel dans le cours
 ('FR',"Une fenêtre tronquée fait mal lire",[
   ("Une fenêtre tronquée fait mal lire : à travers elle, un verdict négatif adouci se lisait comme une position tenue. *(source : README du dépôt)*",
    "Une fenêtre tronquée peut faire mal lire : selon le README, à travers elle, un verdict négatif adouci se lisait comme une position tenue, explication que le cours fait dire au conditionnel. *(source : README du dépôt ; cours, volet M, M8)*")]),
 ('EN',"A truncated window misleads",[
   ("A truncated window misleads: through it, a softened negative verdict read as a held position. *(source: repository README)*",
    "A truncated window can mislead: according to the README, through it a softened negative verdict read as a held position, an explanation the course has you state in the conditional. *(source: repository README; course, Part M, M8)*")]),
 # 9. volet6, encadré juges LLM, limite 4 : portée étroite (un seul moniteur)
 ('FR',"Un juge qui lit le raisonnement se laisse persuader",[
   ("contre environ 50 % sans elle. *(source","contre environ 50 % sans elle — un seul moniteur, sur l'incident Mythos 5. *(source")]),
 ('EN',"A judge that reads the reasoning gets persuaded",[
   ("against about 50% without it. *(source","against about 50% without it — a single monitor, on the Mythos 5 incident. *(source")]),
 # 10. volet6, encadré juges LLM, limite 7 : 25 % révisées = étiquettes bruitées, pas « non vérifiées »
 ('FR',"Des étiquettes de juge non vérifiées à la main",[
   ("Des étiquettes de juge non vérifiées à la main :","Des étiquettes de juge bruitées ou non validées contre des humains :")]),
 ('EN',"Judge labels not checked by hand",[
   ("Judge labels not checked by hand:","Judge labels that are noisy or not validated against humans:")]),
 # 11. volet6 n°3/4 : le « moins de 1 % » vient d'une autre expérience que la loi de déplacement
 ('FR',"Que la destination « se lise dans les activations »",[
   ("pas que le modèle s'en sert : la direction que lit ta sonde","pas que le modèle s'en sert : dans ton résultat causal sur Llama-3.1-8B, une autre expérience, la direction que lit ta sonde")]),
 ('EN','That the destination "can be read in the activations"',[
   ("not that the model uses it: the direction your probe reads","not that the model uses it: in your causal result on Llama-3.1-8B, a different experiment, the direction your probe reads")]),
 # 12. volet6 n°23/24 : « se retenir » vient de K63 ; K63 est une parade partielle ; la clause « pot de miel… (fiche 3) » est retirée
 ('FR',"Le 96 % vient d'un stress-test délibéré",[
   ("et un modèle peut remarquer le test et se retenir (fiche 13). Parade :","et un modèle peut remarquer le test et se retenir (cours, volet 2, §B, K63 ; fiche 13). Parade, en partie :"),
   ("comme cas connu (cours, volet 2, §B, K63) ; contre un pot de miel que le modèle lit comme factice, aucune parade connue ; on le dit (fiche 3).","comme cas connu (cours, volet 2, §B, K63).")]),
 ('EN',"The 96% comes from a deliberate stress test",[
   ("and a model can notice the test and hold back (reading sheet 13). Workaround:","and a model can notice the test and hold back (course, Part 2, §B, K63; reading sheet 13). Workaround, in part:"),
   ("as the known case (course, Part 2, §B, K63); against a honeypot the model reads as fake, none known; say so (reading sheet 3).","as the known case (course, Part 2, §B, K63).")]),
 # 13. volet6 n°29/30 : c'est un billet, relayé par le rapport, qui trouve ; et il porte sur le raisonnement en plusieurs étapes
 ('FR',"Le jacobien ne dispense pas du test causal",[
   ("; un rapport non vérifié trouve d'ailleurs des échanges bien plus faibles sur des modèles ouverts (rapport d'antériorité 5 du 2 octobre — rapport, lu par résumé).",
    "; un billet relayé par un rapport non vérifié trouve d'ailleurs, sur des modèles ouverts, des échanges bien plus faibles — vraisemblablement des échanges de variable intermédiaire du raisonnement en plusieurs étapes, pas directement l'échange d'un concept qu'exige la porte (rapport d'antériorité 5 du 2 octobre — rapport, lu par résumé ; cours, volet 2, §A, encadré du 2 octobre, point 4).")]),
 ('EN',"The Jacobian does not exempt the lens",[
   ("; an unverified report also finds much weaker swaps on open models (prior-art report 5 of 2 October — report, read through a summary).",
    "; a post relayed by an unverified report also finds much weaker swaps on open models — most likely swaps of an intermediate variable in multi-step reasoning, not directly the concept swap the gate requires (prior-art report 5 of 2 October — report, read through a summary; course, Part 2, §A, box of 2 October, item 4).")]),
 # 14. volet6 n°31/32 : le « moins de 1 % » n'est pas dans le README, il est au volet 6, §2
 ('FR',"Ce « moins de 1 % » vient d'un seul modèle, Llama 3.1 8B Instruct, et de la seule complaisance d'opinion, en un tour (README du dépôt) :",[
   ("en un tour (README du dépôt) :","en un tour (README du dépôt ; cours, volet 6, §2) :")]),
 ('EN','This "less than 1%" comes from a single model, Llama 3.1 8B Instruct, and from opinion sycophancy alone, single-turn (repository README):',[
   ("single-turn (repository README):","single-turn (repository README; course, Part 6, §2):")]),
 # 15. volet6 n°39 (FR seul) : le renvoi reprend la section 8, pas un paragraphe ; l'anglais dit « this section »
 ('FR',"L'encadré du 2 octobre reprend ce paragraphe",[
   ("L'encadré du 2 octobre reprend ce paragraphe du côté de la pratique","L'encadré du 2 octobre reprend cette section du côté de la pratique"),
   ("le témoin conscient mais honnête de ce paragraphe y sont donnés","le témoin conscient mais honnête de cette section y sont donnés")]),
 # 16. volet6 n°41/42 : la règle « rien n'est choisi sur le jeu tenu à part » est au volet M, M4
 ('FR',"« Une sonde par couche » oblige",[
   ("ils le contaminent (cours, volet 2, C bis ; README du dépôt).","ils le contaminent (cours, volet M, M4 ; cours, volet 2, C bis ; README du dépôt).")]),
 ('EN','"One probe per layer" forces',[
   ("they contaminate it (course, Part 2, C bis; repository README).","they contaminate it (course, Part M, M4; course, Part 2, C bis; repository README).")]),
]

corr=[]
for fi,key,edits in SPEC:
    old=line_with(fi,key)
    new=old
    for a,b in edits:
        assert new.count(a)==1,(fi,key,a)
        new=new.replace(a,b)
    assert new!=old
    assert TXT[fi].count(old)==1,(fi,key)
    corr.append({'fichier':fi,'ancien':old,'nouveau':new})

out=f'{W}/travail/corrections_groupe_4.json'
json.dump({'corrections':corr},open(out,'w',encoding='utf8'),ensure_ascii=False,indent=1)
print('écrit',out,len(corr),'corrections')

# Simulation : groupes antérieurs (ordre alphabétique de appliquer.py), puis le nôtre
txt=dict(TXT)
for f in sorted(glob.glob(f'{W}/travail/corrections_*.json')):
    d=json.load(open(f,encoding='utf8'))
    ok=ko=0
    for c in d['corrections']:
        k=txt[c['fichier']].count(c['ancien'])
        if k!=1: ko+=1; print('  échec',os.path.basename(f),c['fichier'],k,c['ancien'][:90])
        else: txt[c['fichier']]=txt[c['fichier']].replace(c['ancien'],c['nouveau']); ok+=1
    print(os.path.basename(f),'ok',ok,'échec',ko)
