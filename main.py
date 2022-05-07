import turtle
import random

def crete_heroes(x,y):
    angle = 0
    heroes_list = []
    num_balls = random.randint(9, 19)
    for i in range(num_balls):
        hero = turtle.Turtle()
        hero.shape('circle')
        hero.shapesize(0.3)
        hero.setposition(x,y)
        random_color = (random.random(), 
                    random.random(),
                    random.random()
                    )
        hero.color(random_color)
        hero.penup()
        hero.speed(0)
        hero.setheading(angle)
        angle += random.randint(-10, 10)
        hero.line = 100
        heroes_list.append(hero)
    return heroes_list

def fire(x,y):
    crete_heroes(x,y)
    for i in range(100):
        for hero in window.turtles():
            step = random.randint(0, 2)
            hero.forward(step)
            hero.line -= 1
            if not hero.line:
                hero.reset()
        window.update()


window = turtle.Screen()
window.bgcolor('#000000')
window.tracer(0)
window.onclick(fire)
window.mainloop()