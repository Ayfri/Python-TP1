import queue
import subprocess
import sys
import tkinter as tk
import threading
import traceback
from tkinter import Button
from tkinter.font import Font


queue = queue.Queue()

def openExercice(number: int) -> None:
	print(f"Opening exercice {number}")
	module = __import__(f"TP1.ex{number}")
	subModule = getattr(module, f"ex{number}")
	function = getattr(subModule, f"tp{number}")
	function()

def generateButtons(frm: tk.Frame) -> None:
	for i in range(1, 8):
		button: Btn = Btn(queue, i)
		button.createButton(frm)

class TextRedirector(object):
	def __init__(self, widget: tk.Text, tag="stdout") -> None:
		self.widget = widget
		self.tag = tag

	def readline(self, *string: str, **kargs) -> str:
		self.widget.configure(state="normal")
		self.widget.insert("end", *string, self.tag)
		self.widget.configure(state="disabled")
		return string

	def flush(self) -> None:
		pass

	def write(self, string: str) -> None:
		self.widget.configure(state="normal")
		self.widget.insert("end", string, self.tag)
		self.widget.configure(state="disabled")

class Btn(threading.Thread):
	btn: Button
	font: Font

	def __init__(self, q, number: int):
		super().__init__()
		self.queue = q
		self.number = number
		self.worker = True
		self.font = Font(family="Helvetica", size=13)

	def run(self) -> None:
		queue.put("")
		while True:
			try:
				self.queue.get()
				terminalText.enable()
				sys.stdout = TextRedirector(terminalText.text)
				def event(event: tk.Event) -> None:
					if event.char.isascii() and event.char.isprintable():
						sys.stdout.write(event.char)

				terminalText.text.bind("<Key>", event)
				terminalText.text.bind("<Delete>", lambda _: sys.stdout.write("\b"))
				terminalText.text.bind("<BackSpace>", lambda _: sys.stdout.write("\b"))
				terminalText.text.bind("<Return>", lambda _: sys.stdout.readline())
				terminalText.text.bind("<Tab>", lambda _: sys.stdout.write("\t"))

				print(terminalText.text.configure(state=tk.NORMAL), terminalText.text["state"])
				openExercice(self.number)
			except BaseException as e:
				traceback.print_exception(e)
			finally:
				self.queue.task_done()

	def createButton(self, frm: tk.Frame) -> None:
		self.btn = Button(frm, text=f"Exercice {self.number}", bg='gray', fg='white', font=self.font, command=self.start)
		self.btn.configure(height=3, width=15, relief='solid', overrelief='solid', font=self.font)
		self.btn.grid(row=self.number, column=0)

class TerminalBox:
	text: tk.Text

	def __init__(self, frm: tk.Frame):
		self.font = Font(family="Helvetica", size=13)

		self.text = tk.Text(frm, height=100, width=150, font=self.font)
		self.text.grid(row=0, column=0)
		self.disable()

	def redirector(self, inputStr: str) -> None:
		self.text.insert(tk.INSERT, inputStr)

	def enable(self) -> None:
		self.text.configure(state="normal")

	def disable(self) -> None:
		self.text.configure(state="disabled")


root = tk.Tk()
root.geometry("1600x900")
root.tk_setPalette(background='#000000', foreground='#ffffff')
buttonsFrame = tk.Frame(root, bg='black')
buttonsFrame.grid(row=0, column=0, sticky="nsew")

terminalFrame = tk.Frame(root, width=1600, bg='black')
terminalFrame.grid(row=0, column=1, sticky="nsew")
terminalText = TerminalBox(terminalFrame)

generateButtons(buttonsFrame)

queue.join()
root.mainloop()
