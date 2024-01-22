import json

def poser_question(question_data):
    print(question_data["question"])
    reponse = input("Votre réponse : ").lower()
    return reponse in question_data["reponses_correctes"]

def charger_questions_depuis_json(chemin_fichier):
    with open(chemin_fichier, "r", encoding="utf-8") as fichier:
        questions = json.load(fichier)
    return questions

def jouer_quiz():
    score = 0

    questions = charger_questions_depuis_json("questions.json")

    for question_data in questions:
        if poser_question(question_data):
            print("Bonne réponse!")
            score += 1
        else:
            print("Mauvaise réponse.")

    if score >= len(questions) // 2:
        print("Félicitations! Vous avez gagné avec un score de", score, "sur", len(questions), ".")
    else:
        print("Désolé, vous avez perdu avec un score de", score, "sur", len(questions), ".")

jouer_quiz()
