import tkinter as tk
import traceback
from queue import Queue
from threading import Thread

from utils.input import intInput

def makeWindow() -> None:
	"""
	Crée la fenêtre du graphique.
	:return: None
	:rtype: None
	"""
	window = tk.Tk()
	window.title("Window")
	window.geometry("400x400")
	window.resizable = False
	frame = tk.Frame(window)
	frame.pack(fill=tk.BOTH, expand=1)

	canvas = tk.Canvas(frame, width=400, height=400)
	canvas.create_line(50, 250, 350, 250)
	canvas.create_line(100, 250, 100, 50)
	canvas.create_line(300, 250, 300, 50)
	canvas.create_line(300, 50, 100, 50)

	canvas.create_line(50, 250, 100, 50)
	canvas.create_line(350, 250, 300, 50)
	canvas.pack(fill=tk.BOTH, expand=1)
	font = ("Helvetica", 12)

	label = tk.Label(frame, text="(A + B) * C * 0.5", font=font)
	label.place(anchor="center", relx=0.5, rely=0.85)

	labelA = tk.Label(frame, text="A", font=font)
	labelA.place(anchor="center", relx=0.5, rely=0.7)

	labelB = tk.Label(frame, text="B", font=font)
	labelB.place(anchor="center", relx=0.7, rely=0.35)

	labelC = tk.Label(frame, text="C", font=font)
	labelC.place(anchor="center", relx=0.5, rely=0.07)

	window.mainloop()

class WindowWorker(Thread):
	""" Thread qui gère la fenêtre graphique. """
	queue: Queue

	def __init__(self, queue: Queue) -> None:
		Thread.__init__(self)
		self.queue = queue

	def run(self) -> None:
		while True:
			self.queue.get()
			try:
				makeWindow()
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
		while True:
			a, b, c = self.queue.get()
			try:
				print(f"""Surface du trapèze = (A + B) * C * 0.5
La surface du trapèze est ({a} + {b}) * {c} * 0.5 = {int((a + b) * c * 0.5)}m""")
			finally:
				self.queue.task_done()

def ex2() -> None:
	"""
	Exercice 2: Calcul de la surface d'un trapèze.
	Bonus: Afficher la surface d'un trapèze dans une fenêtre graphique.
	:return: None
	:rtype: None
	"""
	first: int = intInput(text="Rentrez A (en mètres) : ")
	second: int = intInput(text="Rentrez B (en mètres) : ")
	third: int = intInput(text="Rentrez C (en mètres) : ")

	queue = Queue()
	worker1 = WindowWorker(queue)
	worker2 = TPWorker(queue)
	worker1.daemon = True
	worker2.daemon = True
	for i in range(2):
		queue.put((first, second, third))
	worker1.start()
	worker2.start()
	queue.join()
