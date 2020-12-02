class Visual(object):
	"""Settings for visuals."""
	def __init__(self, root, canvas):
		self.ellipseSize = 10
		self.barSizeX = 20
		self.barSizeY = self.ellipseSize

		self.letterGap = self.ellipseSize
		self.wordGap = self.ellipseSize * 7

		self.root = root
		self.canvas = canvas

	#Create ellipse and given position
	def createDit(self, pos):
		self.id = self.canvas.create_oval(pos[0], pos[1], pos[0] + self.ellipseSize, pos[1] + self.ellipseSize, fill="black")
		return self.id

	#Create rectangle and given position
	def createDah(self, pos):
		self.id = self.canvas.create_rectangle(pos[0], pos[1], pos[0] + self.barSizeX, pos[1] + self.barSizeY, fill='black')
		return self.id