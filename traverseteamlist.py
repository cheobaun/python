colors = []

while True:
    color = input("Enter a color (enter 'q' to quit): ")
    if color == 'q':
        break
    colors.append(color)

stop = len(colors)

for i in range(stop):
    print(colors[i])
