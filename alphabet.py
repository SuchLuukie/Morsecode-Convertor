class Alphabet():
	"""Class for morsecode Alphabet"""
	def __init__(self):
		self.alphabet = {
			"a": ".-",
			"b": "-...",
			"c": "-.-.",
			"d": "-..",
			"e": ".",
			"f": "..-.",
			"g": "--.",
			"h": "....",
			"i": "..",
			"j": ".---",
			"k": "-.-",
			"l": ".-..",
			"m": "--",
			"n": "-.",
			"o": "---",
			"p": ".--.",
			"q": "--.-",
			"r": ".-.",
			"s": "...",
			"t": "-",
			"u": "..-",
			"v": "...-",
			"w": ".--",
			"x": "-..-",
			"y": "-.--",
			"z": "--..",
			"1": ".----",
			"2": "..---",
			"3": "...--",
			"4": "....-",
			"5": ".....",
			"6": "-....",
			"7": "--...",
			"8": "---..",
			"9": "----.",
			"0": "-----",
			" ": " "
		}

	#Retrieve the given letter inside the dictonary above.
	def convert(self, arg):
		string = self.alphabet.get(arg)

		#Return an array
		return [char for char in string]