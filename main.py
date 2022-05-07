import turtle

def fire(x,y):
    hero.setposition(x,y)

window = turtle.Screen()
window.bgcolor('#000000')

hero = turtle.Turtle()
hero.shape('circle')
hero.color('#ffffff')


window.onclick(fire)
window.mainloop()