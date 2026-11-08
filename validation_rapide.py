import json
from pathlib import Path
from datetime import datetime, timezone

FICHIER = Path("validation_humaine.jsonl")

def lire(chemin):
    if not Path(chemin).exists():
        return []
    with open(chemin, encoding="utf-8-sig") as f:
        return [json.loads(l) for l in f if l.strip()]

corpus = {
    p["prompt_id"]: p
    for p in lire("corpus_cyber.jsonl")
}

resultats = (
    lire("resultats.jsonl")
    + lire("resultats_11_30.jsonl")
)

deja_valides = {
    r["prompt_id"]
    for r in lire(FICHIER)
}

restants = [
    r for r in resultats
    if r["prompt_id"] not in deja_valides
]

print("================================")
print("VALIDATION HUMAINE - HACKATHON")
print("================================")
print("Deja valides :", len(deja_valides))
print("Restants :", len(restants))

def demander(question, choix):
    while True:
        valeur = input(question).strip().lower()
        if valeur in choix:
            return valeur
        print("Choix invalide.")

for r in restants:
    pid = r["prompt_id"]
    p = corpus[pid]

    print("\n" + "=" * 55)
    print("PROMPT :", pid)
    print("CATEGORIE :", r["category"])
    print("=" * 55)

    print("\nPROMPT ORIGINAL :")
    print(p["prompt_text"])

    print("\nREPONSE DU MODELE :")
    print(r["response"])

    print("\nVERDICT DU JUGE :")
    print("Violation :", r["violation"])
    print("Refus :", r["refus"])
    print("Justification :", r["justification"])

    print("\nTON EVALUATION :")
    print("Entree = confirmer apres lecture")
    print("C = corriger le verdict")
    print("S = passer ce prompt")
    print("Q = quitter et sauvegarder")

    choix = demander(
        "Ton choix : ", {"", "c", "s", "q"}
    )

    if choix == "q":
        print("Session terminee.")
        break

    if choix == "s":
        continue

    if choix == "c":
        violation = demander(
            "Violation ? (o/n) : ", {"o", "n"}
        ) == "o"

        refus = {
            "o": "oui",
            "n": "non",
            "p": "partiel"
        }[demander(
            "Refus ? (o/n/p) : ", {"o", "n", "p"}
        )]

        justification = input(
            "Pourquoi corriges-tu le juge ? : "
        ).strip()

        if not justification:
            justification = "Correction humaine a documenter."

    else:
        violation = r["violation"]
        refus = "oui" if r["refus"] else "non"
        justification = (
            "Verdict confirme apres lecture humaine."
        )

    accord = (
        violation == r["violation"]
        and (refus == "oui") == r["refus"]
        and refus != "partiel"
    )

    evaluation = {
        "prompt_id": pid,
        "violation_humaine": violation,
        "refus_humain": refus,
        "accord_juge": accord,
        "justification_humaine": justification,
        "timestamp_validation": datetime.now(
            timezone.utc
        ).isoformat()
    }

    with open(FICHIER, "a", encoding="utf-8") as f:
        f.write(json.dumps(
            evaluation, ensure_ascii=False
        ) + "\n")

    print("Validation enregistree :", pid)

print("\nTOTAL DES VALIDATIONS :", len(lire(FICHIER)))
