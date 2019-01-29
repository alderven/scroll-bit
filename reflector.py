import scrollbit
import random

X_MAX = 16
Y_MAX = 6

x = random.randint(0, X_MAX+1)
y = random.randint(0, Y_MAX+1)
x_direction = random.choice([-1, 1])
y_direction = random.choice([-1, 1])

while True:
    
    for x_ in range(0, X_MAX+1):
        for y_ in range(0, Y_MAX+1):
            brightness = scrollbit.get_pixel(x_, y_)
            if brightness:
                scrollbit.set_pixel(x_, y_, brightness-15)
    
    scrollbit.set_pixel(x, y, 255)
    scrollbit.show()
        
    x += x_direction
    y += y_direction

    if x < 0 or x > X_MAX:
        x_direction *= -1
        x = 0 if x < 0 else X_MAX
    
    if y < 0 or y > Y_MAX:
        y_direction *= -1
        y = 0 if y < 0 else Y_MAX
