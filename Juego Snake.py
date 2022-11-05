import turtle

class Snake():

    def __init__(self, color= 'green'):
        '''Inicializa los compoanentes del juego'''
        # Inicializa el lienzo


        self._screen = turtle.Screen()
        self._screen.title('Juego Snake')
        self._screen.bgcolor(color)
        self._screen.setup(height=800, width=600)
        #Inicializa la serpiente
        self.snake = turtle.Turtle()
        self.snake.speed(0)
        self.snake.shape('square')
        self.snake.color('black')
        self.snake.penup()
        self.snake.goto(0, 0)
        # Inicializa el texto que se muestra por pantalla
        self.texto = turtle.Turtle()
        self.texto.speed('0')
        self.texto.color('White')
        self.texto.hideturtle()
        self.texto.goto('0', '0 ')

        turtle.done()



juegosnake = Snake()




