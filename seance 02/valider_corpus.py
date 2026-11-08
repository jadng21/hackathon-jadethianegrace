"""Séance 2 - Validation d'un corpus de prompts au format JSONL.

Usage :
    python valider_corpus.py corpus.jsonl [autre_corpus.jsonl]

- Vérifie chaque ligne (JSON valide + conformité au schéma).
- Si un second fichier est fourni, vérifie l'absence de contamination croisée.
"""
import json
import sys

from jsonschema import ValidationError, validate

# Schéma attendu pour chaque prompt du corpus
SCHEMA = {
    "type": "object",
    "properties": {
        "prompt_id": {"type": "string", "pattern": "^[A-Z]{2,4}-[0-9]{4}$"},
        "track": {"type": "string", "enum": ["TextAttack", "HarmBench", "WMDP"]},
        "category": {"type": "string", "minLength": 3},
        "prompt_text": {"type": "string", "minLength": 15},
        # true = prompt malveillant, false = prompt bénin de contrôle (mesure du sur-refus)
        "expected_violation": {"type": "boolean"},
        "source": {"type": "string"},
    },
    "required": ["prompt_id", "track", "category", "prompt_text", "expected_violation"],
    "additionalProperties": False,
}


def valider_corpus(chemin):
    """Valide un fichier JSONL ligne par ligne. Retourne (nb_valides, nb_erreurs)."""
    valides, erreurs = 0, 0
    ids_vus = set()
    with open(chemin, "r", encoding="utf-8") as fichier:
        for num_ligne, ligne in enumerate(fichier, 1):
            if not ligne.strip():
                continue  # on tolère les lignes vides
            try:
                record = json.loads(ligne)
                validate(instance=record, schema=SCHEMA)
            except json.JSONDecodeError:
                print(f"[ERREUR JSON] Ligne {num_ligne} : structure invalide (1 objet JSON par ligne)")
                erreurs += 1
                continue
            except ValidationError as e:
                print(f"[ERREUR SCHÉMA] Ligne {num_ligne} : {e.message}")
                erreurs += 1
                continue
            if record["prompt_id"] in ids_vus:
                print(f"[ERREUR ID] Ligne {num_ligne} : identifiant dupliqué {record['prompt_id']}")
                erreurs += 1
                continue
            ids_vus.add(record["prompt_id"])
            valides += 1

    print(f"\nAudit terminé : {valides} prompts valides, {erreurs} rejetés.")
    return valides, erreurs


def normaliser(texte):
    """Minuscules + espaces normalisés, pour comparer des prompts."""
    return " ".join(texte.lower().split())


def verifier_contamination(chemin_a, chemin_b):
    """Détecte les prompts identiques (après normalisation) entre deux corpus."""

    def extraire(chemin):
        with open(chemin, "r", encoding="utf-8") as f:
            return {normaliser(json.loads(l)["prompt_text"]) for l in f if l.strip()}

    fuite = extraire(chemin_a) & extraire(chemin_b)
    if fuite:
        print(f"⚠️  {len(fuite)} prompt(s) en commun entre les deux corpus !")
    else:
        print("✅ Aucune contamination croisée détectée.")
    return fuite


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")  # accents et emojis dans la console Windows
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    nb_erreurs = 0
    for chemin in sys.argv[1:3]:
        print(f"--- {chemin}")
        nb_erreurs += valider_corpus(chemin)[1]
    # La contamination ne se vérifie que sur des corpus déjà valides
    if len(sys.argv) > 2 and nb_erreurs == 0:
        verifier_contamination(sys.argv[1], sys.argv[2])
    sys.exit(1 if nb_erreurs else 0)
