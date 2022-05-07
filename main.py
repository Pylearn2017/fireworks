import turtle
import random

def fire(x,y):
    angle = 0
    for hero in heroes_list:
        hero.setposition(x,y)
    for hero in heroes_list:
        hero.setheading(angle)
        angle += 40 + random.randint(-10, 10)
    size = random.randint(30, 70)
    for i in range(size):
        for hero in heroes_list:
            step = random.randint(0, 2)
            hero.forward(step)

window = turtle.Screen()
window.bgcolor('#000000')

heroes_list = []
num_balls = random.randint(9, 19)
for i in range(num_balls):
    hero = turtle.Turtle()
    hero.shape('circle')
    hero.shapesize(0.3)
    random_color = (random.random(), 
                random.random(),
                random.random()
                )
    hero.color(random_color)
    hero.penup()
    hero.speed(0)
    heroes_list.append(hero)


window.onclick(fire)
window.mainloop()