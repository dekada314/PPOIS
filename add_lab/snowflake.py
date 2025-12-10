import turtle

screen = turtle.Screen()
screen.setup(1000, 1000)
t = turtle.Turtle()
t.speed(0)
t.left(90)
# t.hideturtle()

def draw_snowflake(x, y, length):
    t.penup()
    t.goto(x,y)
    t.pendown()
    coord = []
    k = 1.6 / 2.6
    
    for _ in range(5):
        t.forward(length)
        end_x, end_y = t.pos()
        
        new_x, new_y, new_length = x + k * (end_x - x),y + k * (end_y - y), k  * 0.63 * length
        coord.append([new_x, new_y, new_length])
        
        t.backward(length)
        t.right(72)
        
    return coord

def main():
    x, y, length = 0, 0, 425
    coord_to_draw = draw_snowflake(x, y, length)
    for _ in range(4):
        for _ in range(len(coord_to_draw)):
            coord_to_draw += (draw_snowflake(*(coord_to_draw.pop(0))))
            print(coord_to_draw)
        
if __name__ == '__main__':
    main()
    turtle.done()