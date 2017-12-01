def main():
	win = GraphWin('FACE', 400, 400)
	win.yUp()
	
	pt = Point(100, 50)
	pt.draw(win)
	
	eye2 = Line(Point(55,105), Point(45, 105)) # set endpoints
	eye2.setWidth(3)
	eye2.draw(win)
	
	message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
	message.draw(win)
	win.getMouse()
	win.close()

main()
