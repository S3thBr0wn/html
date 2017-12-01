def main():
    win = GraphWin ('FACE', 400, 400)
    win.yUp() 
    
    head = Circle(Point(40,100), 25)
    head.setFill("#ffff00")
    head.draw(win)

    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill('#00ff00')
    eye1.draw(win)

    eye2 = Line(Point(45, 105), Point(55, 105))
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = Oval(Point(30, 90), Point(50, 85))
    mouth.setFill("#ff7f00")
    mouth.draw(win)

    label = Text(Point(100, 120), 'SMILE')
    label.draw(win)

    message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()

    main()
