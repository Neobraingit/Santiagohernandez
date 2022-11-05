# Videojuego Snake con interfaz gráfica
import time
import turtle
screen = turtle.Screen()
screen.title('Esto es el título')
screen.bgcolor('green')
screen.setup(width=800, height=600)
t = turtle.Turtle()
t.goto(150, 5)
t.goto((-100, -30))
t.speed(0)
t.goto(200,30)
t.shape('square')
t.color('red')
t.penup()
t.write('Esto es texto escrito en el texto', align='center', font=('Courier', 24, 'normal'))
t2 = turtle.Turtle()
t2.sety(t2.ycor() + 100)
def move():
    t2.sety(t2.ycor() - 20)

move()

screen.listen()
screen.onkeypress(move, 's')
import time

t2.forward(20)

while True:
    screen.update()
    time.sleep(0.1)

screen.mainloop()

turtle.done()
