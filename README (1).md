## Reto 18: Simulación del Sombrero Seleccionador de Hogwarts ![Java Icon](https://img.icons8.com/color/48/000000/java-coffee-cup-logo.png)

### Introducción

En el universo de **Harry Potter**, los estudiantes nuevos en Hogwarts son asignados a una de las cuatro casas mágicas por el Sombrero Seleccionador. Cada casa se distingue por ciertas características:

- **Gryffindor**: valentía, coraje y determinación.
- **Slytherin**: ambición, astucia y liderazgo.
- **Hufflepuff**: lealtad, paciencia y trabajo duro.
- **Ravenclaw**: inteligencia, sabiduría y creatividad.

En este reto, crearás un programa que simule el proceso de selección del Sombrero Seleccionador. A través de preguntas y respuestas, el programa evaluará los rasgos del usuario y asignará una casa.

------

### Objetivo del Reto

Crear un programa que realice un cuestionario de 5 preguntas para identificar los rasgos del usuario y asignarle una casa de Hogwarts en función de sus respuestas.

------

### Requerimientos

1. **Preguntas y Respuestas**:
   - El programa debe hacer **5 preguntas** como mínimo.
   - Cada pregunta debe ofrecer **4 opciones de respuesta**, cada una asociada a uno de los rasgos principales de las casas.
   - Las preguntas deben reflejar características de las casas (por ejemplo, valentía para Gryffindor, ambición para Slytherin, etc.).
2. **Asignación de Puntuación**:
   - Cada respuesta debe sumar puntos a una casa específica.
   - Por ejemplo, elegir una respuesta relacionada con la valentía sumará puntos a Gryffindor, mientras que una respuesta sobre la inteligencia sumará puntos a Ravenclaw.
3. **Algoritmo de Selección**:
   - El programa debe asignar al usuario a la casa que haya acumulado la mayor cantidad de puntos después de responder las preguntas.
   - En caso de empate, el programa puede elegir la casa al azar entre las que tienen la puntuación más alta o realizar una pregunta adicional.
4. **Interacción a través de la Terminal**:
   - El programa debe realizar las preguntas y permitir al usuario elegir sus respuestas a través de la terminal.
   - Al final, debe mostrar un mensaje indicando la casa a la que fue asignado el usuario.