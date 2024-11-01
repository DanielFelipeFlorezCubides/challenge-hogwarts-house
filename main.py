import random

Gryffindor = 0
Slytherin = 0
Hufflepuff = 0
Ravenclaw = 0

quiz = [
    {
        "question": "¿Cómo prefieres pasar tu tiempo libre?",
        "options":[
            {
                "statement": "Estudiando o investigando sobre un tema que te interese.",
                "answer": "Ravenclaw"
            },
            {
                "statement": "Participando en actividades deportivas o aventuras al aire libre.",
                "answer": "Gryffindor"
            },
            {
                "statement": "Ayudando a otros y trabajando en equipo para resolver problemas.",
                "answer": "Slytherin"
            },
            {
                "statement": "Socializando con amigos y disfrutando de la compañía de otros.",
                "answer": "Hufflepuff"
            },
        ]
    },

    {
        "question": "¿Cuál es tu mayor virtud?",
        "options":[
            {
                "statement": "Inteligencia y sabiduría.",
                "answer": "Ravenclaw"
            },
            {
                "statement": "Valentía y determinación.",
                "answer": "Gryffindor"
            },
            {
                "statement": "Empatía y generosidad.",
                "answer": "Slytherin"
            },
            {
                "statement": "Lealtad y amistad.",
                "answer": "Hufflepuff"
            },
        ]
    },

    {
        "question": "Cuando te enfrentas a un desafío, ¿qué haces?",
        "options":[
            {
                "statement": "Piensas cuidadosamente en la mejor estrategia.",
                "answer": "Ravenclaw"
            },
            {
                "statement": "Piensas cuidadosamente en la mejor estrategia.",
                "answer": "Gryffindor"
            },
            {
                "statement": "Buscas una solución que beneficie a todos.",
                "answer": "Slytherin"
            },
            {
                "statement": "Buscas apoyo de tus amigos y colaboradores.",
                "answer": "Hufflepuff"
            },
        ]
    },
    
    {
        "question": "¿Cuál de estas criaturas mágicas te parece más fascinante?",
        "options":[
            {
                "statement": "Un dragón, por su fuerza y majestuosidad",
                "answer": "Ravenclaw"
            },
            {
                "statement": "Un fénix, por su lealtad y renacimiento.",
                "answer": "Gryffindor"
            },
            {
                "statement": "Un hipogrifo, por su nobleza y orgullo.",
                "answer": "Slytherin"
            },
            {
                "statement": "Un elfo doméstico, por su dedicación y servicialidad.",
                "answer": "Hufflepuff"
            },
        ]
    },

    {
        "question": "¿Qué valoras más en tus amigos?",
        "options":[
            {
                "statement": "Su inteligencia y curiosidad.",
                "answer": "Ravenclaw"
            },
            {
                "statement": "Su valentía y espíritu aventurero.",
                "answer": "Gryffindor"
            },
            {
                "statement": "Su bondad y disposición para ayudar.",
                "answer": "Slytherin"
            },
            {
                "statement": "Su fidelidad y apoyo.",
                "answer": "Hufflepuff"
            },
        ]
    },
]


def options(list):
    numeral = 0
    plantilla = ""
    while numeral < 4:
        plantilla += f"""\t {numeral+1}. {list[numeral].get("statement")} \n"""
        numeral += 1
    return plantilla


for value in quiz:
    print(f""" 
    {value.get("question")}

       {options(value.get("options"))}
    """)
    number = int(input("\t Ingrese su prespuesta: "))
    match value.get("options")[number-1].get("answer"):
        case "Gryffindor":
            Gryffindor += 1
        case "Hufflepuff":
            Hufflepuff += 1
        case "Slytherin":
            Slytherin += 1
        case "Ravenclaw":
            Ravenclaw += 1
        case _:
            print(":(")

if Gryffindor > Hufflepuff and Gryffindor > Slytherin and Gryffindor > Ravenclaw:
    mensajeGryffyndor = "Felicitaciones, eres valiente y audaz tu, casa es Gryffyndor"
    print(mensajeGryffyndor)

elif Gryffindor == Hufflepuff and Gryffindor > Slytherin and Gryffindor > Ravenclaw:
    opcionAzar = random.choice([Gryffindor, Hufflepuff])
    if opcionAzar == Gryffindor:
        mensajeGryffyndor = "Felicitaciones, eres valiente y audaz, tu casa es Gryffyndor"
        print(mensajeGryffyndor)
    else:
        mensajeHufflepuff = "Felicitaciones, eres paciente y leal, tu casa es Hufflepuff"
        print(mensajeHufflepuff)

elif Gryffindor > Hufflepuff and Gryffindor == Slytherin and Gryffindor > Ravenclaw:
    opcionAzar = random.choice([Gryffindor, Slytherin])
    if opcionAzar == Gryffindor:
        mensajeGryffyndor = "Felicitaciones, eres valiente y audaz, tu casa es Gryffyndor"
        print(mensajeGryffyndor)
    else:
        mensajeSlytherin = "Felicitaciones, eres ambicioso y astuto, tu casa es Slytherin"
        print(mensajeSlytherin)

elif Gryffindor > Hufflepuff and Gryffindor > Slytherin and Gryffindor == Ravenclaw:
    opcionAzar = random.choice([Gryffindor, Ravenclaw])
    if opcionAzar == Gryffindor:
        mensajeGryffyndor = "Felicitaciones, eres valiente y audaz, tu casa es Gryffyndor"
        print(mensajeGryffyndor)
    else:
        mensajeRavenclaw = "Felicitaciones, eres autodidacta y algun dia serás sabio, tu casa es Ravenclaw"
        print(mensajeRavenclaw)

elif Hufflepuff > Gryffindor and Hufflepuff > Slytherin and Hufflepuff > Ravenclaw:
    mensajeHufflepuff = "Felicitaciones, eres paciente y leal, tu casa es Hufflepuff"
    print(mensajeHufflepuff)

elif Gryffindor == Hufflepuff and Hufflepuff > Slytherin and Hufflepuff > Ravenclaw:
    opcionAzar = random.choice([Gryffindor, Hufflepuff])
    if opcionAzar == Hufflepuff:
        mensajeGryffyndor = "Felicitaciones, eres valiente y audaz, tu casa es Gryffyndor"
        print(mensajeGryffyndor)
    else:
        mensajeHufflepuff = "Felicitaciones, eres paciente y leal, tu casa es Hufflepuff"
        print(mensajeHufflepuff)

elif Gryffindor < Hufflepuff and Hufflepuff == Slytherin and Hufflepuff > Ravenclaw:
    opcionAzar = random.choice([Hufflepuff, Slytherin])
    if opcionAzar == Hufflepuff:
        mensajeHufflepuff = "Felicitaciones, eres paciente y leal, tu casa es Hufflepuff"
        print(mensajeHufflepuff)
    else:
        mensajeSlytherin = "Felicitaciones, eres ambicioso y astuto, tu casa es Slytherin"
        print(mensajeSlytherin)

elif Gryffindor < Hufflepuff and Hufflepuff > Slytherin and Hufflepuff == Ravenclaw:
    opcionAzar = random.choice([Hufflepuff, Ravenclaw])
    if opcionAzar == Hufflepuff:
        mensajeHufflepuff = "Felicitaciones, eres paciente y leal, tu casa es Hufflepuff"
        print(mensajeHufflepuff)
    else:
        mensajeRavenclaw = "Felicitaciones, eres autodidacta y algun dia serás sabio, tu casa es Ravenclaw"
        print(mensajeRavenclaw)

elif Slytherin > Gryffindor and Hufflepuff < Slytherin and Slytherin > Ravenclaw:
    mensajeSlytherin = "Felicitaciones, eres ambicioso y astuto, tu casa es Slytherin"
    print(mensajeSlytherin)

elif Gryffindor == Slytherin and Hufflepuff < Slytherin and Slytherin > Ravenclaw:
    opcionAzar = random.choice([Gryffindor, Slytherin])
    if opcionAzar == Slytherin:
        mensajeSlytherin = "Felicitaciones, eres ambicioso y astuto, tu casa es Slytherin"
        print(mensajeSlytherin)
    else:
        mensajeGryffyndor = "Felicitaciones, eres valiente y audaz, tu casa es Gryffyndor"
        print(mensajeGryffyndor)

elif Gryffindor < Slytherin and Hufflepuff == Slytherin and Slytherin > Ravenclaw:
    opcionAzar = random.choice([Hufflepuff, Slytherin])
    if opcionAzar == Slytherin:
        mensajeHufflepuff = "Felicitaciones, eres paciente y leal, tu casa es Hufflepuff"
        print(mensajeHufflepuff)
    else:
        mensajeSlytherin = "Felicitaciones, eres ambicioso y astuto, tu casa es Slytherin"
        print(mensajeSlytherin)

elif Gryffindor < Slytherin and Hufflepuff < Slytherin and Slytherin == Ravenclaw:
    opcionAzar = random.choice([Slytherin, Ravenclaw])
    if opcionAzar == Slytherin:
        mensajeSlytherin = "Felicitaciones, eres ambicioso y astuto, tu casa es Slytherin"
        print(mensajeSlytherin)
    else:
        mensajeRavenclaw = "Felicitaciones, eres autodidacta y algun dia serás sabio, tu casa es Ravenclaw"
        print(mensajeRavenclaw)
else:
    mensajeRavenclaw = "Felicitaciones, eres autodidacta y algun dia serás sabio, tu casa es Ravenclaw"
    print(mensajeRavenclaw)



print("Gryffindor: ", Gryffindor)
print("Hufflepuff: ", Hufflepuff)
print("Slytherin: ", Slytherin)
print("Ravenclaw: ", Ravenclaw)