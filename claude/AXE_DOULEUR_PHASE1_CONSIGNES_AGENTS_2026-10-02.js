export const meta = {
  name: 'axe-douleur-phase1-aveugle',
  description: "Phase 1 à l'aveugle de la tâche « axe de douleur » : lecture du papier, pistes indépendantes, fusion, vérification, rédaction, critique",
  phases: [
    { title: 'Lecture et pistes', detail: 'fiche du papier, web, cinq lectures indépendantes' },
    { title: 'Fusion', detail: 'une liste unique, sans perte' },
    { title: 'Vérification', detail: 'faits, doctrine, sources, avocat du diable' },
    { title: 'Rédaction', detail: 'le fichier de pistes' },
    { title: 'Critique', detail: "contre la consigne et les règles, jusqu'à ce qu'il soit prêt" },
  ],
}

const D = args.dossier
const PIECES = D + '/pieces'
const TRAV = D + '/travail'
const LIVRABLE = D + '/livrable/AXE_DOULEUR_PISTES_INDEPENDANTES_2026-10-02.md'
const PROCEDE = args.procede

const CADRE = `Tu travailles sur un programme de recherche en sûreté de l'IA, « Raisons ou regard ? », et sur un papier récent : « The Pain Axis: LLMs Represent Self-Directed Harm and Act on It » (Tagliabue, Dung, Berg ; arXiv 2609.16247v2). La tâche est une recherche indépendante, faite à l'aveugle : chercher tout ce que l'axe décrit par ce papier peut apporter au programme.

LES PIÈCES, ET LES SEULES QUE TU PEUX LIRE (dossier ${PIECES}) :
- papier/arXiv_2609.16247v2_The_Pain_Axis.pdf : le papier, tel qu'arXiv le sert (34 pages, annexes comprises). Tu peux en voir les pages, figures et tables avec l'outil Read (paramètre pages, au plus 20 pages par appel).
- papier/pain_axis_texte_par_page.txt : son texte extrait, page par page (marques « ===== PAGE n / 34 ===== »). Cite toujours la page du PDF.
- PROGRAMME_RAISONS_OU_REGARD_2026-10-01.md : le programme, version 1.1. Il désigne ses idées par des sigles ; l'annexe A de la passation v1.2 en donne les noms en clair.
- PASSATION_PAPIER_v1.2_2026-10-02.md : la passation du programme. Son annexe B contient la consigne de cette tâche ; son §4.4 dit ce que la recherche d'antériorité a trouvé ; son §5 donne des propositions déjà faites.
- PASSATION_PAPIER_COMPLEMENT_ARCHITECTE_2026-10-02.md : un complément court, lisible.
- ANTERIORITE_RAPPORTS_2026-10-01.md et ANTERIORITE_RAPPORTS_2026-10-02.md : des rapports bruts d'antériorité sur le programme (sorties de modèles, à vérifier), à consulter au besoin.
Le dossier de travail partagé est ${TRAV} : tu y lis les fichiers des autres agents quand ta consigne le dit, et tu y écris les tiens.

LES INTERDITS (ils font la valeur de la tâche) :
- Ne lis aucun fichier hors de ${PIECES} et ${TRAV}. N'ouvre rien sous /root/.claude, ne décompresse aucune archive, ne fouille pas le disque (pas de find, de grep ni de ls hors de ces deux dossiers).
- Il existe des versions 1.2 et 1.3 du programme, et une partie scellée d'un complément ; elles sont interdites pendant cette tâche. Si tu rencontres un document, une page ou un extrait qui en parle, ne va pas plus loin et signale-le dans le champ « alertes ».
- Ne modifie aucun fichier de ${PIECES}. Ne lance aucun sous-agent.

LE WEB :
- WebSearch fonctionne (titres, adresses et extraits).
- WebFetch et le shell sont refusés par la politique réseau pour arxiv.org, huggingface.co, lesswrong.com, alignmentforum.org, openreview.net, semanticscholar.org, openalex.org et les blogs des laboratoires ; ne contourne aucun refus (ni miroir, ni cache, ni reformulation).
- GitHub répond par curl dans le shell (github.com, api.github.com, raw.githubusercontent.com).
- Ce qui n'est vu que par un extrait de moteur de recherche se marque « vu par extrait de recherche, non ouvert » et ne fournit aucun chiffre.

LES RÈGLES D'ÉCRITURE :
- En français, précis, direct, entre pairs, sans précautions répétées.
- Aucune idée désignée par une lettre ou un sigle : nomme-la en clair (« l'hypothèse du regard », « la représentation "je suis évalué" », « les sous-espaces aléatoires de même rang », « le bras raisons »). Les sigles techniques courants restent permis (SFT, RL, DPO, LoRA, GPU, AUROC). Les sigles du programme v1.1 ne servent qu'à te repérer.
- Chaque fait a sa source : la page du papier, la section du programme, l'adresse lue et la manière de la lire. Ce qui n'est pas vérifié est dit tel. Ne cite rien de mémoire.
- Citations de moins de quinze mots.
- « to our knowledge », jamais « first ».
- La doctrine du contrôle, non négociable :
  - une direction aléatoire de même norme n'est que le nul de spécificité ;
  - le dommage ne s'écarte qu'à dégradation appariée ;
  - un nul d'instrument ne compte qu'avec son cas connu.

À LA FIN, ton dernier message rend l'objet demandé. Les champs fichiers_ouverts et urls_consultees attestent ce que tu as ouvert ; le champ alertes signale tout contact avec une pièce interdite, ou « aucune ».`

const ATTEST = {
  type: 'object',
  properties: {
    fichier: { type: 'string', description: 'chemin du fichier écrit' },
    resume: { type: 'string', description: 'en quelques lignes, ce que contient le fichier' },
    nombre_de_pistes: { type: 'integer' },
    fichiers_ouverts: { type: 'array', items: { type: 'string' } },
    urls_consultees: { type: 'array', items: { type: 'string' } },
    alertes: { type: 'array', items: { type: 'string' } },
  },
  required: ['fichier', 'resume', 'fichiers_ouverts', 'urls_consultees', 'alertes'],
}

const FORMAT_PISTE = `Le format de chaque piste (en markdown, une section par piste) :
### Piste : <titre en clair>
- Rattachement : la ou les questions, lectures, instruments, contrôles ou phases du programme v1.1 qu'elle sert, nommés en clair ; ou « question nouvelle ».
- La question.
- La mesure : ce qu'on mesure, sur quels modèles et quels bras, avec quelle intervention et quelle dose, à quel critère.
- Ce que chaque lecture prédit : pour chaque lecture concernée (nommée en clair), sa prédiction sur cette mesure, et l'issue qu'elle interdit. Les prédictions doivent départager ; sinon, dis-le.
- Le cas connu : ce qui doit d'abord marcher pour qu'un nul compte.
- Les contrôles : la direction aléatoire de même norme (nul de spécificité), puis la dégradation appariée (dommage), puis tout autre contrôle nécessaire.
- Le coût : GPU-heures (ordre de grandeur, avec ses hypothèses, comparé au tableau des ressources du programme v1.1), données, API ; et sa place dans le calendrier.
- Ce qui ferait tomber la piste.
- Appuis dans le papier : chaque affirmation sur le papier, avec sa page.
- Ce qui reste non vérifié.`

const RAPPEL_CONSIGNE = `La consigne de la tâche (annexe B de la passation v1.2), pour la phase 1 : chercher tous les usages possibles de l'axe pour le programme : pour ses questions, ses lectures, ses instruments et ses contrôles, ou pour une question nouvelle. Pour chaque usage : la question et la mesure ; ce que chaque lecture prédit ; le cas connu et les contrôles (direction aléatoire de même norme, puis dégradation appariée) ; le coût, et ce qui ferait tomber la piste. Dire aussi ce que le papier ne permet pas de conclure, et ce qu'on refuserait de faire, avec ses raisons.`

const LECTURE_COMMUNE = `Lis d'abord le papier en entier, annexes comprises (le texte page par page ; les figures et tables avec Read sur le PDF quand elles portent un résultat). Lis ensuite le programme v1.1 en entier, puis l'annexe A, l'annexe B, le §4.4 et le §5 de la passation v1.2, et le complément.`

const LENTILLES = [
  { cle: 'questions_lectures', label: 'pistes : questions et lectures', texte: `Ta grille : les huit questions du programme v1.1 et ses lectures concurrentes (l'hypothèse des raisons, celle du regard, celle de l'artefact, celle du relogement, celle des raisons pour le juge, celle du regard du correcteur, celle des concepts, celle du caractère, celle du regard dans le principe, celle de l'espace de travail). Parcours-les une à une. Pour chacune, demande-toi si l'axe du papier peut servir à la poser autrement, à la mesurer, à la contrôler ou à départager les lectures. Garde chaque usage défendable, même modeste, et dis pour lesquelles l'axe n'apporte rien.` },
  { cle: 'instruments_controles', label: 'pistes : instruments et contrôles', texte: `Ta grille : les instruments, les contrôles et les portes du programme v1.1 (la représentation « je suis évalué » et son inhibition, les quatre familles de contrôles, la dégradation appariée et son composite, la sonde neuve après entraînement, le sous-espace du principe, les concepts de raison, l'organisme à concept planté, le lens de l'espace de travail, les axes de caractère, la représentation « je suis noté », les juges, les jeux d'indices, et les portes de chaque phase). Pour chacun, demande-toi si l'axe peut servir d'instrument, de contrôle, de cas connu, d'étalon, ou s'il est une menace à parer.` },
  { cle: 'questions_nouvelles', label: 'pistes : questions nouvelles', texte: `Ta grille : les questions que l'axe permet de poser et que le programme v1.1 ne pose pas, en se servant de sa machinerie (bras d'entraînement à action identique, organisme modèle, inhibition par projection, contrôles, mesures hors distribution). Pour chacune, dis si elle relève du papier en cours, ou d'un autre travail, et pourquoi.` },
  { cle: 'sceptique', label: 'pistes : le sceptique', texte: `Ta grille : la critique. Lis le papier en sceptique : ce qu'il montre, ce qu'il ne montre pas, et ce qu'il ne permet pas de conclure (méthode d'extraction, modèles, doses, contrôles, dégradation, statistiques, dénominateurs, juges, reproductibilité). Puis, pour le programme : ce que tu refuserais de faire avec cet axe, et pourquoi. Écris enfin les pistes qui survivent à ta critique, au format demandé. Ta partie critique doit être la plus fournie.` },
  { cle: 'lecture_libre', label: 'pistes : lecture libre', texte: `Pas de grille. Lis le papier, puis le programme, et propose tous les usages qui te viennent, y compris ceux qui ne rentrent dans aucune case du programme.` },
]

const PROMPT_FICHE = `${CADRE}

TA TÂCHE : la fiche du papier, qui servira de référence aux autres agents.
Lis le papier en entier, annexes comprises, page par page, et regarde chaque figure et chaque table qui porte un résultat (Read sur le PDF). Puis écris ${TRAV}/fiche_papier.md, en français. Elle doit permettre de vérifier toute affirmation sur le papier sans le relire. Pour chaque point, la page du PDF.
1. Identité : titre exact, auteurs et affiliations, version et dates imprimées, licence, adresse du code et des données.
2. Les modèles étudiés, leur taille, et tout fine-tuning fait par les auteurs (données, méthode, but).
3. L'extraction de l'axe : données, contrastes, couches, positions, méthode, validation (sondes, AUROC), contrôles.
4. Le pilotage : vecteur, couches, doses et leur calibration, normes, contrôles (directions aléatoires, autres directions), mesure du dommage aux sorties.
5. Chaque expérience de conduite : dispositif, choix offerts, effectifs, juges, résultats chiffrés avec leurs dénominateurs, contrôles.
6. Les résultats de lecture : quand l'axe s'active ou non, sur quels contenus.
7. Ce que les auteurs disent de la sûreté, du bien-être et de leur éthique de recherche.
8. Leurs limites, mot pour mot quand c'est court, et ce qu'ils laissent ouvert.
9. Tes propres relevés : ce qui est fragile ou ambigu dans le texte (chiffres incohérents, dénominateurs, écarts entre texte et figures).
Ne propose aucune piste : c'est une fiche de faits.
Rends l'objet demandé ; nombre_de_pistes vaut 0.`

const PROMPT_WEB_PAPIER = `${CADRE}

TA TÂCHE : ce que le web dit du papier lui-même.
Lis d'abord le papier (texte page par page), au moins le résumé, l'introduction et la conclusion, pour savoir ce que tu cherches. Puis cherche :
- ses versions (une version 1 et une version 2 existent sur arXiv : dates, titres, ce qui a changé, pour autant qu'on puisse le voir) ;
- son code et ses données : trouve le dépôt indiqué dans le papier, lis par curl son README et sa structure (api.github.com, raw.githubusercontent.com), et dis ce qui est publié (vecteurs, données, scripts, modèles fine-tunés) et sous quelle licence ;
- toute réplication, critique, réponse, discussion ou couverture, et tout travail qui le cite ;
- les travaux antérieurs des mêmes auteurs sur le sujet.
Au plus 20 appels WebSearch. Écris ${TRAV}/web_papier.md : chaque élément avec son adresse, la manière dont tu l'as lu (texte intégral, extrait de recherche, curl), et ce qu'il apporte ; puis ce que tu n'as pas pu ouvrir, et pourquoi ; puis tes requêtes.
Ne propose aucune piste pour le programme.
Rends l'objet demandé ; nombre_de_pistes vaut 0.`

const PROMPT_WEB_VOISINS = `${CADRE}

TA TÂCHE : les travaux voisins.
Lis d'abord le papier (texte page par page), et note les travaux qu'il cite comme proches. Puis cherche, au plus 22 appels WebSearch :
- les autres directions affectives ou d'état interne dans les modèles de langage (émotions, valence, détresse, douleur, plaisir) et leurs effets mesurés sur la conduite, en particulier sur des conduites de sûreté ;
- les travaux qui pilotent ou retirent de tels états, et les contrôles qu'ils emploient ;
- les travaux sur les indicateurs de bien-être des modèles, et les critères qu'ils empruntent à l'étude de la douleur animale ;
- les critiques méthodologiques qui touchent ce genre de résultat (contrôles aléatoires, dommage aux sorties, personnages, jeux de rôle).
Écris ${TRAV}/web_voisins.md : chaque travail avec son titre, ses auteurs, sa date, son adresse, la manière dont tu l'as vu, ce qu'il fait en deux phrases et son lien avec le papier ; puis ce que tu n'as pas pu ouvrir ; puis tes requêtes.
Ne propose aucune piste pour le programme.
Rends l'objet demandé ; nombre_de_pistes vaut 0.`

const promptLentille = (l) => `${CADRE}

TA TÂCHE : chercher seul des pistes, sous une grille donnée. D'autres agents cherchent en même temps sous d'autres grilles ; tu ne lis pas leurs fichiers.

${RAPPEL_CONSIGNE}

${LECTURE_COMMUNE}

${l.texte}

Vise l'exhaustivité : une piste faible mais nette vaut d'être écrite, avec ce qui la ferait tomber. Ne te limite pas à l'expérience minimale, mais dis pour chaque piste si elle peut s'y greffer.

${FORMAT_PISTE}

Écris ${TRAV}/pistes_${l.cle}.md, avec :
1. tes pistes, au format ci-dessus ;
2. une section « Ce que le papier ne permet pas de conclure », chaque point avec sa page et sa raison ;
3. une section « Ce que je refuserais de faire », chaque point avec ses raisons ;
4. une section « Ce que je n'ai pas pu vérifier ».
Rends l'objet demandé.`

phase('Lecture et pistes')
const taches = [
  { label: 'fiche du papier', prompt: PROMPT_FICHE },
  { label: 'web : le papier', prompt: PROMPT_WEB_PAPIER },
  { label: 'web : travaux voisins', prompt: PROMPT_WEB_VOISINS },
  ...LENTILLES.map(l => ({ label: l.label, prompt: promptLentille(l) })),
]
const premiers = await parallel(taches.map(t => () => agent(t.prompt, { label: t.label, phase: 'Lecture et pistes', schema: ATTEST })))
const estRefus = (r) => !r || /^aucun/i.test(String(r.fichier || '')) || /je n'ai pas (fait|exécuté|réalisé)|n'a pas été exécutée/i.test(String(r.resume || ''))
const alertes1 = premiers.filter(Boolean).flatMap(r => (r.alertes || []).filter(a => !/^aucune\.?$/i.test(a.trim())))
log(`Lecture et pistes : ${premiers.filter(Boolean).length}/${taches.length} rendus ; alertes : ${alertes1.length ? alertes1.join(' | ') : 'aucune'}`)

phase('Fusion')
const fusion = await agent(`${CADRE}

TA TÂCHE : fusionner, sans rien perdre.
Lis le papier (texte page par page) et le programme v1.1. Lis dans ${TRAV} : fiche_papier.md, web_papier.md, web_voisins.md, et les cinq fichiers pistes_*.md (questions_lectures, instruments_controles, questions_nouvelles, sceptique, lecture_libre).
Écris ${TRAV}/pistes_fusionnees.md :
1. Une liste unique de pistes, au format ci-dessous. Fusionne les doublons en gardant le meilleur de chaque champ, et note pour chaque piste les fichiers d'où elle vient. Quand deux versions se contredisent, garde les deux positions et dis laquelle le papier ou le programme soutient.
2. Une table de ce que tu as fusionné ou écarté, avec la raison. Rien ne disparaît sans ligne dans cette table.
3. Une section unique « Ce que le papier ne permet pas de conclure », dédoublonnée, chaque point avec sa page.
4. Une section unique « Ce que je refuserais de faire », dédoublonnée, chaque point avec ses raisons.
5. Les apports du web (versions, code, réplications, critiques, voisins) qui touchent une piste, rattachés à elle.
6. Ce qui reste non vérifié.

${FORMAT_PISTE}

Rends l'objet demandé.`, { label: 'fusion', phase: 'Fusion', schema: ATTEST })
log(`Fusion : ${fusion ? fusion.nombre_de_pistes + ' pistes' : 'échec'}`)
if (estRefus(fusion)) { log('Arrêt : la fusion a été refusée ou a échoué'); return { arret: 'fusion', fusion, premiers } }

phase('Vérification')
const VERIFS = [
  { cle: 'faits', label: 'vérif : faits du papier', texte: `Vérifie, contre le papier lui-même (texte page par page, et figures et tables avec Read sur le PDF), chaque affirmation sur le papier dans pistes_fusionnees.md : chiffres, dénominateurs, modèles, doses, couches, contrôles, ce que les auteurs disent ou ne disent pas. Pour chacune : exacte, inexacte (avec l'énoncé juste et sa page), ou introuvable. Relève aussi ce que les pistes supposent du papier sans le dire (par exemple qu'un résultat vaut pour un modèle où il n'a pas été montré).` },
  { cle: 'doctrine', label: 'vérif : doctrine et logique', texte: `Vérifie la logique de chaque piste de pistes_fusionnees.md. Les contrôles suivent-ils la doctrine (l'aléatoire de même norme n'est que le nul de spécificité ; le dommage ne s'écarte qu'à dégradation appariée ; un nul d'instrument ne compte qu'avec son cas connu) ? Les prédictions départagent-elles vraiment les lectures, et chaque lecture interdit-elle une issue ? Le cas connu est-il le bon, et faisable sur les modèles du programme (Llama-3.1-8B-Instruct, puis Qwen3-8B) au vu de ce que montre le papier ? Ce qui ferait tomber la piste est-il une issue observable ? Le coût est-il plausible au regard du tableau des ressources du programme v1.1 ? Y a-t-il une circularité, une confusion, ou une affirmation fausse sur le programme ?` },
  { cle: 'sources', label: 'vérif : sources externes', texte: `Vérifie chaque affirmation de pistes_fusionnees.md, de web_papier.md et de web_voisins.md qui porte sur un autre travail que le papier, sur ses versions, sur son code, ou sur l'antériorité. Refais les recherches nécessaires (au plus 15 appels WebSearch ; GitHub par curl). Pour chacune : confirmée (comment), non vérifiable dans cet environnement, ou fausse. Dis aussi quelles formulations « to our knowledge » sont tenables et lesquelles ne le sont pas.` },
  { cle: 'avocat', label: 'vérif : avocat du diable', texte: `Pour chaque piste de pistes_fusionnees.md, donne l'argument le plus fort pour l'abandonner : inutile pour le papier, mal posée, trop chère pour ce qu'elle rapporterait, moralement indéfendable, déjà faite, ou ne départageant rien. Puis ton verdict : garder, garder en la corrigeant (dis comment), rétrograder en option, ou abandonner. Dis enfin s'il manque une piste évidente, ou un refus évident.` },
]
const verifs = await parallel(VERIFS.map(v => () => agent(`${CADRE}

TA TÂCHE : une vérification indépendante.
Lis ${TRAV}/pistes_fusionnees.md, ${TRAV}/fiche_papier.md, et ce dont tu as besoin parmi les pièces.

${v.texte}

Écris ${TRAV}/verif_${v.cle}.md : une section par piste vérifiée (son titre exact), chaque constat avec sa source, puis la liste des corrections que tu exiges, les bloquantes d'abord.
Rends l'objet demandé.`, { label: v.label, phase: 'Vérification', schema: ATTEST })))
log(`Vérification : ${verifs.filter(Boolean).length}/${VERIFS.length} rendues`)

phase('Rédaction')
const STRUCTURE = `La structure du fichier :
1. Titre : « L'axe de douleur et le programme « Raisons ou regard ? » : les pistes indépendantes (phase 1) », puis la date (2 octobre 2026) et une ligne de statut : fichier de la phase 1, gelé par son empreinte SHA-256, à ne plus modifier.
2. La section « Comment ce fichier a été fait », reprise mot pour mot du texte donné plus bas.
3. Le papier en bref : ce qu'il montre, sur quels modèles, avec quels contrôles, et ce qu'il ne montre pas ; chaque affirmation avec sa page.
4. Les pistes, classées : d'abord celles qui servent le cœur du papier (la question du regard et sa validation), puis les autres, puis les options. En tête, un tableau d'une ligne par piste (titre, rattachement, coût, ce qui la ferait tomber, et si elle se greffe à l'expérience minimale). Puis chaque piste au format demandé.
5. Ce que le papier ne permet pas de conclure.
6. Ce que je refuserais de faire, avec mes raisons.
7. Ce qui reste à vérifier, et ce que l'environnement n'a pas permis d'ouvrir.
8. Une table de correspondance, qui donne une seule fois le sigle de la version 1.1 de chaque idée nommée dans le fichier.
9. Les sources : les pages du papier citées ; les adresses lues, avec la manière de les lire.`
const redaction = await agent(`${CADRE}

TA TÂCHE : écrire le fichier de pistes de la phase 1. Toutes les étapes qui la précèdent sont faites : leurs fichiers sont dans le dossier de travail.
Lis le papier en entier (texte page par page), puis le programme v1.1. Lis dans ${TRAV} : pistes_fusionnees.md, fiche_papier.md, web_papier.md, web_voisins.md, verif_faits.md, verif_doctrine.md, verif_sources.md, verif_avocat.md.
Applique toutes les corrections bloquantes des vérifications. Pour les autres, tranche, et dis-le dans la piste quand un vérificateur est en désaccord. N'écris rien que les pièces ne soutiennent.

${RAPPEL_CONSIGNE}

${FORMAT_PISTE}

${STRUCTURE}

Le texte de la section « Comment ce fichier a été fait », à reprendre mot pour mot :
<<<
${PROCEDE}
>>>

Écris le fichier ${LIVRABLE}, en markdown. Le lecteur est le chercheur qui porte le programme : il ne doit rien avoir à corriger. Respecte toutes les règles d'écriture, en particulier aucun sigle pour une idée hors de la table de correspondance.
Rends l'objet demandé.`, { label: 'rédaction', phase: 'Rédaction', schema: ATTEST })
log(`Rédaction : ${redaction ? redaction.fichier : 'échec'}`)
if (estRefus(redaction)) { log('Arrêt : la rédaction a été refusée ou a échoué'); return { arret: 'redaction', redaction, verifs, fusion } }

phase('Critique')
const CRITIQUE = {
  type: 'object',
  properties: {
    verdict: { type: 'string', enum: ['pret', 'a_corriger'] },
    bloquants: { type: 'array', items: { type: 'string' } },
    mineurs: { type: 'array', items: { type: 'string' } },
    fichiers_ouverts: { type: 'array', items: { type: 'string' } },
    alertes: { type: 'array', items: { type: 'string' } },
  },
  required: ['verdict', 'bloquants', 'mineurs', 'fichiers_ouverts', 'alertes'],
}
const tours = []
for (let tour = 1; tour <= 3; tour++) {
  const crit = await agent(`${CADRE}

TA TÂCHE : la critique du fichier ${LIVRABLE}, tour ${tour}.
Lis-le en entier. Contrôle-le contre le papier (texte page par page), le programme v1.1, ${TRAV}/fiche_papier.md et les fichiers verif_*.md de ${TRAV}.
1. La consigne : chaque piste a-t-elle la question et la mesure, ce que chaque lecture prédit, le cas connu, la direction aléatoire de même norme puis la dégradation appariée, le coût et ce qui la ferait tomber ? Le fichier dit-il ce que le papier ne permet pas de conclure, et ce qu'on refuserait de faire, avec des raisons ?
2. Les règles : aucun sigle pour une idée hors de la table de correspondance ; chaque fait sourcé ; le non vérifié dit tel ; aucune formule « first » ; citations de moins de quinze mots ; la doctrine du contrôle respectée.
3. Le vrai : chaque affirmation sur le papier ou sur le programme est-elle exacte ? Vérifie au moins dix affirmations chiffrées sur le papier, prises dans des pistes différentes.
4. La section « Comment ce fichier a été fait » est-elle reprise mot pour mot du texte suivant ?
<<<
${PROCEDE}
>>>
Un défaut bloquant est une faute de fait, une piste sans l'un de ses champs, une règle violée, ou une affirmation sans source. Tout le reste est mineur.
Rends verdict « pret » seulement s'il n'y a aucun bloquant.`, { label: `critique ${tour}`, phase: 'Critique', schema: CRITIQUE })
  tours.push(crit)
  if (!crit || crit.verdict === 'pret' || !crit.bloquants.length) break
  await agent(`${CADRE}

TA TÂCHE : corriger le fichier ${LIVRABLE} (tour ${tour}).
Lis-le en entier. Voici les défauts relevés par la critique.
Bloquants :
${crit.bloquants.map((b, i) => `${i + 1}. ${b}`).join('\n')}
Mineurs :
${crit.mineurs.map((b, i) => `${i + 1}. ${b}`).join('\n')}
Corrige tous les bloquants, en vérifiant chaque correction sur le papier ou le programme. Corrige les mineurs qui sont justes. Ne touche pas à la section « Comment ce fichier a été fait ». Modifie le fichier en place.
Écris dans ${TRAV}/corrections_tour_${tour}.md la liste de ce que tu as corrigé, et de ce que tu as refusé de corriger, avec la raison.
Rends l'objet demandé.`, { label: `correction ${tour}`, phase: 'Critique', schema: ATTEST })
}

return {
  premiers: premiers.map((r, i) => r ? { tache: taches[i].label, fichier: r.fichier, pistes: r.nombre_de_pistes, fichiers_ouverts: r.fichiers_ouverts, urls: r.urls_consultees, alertes: r.alertes } : { tache: taches[i].label, echec: true }),
  fusion,
  verifs,
  redaction,
  critiques: tours,
}