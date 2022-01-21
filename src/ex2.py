import tkinter as tk
import traceback
from queue import Queue
from threading import Thread
from tkinter import Canvas, Frame, Label, Tk
from typing import Any

from utils.input import int_input
from utils.prints import Color

def make_window() -> None:
	"""
	Crée la fenêtre du graphique.

	:return: None
	:rtype: None
	"""
	window: Tk = tk.Tk()
	window.title("Window")
	window.geometry("400x400")
	window.resizable = False
	frame: Frame = tk.Frame(window)
	frame.pack(fill = tk.BOTH, expand = 1)

	canvas: Canvas = tk.Canvas(frame, width = 400, height = 400)
	canvas.create_line(50, 250, 350, 250)
	canvas.create_line(100, 250, 100, 50)
	canvas.create_line(300, 250, 300, 50)
	canvas.create_line(300, 50, 100, 50)

	canvas.create_line(50, 250, 100, 50)
	canvas.create_line(350, 250, 300, 50)
	canvas.pack(fill = tk.BOTH, expand = 1)
	font: (str, int) = ("Helvetica", 12)

	label: Label = tk.Label(frame, text = "(A + B) * C * 0.5", font = font)
	label.place(anchor = "center", relx = 0.5, rely = 0.85)

	label_a: Label = tk.Label(frame, text = "A", font = font)
	label_a.place(anchor = "center", relx = 0.5, rely = 0.7)

	label_b: Label = tk.Label(frame, text = "B", font = font)
	label_b.place(anchor = "center", relx = 0.7, rely = 0.35)

	label_c: Label = tk.Label(frame, text = "C", font = font)
	label_c.place(anchor = "center", relx = 0.5, rely = 0.07)

	window.mainloop()

class WindowWorker(Thread):
	""" Thread qui gère la fenêtre graphique. """
	queue: Queue

	def __init__(self, queue: Queue) -> None:
		Thread.__init__(self)
		self.queue = queue

	def run(self) -> None:
		"""
		Ouvre le graphique et attend les entrées de l'utilisateur.

		:return: None
		:rtype: None
		"""
		while True:
			self.queue.get()
			try:
				make_window()
			except BaseException as e:
				traceback.print_exception(e)
			finally:
				self.queue.task_done()

class TPWorker(Thread):
	""" Thread qui gère le traitement du TP. """
	queue: Queue

	def __init__(self, queue: Queue) -> None:
		super().__init__()
		self.queue = queue

	def run(self) -> None:
		"""
		Affiche la formule de calcul du trapèze ansi que le résultat.

		:return: None
		:rtype: None
		"""
		while True:
			a, b, c = self.queue.get()
			try:
				print(f"""{Color.PURPLE}Surface du trapèze = (A + B) * C * 0.5
La surface du trapèze est ({a} + {b}) * {c} * 0.5 = {int((a + b) * c * 0.5)}m{Color.END}""")
			finally:
				self.queue.task_done()

def ex2() -> None:
	"""
	Exercice 2: Calcul de la surface d'un trapèze.
	Bonus: Afficher la surface d'un trapèze dans une fenêtre graphique.

	:return: None
	:rtype: None
	"""
	first: int = int_input(text = "Rentrez A (en mètres) : ")
	second: int = int_input(text = "Rentrez B (en mètres) : ")
	third: int = int_input(text = "Rentrez C (en mètres) : ")

	queue: Queue[Any] = Queue()
	worker1: WindowWorker = WindowWorker(queue)
	worker2: TPWorker = TPWorker(queue)
	worker1.daemon = True
	worker2.daemon = True
	for i in range(2):
		queue.put((first, second, third))
	worker1.start()
	worker2.start()
	queue.join()
