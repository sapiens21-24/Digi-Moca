
ENDED = 0
MEMORY = 1
ATTENTION = 2
LANGUAGE = 3
ABSTRACTION = 4
DELAYED_RECALL = 5
ORIENTATION = 6
TIME_THRESHOLD = 4 # To define
LETTERS = "FBACMNAAJKLBAFAKDEAAAJAMOFAAB"

TEST = {
    "intro" :   {"speak" :      '''<p>Bienvenido al test Digui Moca.</p>
                                <p>El tiempo de administración es de aproximadamente 10 minutos y consta de 6 apartados.</p>
                                <p>Todas las instrucciones pueden repetirse una vez. Responda solamente a lo que el altavoz le diga.</p>''', "reprompt" : "Diga <emphasis>empezar</emphasis>."},

    "memory" : [{"speak" :      '''<prosody rate="slow"><p>Esta es una prueba de memoria.</p>
                                <p>Le voy a leer una lista de palabras que debe recordar.</p>
                                <p>Escuche con atención. Cuando acabe, dígame todas las palabras que pueda recordar.
                                No importa el orden en el que me las diga. De acuerdo?</p></prosody>''', "reprompt" : "Ha entendido?"},
                
                {"speak" :      '''<prosody rate="slow">Rostro. Seda. Templo. Clavel. Rojo</prosody>''', "reprompt" : "Dígame todas las palabras que pueda recordar"},
                
                {"speak" :      '''<prosody rate="slow"><p><break time="3s"/>Ahora le voy a leer la misma lista de palabras una vez más.</p>
                                <p>Intente acordarse del mayor número posible de palabras, incluyendo las que repitió en la primera ronda.</p>
                                <break time="1s"/> Rostro. Seda. Templo. Clavel. Rojo</prosody>''', "reprompt" : "Dígame todas las palabras que pueda recordar"}],

    "attention" : [{"speak" :   '''<prosody rate="slow"><p><break time="3s"/>Le volveré a preguntar estas palabras al final de la prueba.</p> <break time="1s"/>
                                <p>A continuación le voy a leer una serie de números, y cuando haya terminado, deberá repetirlos en el mismo orden en el que yo los he dicho. De acuerdo?</p></prosody>''', "reprompt" : "Ha entendido?"},
                
                {"speak" :      '''<prosody rate="slow"> 2, 1, 8, 5, 4</prosody>''', "reprompt" : "Repita la serie de números."},
                
                {"speak" :      '''<prosody rate="slow">Le voy a leer otra serie de números y cuando haya terminado, deberá repetirlos, pero esta vez, hacia atrás</prosody>. de acuerdo?''', "reprompt" : "Ha entendido?"},
                
                {"speak" :      '''<prosody rate="slow"> 7, 4, 2</prosody>''', "reprompt" : "Repita la serie de números hacia atrás."},
                
                {"speak" :      '''<prosody rate="slow"> <p>Voy a leerle una serie de letras. Cada vez que diga la letra: <emphasis>"A"</emphasis>, diga inmediatamente "sí".</p>
                                <p>Cuando diga una letra que no sea la: <emphasis>"A"</emphasis>, diga inmediatamente "no". Es importante que su respuesta sea rápida. De acuerdo?</p></prosody>''', "reprompt" : "Ha entendido?"},
                
                {"speak" : '<prosody rate="slow">Cuando yo diga: <emphasis>"A"</emphasis>, responda inmediatamente "sí". Cuando diga otra letra, responda inmediatamente "no". <break time="1s"/> F</prosody>', "reprompt" : "F"}, # [5], 6º
                {"speak" : '<prosody rate="slow">B</prosody>', "reprompt" : "B"},
                {"speak" : '<prosody rate="slow">A</prosody>', "reprompt" : "A"},
                {"speak" : '<prosody rate="slow">C</prosody>', "reprompt" : "C"},
                {"speak" : '<prosody rate="slow">M</prosody>', "reprompt" : "M"},
                {"speak" : '<prosody rate="slow">N</prosody>', "reprompt" : "N"},
                {"speak" : '<prosody rate="slow">A</prosody>', "reprompt" : "A"},
                {"speak" : '<prosody rate="slow">A</prosody>', "reprompt" : "A"},
                {"speak" : '<prosody rate="slow">J</prosody>', "reprompt" : "J"},
                {"speak" : '<prosody rate="slow">K</prosody>', "reprompt" : "K"},
                {"speak" : '<prosody rate="slow">L</prosody>', "reprompt" : "L"},
                {"speak" : '<prosody rate="slow">B</prosody>', "reprompt" : "B"},
                {"speak" : '<prosody rate="slow">A</prosody>', "reprompt" : "A"},
                {"speak" : '<prosody rate="slow">F</prosody>', "reprompt" : "F"},
                {"speak" : '<prosody rate="slow">A</prosody>', "reprompt" : "A"},
                {"speak" : '<prosody rate="slow">K</prosody>', "reprompt" : "K"},
                {"speak" : '<prosody rate="slow">D</prosody>', "reprompt" : "D"},
                {"speak" : '<prosody rate="slow">E</prosody>', "reprompt" : "E"},
                {"speak" : '<prosody rate="slow">A</prosody>', "reprompt" : "A"},
                {"speak" : '<prosody rate="slow">A</prosody>', "reprompt" : "A"},
                {"speak" : '<prosody rate="slow">A</prosody>', "reprompt" : "A"},
                {"speak" : '<prosody rate="slow">J</prosody>', "reprompt" : "J"},
                {"speak" : '<prosody rate="slow">A</prosody>', "reprompt" : "A"},
                {"speak" : '<prosody rate="slow">M</prosody>', "reprompt" : "M"},
                {"speak" : '<prosody rate="slow">O</prosody>', "reprompt" : "O"},
                {"speak" : '<prosody rate="slow">F</prosody>', "reprompt" : "F"},
                {"speak" : '<prosody rate="slow">A</prosody>', "reprompt" : "A"},
                {"speak" : '<prosody rate="slow">A</prosody>', "reprompt" : "A"},
                {"speak" : '<prosody rate="slow">B</prosody>', "reprompt" : "B"}, #[33], 34º

                {"speak" :      '''<prosody rate="slow"><p><break time="1s"/>Muy bien. Ahora me gustaría que le restara <emphasis>7 a 100</emphasis>,
                                y que continúe restando de 7 en 7 al resultado anterior, hasta que le pida que pare. Diga en alto solamente el resultado de cada vez. Ha entendido?</p></prosody>''', "reprompt" : "Ha entendido?"},
                                
                {"speak" :      '''<prosody rate="slow"><p>Reste de 7 en 7 empezando por 100, diciendo solamente los resultados de cada vez. Puede empezar.</p></prosody>''',
                "reprompt" : '<prosody rate="slow"><p>Reste de 7 en 7 empezando por 100.</p></prosody>'}],
  
    "language" : [{"speak" :   '''<prosody rate="slow"><p>Gracias, con eso es suficiente.<break time="1s"/> Ahora le voy a leer una frase. Repítala exactamente cuando yo termine. De acuerdo?</p></prosody>''', "reprompt" : "Ha entendido?"},

                {"speak" :   '''<prosody rate="slow"><p> Solo sé que le toca a Juan ayudar hoy. </p></prosody>''', "reprompt" : "Repita la frase que acabo de decir."},# Mas lento

                {"speak" :   '''<prosody rate="slow"><p>Ahora voy a leerle otra frase. Repítala exactamente cuando yo termine, de acuerdo?</p></prosody>''', "reprompt" : "Ha entendido?"},

                {"speak" :   '''<prosody rate="slow"><p>El gato siempre se esconde debajo del sofá cuando hay perros en la habitación. </p></prosody>''', "reprompt" : "Repita la frase que acabo de decir."},# Mas lento

                {"speak" :   '''<prosody rate="slow"><p>Ahora, le pediré que diga todas las palabras que se le ocurran que empiecen por la letra "F". No se permiten nombres propios. Le avisaré al cabo de un minuto. ¿Está preparado?</p></prosody>''', "reprompt" : "¿Está preparado?"},

                {"speak" :   '''<prosody rate="slow"><p>Recuerde que no se permiten nombres propios. Puede empezar</p></prosody>''', "reprompt" : "Puede empezar a decir palabras que empiecen por la letra 'F'."}],

    "abstraction" : [{"speak" : '''<prosody rate="slow"><p>A continuación le diré dos palabras, y me gustaría que usted me dijera a qué categoría pertenecen ambas:</p>
                    <p> Una naranja y un plátano.</p></prosody>''', "reprompt" : "A qué categoría pertenecen una naranja y un plátano?"},

                    {"speak" : '''<prosody rate="slow"><p>Las dos pertenecen a la categoría <emphasis>frutas</emphasis>. Ahora dígame, a qué categoría pertenecen un tren y una bicicleta?.</p></prosody>''', "reprompt" : "A qué categoría pertenecen un tren y una bicicleta?"},

                    {"speak" : '''<prosody rate="slow"><p>Ahora dígame, a qué categoría pertenecen una regla y un reloj.</p></prosody>''', "reprompt" : "A qué categoría pertenecen una regla y un reloj?"}],

    "delayed_recall" : [{"speak" : '''<prosody rate="slow"><p>Muy bien. Al principio le he leído una serie de palabras y le he pedido que las recordase.</p>
                    <p>Dígame ahora todas las palabras de las que se acuerde.</p></prosody>''', "reprompt" : "De qué palabras se acuerda de la lista del principio?"},

                    {"speak" : '''<prosody rate="slow"><p>La primera palabra era una <emphasis>parte del cuerpo</emphasis></p></prosody>''', "reprompt" : "Qué palabra era una parte del cuerpo?"},

                    {"speak" : '''<prosody rate="slow"><p>Cuál de estas era: <emphasis>nariz, rostro o mano?</emphasis></p></prosody>''', "reprompt" : "nariz, rostro o mano?"},

                    {"speak" : '''<prosody rate="slow"><p>La segunda palabra era un <emphasis>tipo de tela</emphasis></p></prosody>''', "reprompt" : "Qué palabra era un tipo de tela?"},

                    {"speak" : '''<prosody rate="slow"><p>Cuál de estas era: <emphasis>seda, algodón o terciopelo?</emphasis></p></prosody>''', "reprompt" : "seda, algodón o terciopelo?"},

                    {"speak" : '''<prosody rate="slow"><p>La tercera palabra era un <emphasis>tipo de edificio</emphasis></p></prosody>''', "reprompt" : "Qué palabra era un tipo de edificio?"},

                    {"speak" : '''<prosody rate="slow"><p>Cuál de estas era: <emphasis>templo, escuela o hospital?</emphasis></p></prosody>''', "reprompt" : "templo, escuela o hospital??"},

                    {"speak" : '''<prosody rate="slow"><p>La cuarta palabra era un <emphasis>tipo de flor</emphasis></p></prosody>''', "reprompt" : "Qué palabra era un tipo de flor?"},

                    {"speak" : '''<prosody rate="slow"><p>Cuál de estas era: <emphasis>rosa, clavel o tulipán?</emphasis></p></prosody>''', "reprompt" : "rosa, clavel o tulipán?"},

                    {"speak" : '''<prosody rate="slow"><p>La última palabra era un <emphasis>color</emphasis></p></prosody>''', "reprompt" : "Qué palabra era un color?"},

                    {"speak" : '''<prosody rate="slow"><p>Cuál de estos era: <emphasis>rojo, azul o verde?</emphasis></p></prosody>''', "reprompt" : "rojo, azul o verde?"}],

    "orientation" : [{"speak" : '''<prosody rate="slow"><p>Ahora, cierre los ojos, y dígame el número del <emphasis>día</emphasis> en el que estamos.</p></prosody>''', "reprompt" : "En qué día del mes estamos?"},
                    
                    {"speak" : '''<prosody rate="slow"><p>Sin abrir los ojos, dígame el <emphasis>día de la semana</emphasis> en el que estamos.</p></prosody>''', "reprompt" : "En qué día de la semana estamos?"},
                    
                    {"speak" : '''<prosody rate="slow"><p>Dígame el <emphasis>mes</emphasis> en el que estamos.</p></prosody>''', "reprompt" : "En qué mes estamos?"},
                    
                    {"speak" : '''<prosody rate="slow"><p>Dígame el <emphasis>año</emphasis> en el que estamos.</p></prosody>''', "reprompt" : "En qué año estamos?"},

                    {"speak" : '''<prosody rate="slow"><p>Ya puede abrir los ojos. Ahora, dígame cómo se llama la calle en la que estamos.</p></prosody>''', "reprompt" : "Cómo se llama la calle en la que estamos?"},

                    {"speak" : '''<prosody rate="slow"><p>Por último, dígame en qué ciudad nos encontramos.</p></prosody>''', "reprompt" : "En qué ciudad nos encontramos?"}]
}

class State:
    def __init__(self, item = ENDED, step = 0):
        self.item = item                        # Item of the test in the current State
        self.step = step                        # Step of the current test item
        self.forward_numbers = 0                # True if has remembered straight list of numbers
        self.backward_numbers = 0               # True if has remembered reversed list of numbers
        self.f_words = []                       # List of valid words starting with F
        self.f_start_time = None                # Timestamp of when the F words step started, to count 1 min
        self.letters_last_time = None           # Timestamp of last letter response, in order to measure reaction time
        self.score = 0                          # Overall score of the current test
        self.calculations = []                  # List of calculated substractions of -7 starting from 100
        self.letter_mistakes = 29               # Number of letter mistakes (say yes when it's not A, etc)
        self.first_sentence = 0                 # 1 if user remembered first sentence perfectly
        self.second_sentence = 0                # 1 if user remembered second sentence perfectly
        self.transport = 0                      # 1 if the user is able to tell the category of train and bike
        self.measure = 0                        # 1 if the user is able to tell the category of ruler and clock
        self.unclued_recalls = []               # Words remembered without category clue
        self.clued_recalls = []                 # Words remembered with category clue
        self.choice_recalls = []                # Words remembered with multiple choice clue
        self.day = 0                            # Day of the month stated by user
        self.month = ""                         # Current month stated by user
        self.week = ""                          # Day of the week stated by user
        self.year = 0                           # Current year stated by user
        self.afaga = 0                          # True if user is able to say that we are in Afaga
        self.vigo = 0                           # True if user is able to say that we are in Vigo city
        self.date = ""                          # Date of test administration
        self.study_years = 0                    # Number of years of study (add 1 point if less than 12 years)
        self.user_id = 0                        # User ID number

    def set(self, item = ENDED, step = 0):
        self.item = item
        self.step = step
