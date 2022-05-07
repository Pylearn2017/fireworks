import turtle

def fire(x,y):
    angle = 0
    for hero in heroes_list:
        hero.setposition(x,y)
    for hero in heroes_list:
        hero.setheading(angle)
        angle += 40
    for i in range(50):
        for hero in heroes_list:
            hero.forward(10)

window = turtle.Screen()
window.bgcolor('#000000')

heroes_list = []
for i in range(9):
    hero = turtle.Turtle()
    hero.shape('circle')
    hero.color('#ffffff')
    hero.penup()
    heroes_list.append(hero)


window.onclick(fire)
window.mainloop()