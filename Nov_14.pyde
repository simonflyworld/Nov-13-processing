def setup():
    size(640,480)

def draw_player():
    print("fraw_player")

def draw_sun(x,y):
    print({x},{y})
    ellipse(x,y,50,50)



 
draw_player()
for i in range(0,10,1):
    draw_sun(2+i,3+i)
