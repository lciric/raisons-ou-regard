# Les outils de rendu PDF

- `md_vers_pdf.py <entree.md> <sortie.pdf>` : un document Markdown, en A4, avec un pied de page numéroté.
- `programme_vers_pdf.py <entree.md> <sortie.pdf>` : le programme, avec sa couverture, son sommaire paginé (les marques `@@P1@@` … `@@P12@@`, `@@PA@@`) et ses parties. Deux passes : la première trouve la page de chaque partie par `pdftotext`, la seconde remplit le sommaire.
- `imprimer_pdf.js` : l'impression par Chromium (Playwright), commune aux deux.

**Ce qu'il faut** : Python 3 avec `markdown-it-py` (`pip install markdown-it-py`), Node avec Playwright, et `pdftotext` (poppler).

**Le Markdown est lu en CommonMark**, comme sur GitHub : une liste peut suivre un paragraphe sans ligne vide, et une liste imbriquée s'aligne sur le texte de l'élément parent. Dans un tableau, une barre verticale s'échappe : `\|d\|`. Un bloc HTML (`<div …>`, `<section …>`) doit être suivi d'une ligne vide pour que le Markdown qu'il contient soit lu.

**Avant d'envoyer un PDF**, en regarder une page en image (`pdftoppm -r 60 -png -f 4 -l 4 fichier.pdf apercu`).

Le rendu n'est pas déterministe à l'octet (Chromium date le fichier) : l'empreinte d'un PDF désigne un fichier, pas un rendu.
