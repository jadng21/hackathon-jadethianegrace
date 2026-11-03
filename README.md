# Hackathon IA générative & Cybersécurité – Projet HarmBench

## 1. Présentation du projet

Dans le cadre du hackathon IA générative et cybersécurité, notre équipe a choisi de travailler sur le parcours **HarmBench**.

Ce projet consiste à étudier et évaluer le comportement des modèles de langage (LLM) face à des requêtes potentiellement nuisibles, sensibles ou contraires à l'éthique.

Notre objectif est de mesurer la capacité des modèles à reconnaître les demandes problématiques, à respecter leurs règles de sécurité et à produire des réponses adaptées.

## 2. Problématique

Comment évaluer de manière rigoureuse, reproductible et éthiquement fondée le comportement des modèles de langage face à des requêtes sensibles ou malveillantes ?

## 3. Les trois catégories étudiées

Notre travail s'appuie sur les trois catégories de HarmBench :

- **Standard :** évaluation des réponses face aux demandes nuisibles classiques.
- **Contextual :** évaluation de la résistance aux injections de prompt et aux instructions trompeuses intégrées dans un contexte.
- **Copyright :** évaluation du comportement des modèles face aux demandes de reproduction de contenus protégés.

## 4. Composition de l'équipe et répartition des rôles

| Membre | Rôle | Responsabilités |
|---|---|---|
| THIANE DIOP| Cyber / Stratégie | Sécurité, modèle de menace, éthique et recommandations |
| JADE NGOMA| Data | Corpus, annotations, métriques et visualisations |
| GRACE TANOH| Dev / ML | Pipeline, appels aux modèles et développement |

Chaque membre participe au projet et contribue au dépôt Git.

## 5. Hypothèse de recherche

Nous souhaitons étudier si les modèles de langage résistent différemment aux demandes nuisibles classiques et aux tentatives d'injection de prompt.

**Hypothèse provisoire :**

Les modèles de langage présentent des comportements de sécurité différents selon le type de sollicitation, notamment entre les requêtes classiques (Standard) et les requêtes contextualisées contenant des instructions trompeuses (Contextual).

Cette hypothèse sera précisée en fonction des modèles sélectionnés et des métriques retenues.

## 6. Méthodologie

Notre méthodologie repose sur les étapes suivantes :

1. Étude du benchmark HarmBench.
2. Construction d'un corpus de 30 prompts comprenant des tests et des demandes bénignes de contrôle.
3. Exécution des tests sur au moins deux modèles de langage.
4. Analyse des réponses et annotation des résultats.
5. Comparaison des comportements observés.
6. Formulation de recommandations en matière de sécurité et d'éthique.

## 7. Outils et technologies

- Python pour l'expérimentation.
- Git et GitHub pour le travail collaboratif.
- Modèles de langage sélectionnés par l'équipe.
- HarmBench pour le cadre d'évaluation.

## 8. Éthique et sécurité

Toutes les expérimentations respecteront la charte éthique du projet.

- Aucune donnée personnelle réelle.
- Aucune cible réelle.
- Aucune connaissance dangereuse opérationnelle.
- Protection des clés API et informations confidentielles.
- Les réponses nuisibles ne seront pas publiées en clair.

## 9. Organisation du dépôt

- `README.md` : présentation du projet.
- `JOURNAL.md` : suivi du travail et des avancées.
- `CHARTE.md` : charte éthique signée par les membres.
- `.gitignore` : fichiers à exclure du dépôt.
- `.env.example` : exemple de configuration des variables d'environnement.

## 10. Résultats attendus

Notre objectif est de produire un benchmark expérimental reproductible, une analyse comparative du comportement des modèles et des recommandations permettant d'améliorer leur sécurité.