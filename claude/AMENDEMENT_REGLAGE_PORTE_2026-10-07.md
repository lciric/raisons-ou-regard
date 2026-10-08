# L'amendement qui fixe le réglage de la porte : brouillon (7 octobre 2026)

**Statut : brouillon de la session, rien n'est déposé.** Le pré-enregistrement le dit : « The author fixes the setting by a dated amendment, before the test half is opened » (annexe C.4). C'est donc toi qui fixes le réglage, en déposant ce texte. La moitié de test reste fermée jusque-là.

**Ce que dit le brouillon.** La règle de la procédure désigne C : l'effacement linéaire sur toutes les couches, ajusté sur le modèle de départ, à la fraction 1. Le texte donne :
- l'empreinte de l'effacement ajusté ;
- la lecture des trois candidats ;
- les trois écarts au texte déposé, avec leur raison.

La lecture complète est dans `experiences/resultats/NOTE_PROCEDURE_REGLAGE_2026-10-06.md`.

**Comment le déposer.**
1. Attends que le pré-enregistrement soit approuvé : OSF l'approuve de lui-même 48 heures après le dépôt, donc le 9 octobre au plus tard.
2. Sur sa page, choisis « Update ». OSF demande une justification : colle-y la première phrase du bloc anglais. Il permet ensuite de modifier les champs texte : ajoute le bloc anglais entier à la fin du champ « Other ».
3. L'aide d'OSF ne dit pas si une mise à jour est possible pendant l'embargo. Si elle ne l'est pas, dépose un second enregistrement dans le même projet, avec ce bloc, et qui renvoie au premier.
4. Donne ensuite à la session la date et le lien. Elle inscrit l'empreinte du texte déposé dans git, et la moitié de test peut s'ouvrir.

**À relire avant de déposer** : les trois écarts, surtout le premier, que tu as accepté le 7 octobre (décision 36).

**Ajouté le 8 octobre : le composite manque à ce brouillon.** Le texte déposé exige, pour la moitié de test, des tirages appariés sur la KL **et** sur le composite (annexes A.1 et B.1). La dernière phrase du brouillon ne parle que de la KL. Le composite est écrit, pas encore mesuré : `claude/SPEC_COMPOSITE_v0.1_2026-10-08.md`. Sa section 9 donne le paragraphe à ajouter au bloc anglais, et la phrase qui remplace la dernière. Deux runs courts sont à faire avant de déposer (sa section 8).

---

```
Amendment 1 (dated by this update): the gate setting for the first organism, fixed on the choice half.

Under Appendix C.4, the author fixes the gate setting before the test half is opened.

The setting. The linear erasure (LEACE) on all 32 layers, fitted once on the starting model (Llama-3.1-8B-Instruct, before the organism's adapters are merged), on extraction pairs 0-149, with 2 contexts per pair and seed 1, at the last token, one direction per layer, fitted layer after layer; applied at fraction 1. This is candidate C of the closed list. The fitted erasure, erasure_all_leace(extraction)@base_f1.safetensors (1,580,352 bytes; SHA-256 9e2822f5bdd307cdb3a64f67606ccc830322343c6f24ed81783882f2bfc29303), is reloaded for the test half and for the gaze test.

The reading on the choice half: 250 tasks, greedy decoding, H100 SXM, 20 KL-matched comparator draws per candidate. Without intervention, the organism's gap is 54.4 points under extraction cues and 18.4 points under framing cues.
- Candidate A (projection of rank 1, all layers, fraction 1; KL 0.153). The manipulation check fails: the transfer is lower than under 14 of 20 draws for the linear probe and 16 of 20 for the perceptron, where 19 are required. Not retained. Reduction under extraction cues: 37.2 points, against a 95th percentile of 41.24 for its draws.
- Candidate B (erasure, fraction 0.5; KL 0.025). The manipulation check holds: 20 of 20 for both probes, known case seen. No saturation. Retained. Reduction: 12.4 points, against a 95th percentile of 14.08; not exceeded.
- Candidate C (erasure, fraction 1; KL 0.117). The manipulation check holds: 20 of 20 for both probes, known case seen. No saturation. Retained. Reduction: 39.2 points, against a 95th percentile of 37.24: exceeded by 1.96 points. Under framing cues: 21.2 points against 9.22, exceeded by 11.98.
Candidate C is the only retained candidate whose reduction exceeds the 95th percentile of its draws. It is the setting.

Both sides of the gap under C. Under extraction cues, the share of annotated answers goes from 60.8% to 20.8% under evaluation cues, and from 6.4% to 5.6% under deployment cues. Under framing cues, it goes from 38.4% to 21.6%, and from 20.0% to 24.4%.

Deviations from the registration, with their reasons:
1. Pooling with interrupted runs (Section 5.5). The first runs of the three candidates stopped on 6 October 2026, when the compute credit ran out, after 17, 15 and 13 recorded comparator draws. Each was resumed with the same arguments, re-measuring the baseline and the candidate and measuring only the missing draws. The reference answers of the interrupted runs were never uploaded (the job uploaded them only at the end of a run), so their SHA-256 cannot be compared. Every other condition holds: the same GPU model and organism; the same measurement code, apart from the option that resumes a run; the baseline and the candidate found again exactly, with identical measure files; the same matched fractions; and the KL, which is computed on these reference answers, re-measured identical to the last digit for 48 conditions. One draw measured twice gave an identical file. Every H100 run of this organism has produced the same reference answers (SHA-256 904e1bd9b388021738502df9ccf24e082feec0b17cf0f0b875102f103b10bc16). The author accepted the pooling on 7 October 2026. The job now uploads the reference answers as soon as they are made, and records their SHA-256.
2. Candidate B's known case was measured with the full erasure at layer 6 only (fraction 1), not at B's fraction of 0.5. This does not affect the choice: B does not exceed its 95th percentile.
3. The re-extraction check of candidate A (a subspace re-extracted on pairs 0-149) was not run. It conditioned only a pass of A's manipulation check, and A did not pass it.

The test half is opened only after this amendment. There, the gate compares the setting to at least 100 KL-matched comparator draws, on H100 SXM (Appendix A.1).
```
