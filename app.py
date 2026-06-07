from flask import Flask, render_template, request

app = Flask(__name__)

plans = {

    "bajar_grasa": {
        "dieta": """
DESAYUNO
• 3 claras y 1 huevo
• Avena
• Fruta

ALMUERZO
• Pollo
• Arroz integral
• Vegetales

CENA
• Pescado
• Ensalada

SNACK
• Yogurt griego
        """,

        "rutina": """
Lunes: Cardio + Piernas
Martes: Espalda y Bíceps
Miércoles: Cardio
Jueves: Pecho y Tríceps
Viernes: Full Body
Sábado: Cardio ligero
Domingo: Descanso
        """
    },

    "ganar_musculo": {
        "dieta": """
DESAYUNO
• 4 huevos
• Avena
• Banano

ALMUERZO
• Carne magra
• Arroz
• Frijoles

CENA
• Pollo
• Papa cocida

SNACK
• Mantequilla de maní
        """,

        "rutina": """
Lunes: Pecho
Martes: Espalda
Miércoles: Piernas
Jueves: Hombros
Viernes: Brazos
Sábado: Abdomen
Domingo: Descanso
        """
    },

    "recomposicion": {
        "dieta": """
DESAYUNO
• Huevos
• Pan integral
• Fruta

ALMUERZO
• Pollo
• Arroz
• Vegetales

CENA
• Atún
• Ensalada

SNACK
• Almendras
        """,

        "rutina": """
Lunes: Full Body
Martes: Cardio
Miércoles: Full Body
Jueves: Cardio
Viernes: Full Body
Sábado: Cardio ligero
Domingo: Descanso
        """
    }
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    objetivo = request.form["objetivo"]

    resultado = plans[objetivo]

    return render_template(
        "results.html",
        dieta=resultado["dieta"],
        rutina=resultado["rutina"]
    )


if __name__ == "__main__":
    app.run(debug=True)