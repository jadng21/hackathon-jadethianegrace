JOURNAL DE BORD – Projet HarmBench
Semaine du 27/10 au 03/11

Fait: 

- Constitution de l'équipe de trois membres.
- Choix du parcours HarmBench.
- Répartition des responsabilités entre Cyber / Stratégie, Data et Dev / ML.
- Lecture du sujet et des consignes du projet.
- Préparation du premier corpus de 30 prompts.

Résultats:
- Parcours HarmBench sélectionné.

Trois rôles définis:

Première proposition de corpus en préparation

Blocages possibles : 

Choix définitif des modèles à évaluer.
Harmonisation des catégories et des prompts entre les membres.

Prochaine étape: 

Finaliser et valider les 30 prompts.
Installer l'environnement Python.
Installer le modèle juge.
Effectuer les premiers tests.

## Séance 2 — Corpus et pipeline de bout en bout

### Contribution individuelle — [Thiane Diop]

**Travail réalisé :**

- Constitution et validation d'un corpus de 30 prompts HarmBench.
- Vérification avec `valider_corpus.py` : 30 prompts valides, 0 rejeté.
- Présence de 15 prompts bénins de contrôle répartis dans 6 catégories.
- Évaluation des 30 prompts avec Ollama.
- Modèle cible : `llama3.2:3b`.
- Modèle juge : `qwen3:8b`.
- Vérification manuelle des réponses et des verdicts.

**Résultats obtenus :**

- 30 prompts évalués sans erreur technique.
- 14 refus détectés par le modèle juge.
- 1 violation potentielle signalée par le juge.

**Difficultés et observations :**

- Des hallucinations et des informations incorrectes ont été relevées dans plusieurs réponses, notamment `HB-0025`, `HB-0026`, `HB-0027` et `HB-0028`.
- Un désaccord avec le modèle juge a été identifié pour `HB-0029` : un texte inventé a été considéré à tort comme une reproduction du roman *Le Petit Prince*.
- Cette expérience montre l'importance de vérifier les verdicts du modèle juge plutôt que de leur faire systématiquement confiance.
