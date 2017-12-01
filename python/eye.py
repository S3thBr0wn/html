def main():
    win = GraphWin('FACE', 400, 400) # give title and dimensions
    win.yUp() # make right side up coordinates!
	head = Circle(Point(40,100),25)
    head.setFill("#ffff00")
    head.draw(win)
    message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()
main()
