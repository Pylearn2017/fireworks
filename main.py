import turtle
import random

def crete_heroes(x,y):
    angle = 0
    heroes_list = []
    num_balls = random.randint(7, 12)
    for i in range(num_balls):
        hero = turtle.Turtle()
        hero.shape('circle')
        hero.shapesize(random.randint(1, 3) / 10)
        hero.setposition(x,y)
        random_color = (random.random(), 
                    random.random(),
                    random.random()
                    )
        hero.color(random_color)
        hero.penup()
        hero.speed(0)
        angle += 360/num_balls + random.randint(-10, 10)
        hero.setheading(angle)
        hero.line = 100
        heroes_list.append(hero)
    return heroes_list

def create_window():
    window = turtle.Screen()
    window.bgcolor('#000000')
    window.tracer(0)
    window.onclick(fire)

def fire(x,y):
    if len(window.turtles()) > 30:
        window.clear()
        create_window()
    print(len(window.turtles()))
    heroes_list = crete_heroes(x,y)
    for i in range(100):
        for hero in window.turtles():
            step = random.randint(0, 1)
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