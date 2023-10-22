from turtle import Turtle
from random import choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

cores_carros = [
    "#C0C0C0",  # Prata
    "#0000FF",  # Azul
    "#FF0000",  # Vermelho
    "#008000",  # Verde
    "#FFFF00",  # Amarelo
    "#FFA500",  # Laranja
    "#A52A2A",  # Marrom
    "#FFD700",  # Dourado
    "#C0C0C0",  # Prateado
    "#000080",  # Azul Marinho
    "#808000",  # Verde-oliva
    "#800080",  # Roxo
    "#FFC0CB",  # Rosa
    "#40E0D0",  # Turquesa
    "#F5F5DC",  # Bege
    "#8B4513",  # Marrom Escuro
    "#8B0000",  # Vermelho Escuro
    "#006400",  # Verde Escuro
    "#D3D3D3",  # Cinza Claro
    "#ADD8E6",  # Azul Claro
    "#00FF00",  # Verde Limão
    "#87CEEB",  # Azul Céu
    "#FFFFE0",  # Amarelo Pálido
    "#EE82EE",  # Violeta
    "#FF6F61",  # Coral
    "#FFFFF0"   # Marfim
]
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color(choice(cores_carros))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.penup()

        self.move_increment = MOVE_INCREMENT
        self.move_by = STARTING_MOVE_DISTANCE

        self.range_x = list(range(-300, 300+1, 60))
        self.range_y = list(range(-220,240+1, 50 ))
        self.local_to_go()

    def local_to_go(self):
        x = choice(self.range_x)
        y = choice(self.range_y)

        self.goto(x=x, y=y)
        self.range_x.remove(x)
        self.range_y.remove(y)
    
    def move_forward(self):
        self.forward(self.move_by)
    
    def restart_loop(self):
        self.goto(x= 320, y=self.ycor())

    def clear_cars(self):
        self.hideturtle()

