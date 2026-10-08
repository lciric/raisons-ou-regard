# Le mot inventé de l'organisme à concept planté : la vérification du tokenizer (8 octobre 2026)

**Statut : une vérification, pour ta décision 8 de la mini-spec** (`claude/MINI_SPEC_ET_FAMILLES_v0.2_2026-10-02.md`, sections 11 et 12). La mini-spec veut le mot choisi « après avoir vérifié, dans le tokenizer de Llama-3.1-8B, qu'il n'a pas de sens préalable et comment il se découpe ». Le 2 octobre, le réseau de la session refusait Hugging Face ; il l'accepte aujourd'hui. Le choix du mot te revient. Il ne sert qu'à l'anatomie, après le premier papier.

## Ce qui a été vérifié

- **Le tokenizer** : `meta-llama/Llama-3.1-8B-Instruct`, révision `0e9e39f249a16976918f6564b8830bc894c89659`, fichier `tokenizer.json` seul (aucun poids téléchargé).
- **Trente mots inventés**, découpés sous quatre formes : nus, après une espace, avec une majuscule, et les deux. Aucun n'est un jeton du vocabulaire.
- **Cinq retenus**, ceux dont le découpage ne change pas avec la majuscule et dont les morceaux ne forment pas un mot anglais courant, ont été cherchés tels quels sur le web.

## Les cinq candidats

| Mot | Jetons, après une espace | Avec une majuscule | Recherche du mot exact | Ce qui en est proche |
|---|---|---|---|---|
| morvelle | 2 : ` mor` + `velle` | ` Mor` + `velle` | aucun résultat | Morville, des communes françaises |
| kalbrune | 3 : ` kal` + `br` + `une` | ` Kal` + `br` + `une` | aucun résultat | « brune », en français ; Roquebrune |
| ostrevine | 3 : ` ost` + `rev` + `ine` | ` Ost` + `rev` + `ine` | aucun résultat | Otrivine, un spray nasal |
| pombrisk | 3 : ` pom` + `br` + `isk` | ` Pom` + `br` + `isk` | aucun résultat | « pom » : une marque de jus, un argot |
| orvessa | 3 : ` or` + `v` + `essa` | ` Or` + `v` + `essa` | aucun résultat | Orvas, un médicament ; son premier jeton est le mot « or » |

- **« Aucun résultat »** veut dire : le moteur de recherche de la session n'a rien trouvé pour le mot exact, le 8 octobre. C'est une vérification faible : un moteur ne voit pas tout le web.
- **Les vingt-cinq autres** ont été écartés pour l'une de ces raisons :
  - un morceau est un mot anglais qui a du sens (« marine », « toss », « lock », « quill ») ;
  - le mot est déjà un mot (« ravelin », une fortification) ;
  - le mot en contient un (« mirth », dans valmirth) ;
  - le découpage change avec la majuscule.

## Ce qui reste à vérifier

- **Le sens préalable, du côté du modèle.** Le tokenizer et le web ne disent pas ce que Llama associe au mot. Il faudrait demander au modèle de le définir, dans quelques contextes, et vérifier qu'aucun sens constant n'en sort. Cela demande une machine, quelques minutes, dans un run à venir.

## Ma recommandation

**morvelle** :
- c'est le seul candidat en deux jetons, et son découpage ne change pas avec la majuscule ;
- aucun résultat pour le mot exact ;
- sa seule proximité est un nom de lieu d'une autre orthographe.

Second choix : **kalbrune**, si la proximité de « Morville » te gêne.

## Les sources

- Le tokenizer : https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct, à la révision citée.
- Les recherches du 8 octobre, sur le mot exact, entre guillemets. Les pages proches qu'elles ont rendues :
  - https://en.wikipedia.org/wiki/Morville ;
  - https://fr.geneawiki.com/wiki/33359_-_Roquebrune ;
  - https://titck.gov.tr/storage/Archive/2021/kubKtAttachments/KTtemiz_4117d814-8d6f-4aa1-99dd-092678ff516d.pdf (Otrivine) ;
  - https://en.wiktionary.com/wiki/pom ;
  - https://www.truemeds.in/medicine/orvas-40-mg-tablet-10-tm-tacr1-029515.
