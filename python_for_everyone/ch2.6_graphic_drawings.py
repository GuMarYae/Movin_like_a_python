from ezgraphics import GraphicsWindow

#create a graphic window
win = GraphicsWindow()

canvas = win.canvas()
canvas.drawRect(5, 10, 20, 30)

win.wait()
