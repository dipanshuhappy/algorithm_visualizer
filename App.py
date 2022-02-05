from distutils.command.build import build
import tkinter
from tkinter import Frame, ttk
class AlgorithmVisualizer(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('Algorithm Visualizer')
        self.geometry('500x500')
        self.create_algorithm_buttons()
    def create_algorithm_buttons(self):
        button_frame=ttk.Frame(self)
        button_frame.place(rely=0.5)
        game_of_life=ttk.Button(button_frame,text='Game of Life',width=self.width)
        game_of_life.grid(row=1,column=1)
        towers_of_hanoi=ttk.Button(button_frame,text='Towers of Hanoi',width=400)
        towers_of_hanoi.grid(row=2,column=1)
        selection_sort=ttk.Button(button_frame,text='Selection Sort',width=400)
        selection_sort.grid(row=3,column=1)
        quick_sort=ttk.Button(button_frame,text='Quick Sort',width=400)
        quick_sort.grid(row=4,column=1)
        bubble_sort=ttk.Button(button_frame,text='Bubble Sort',width=400)
        bubble_sort.grid(row=5,column=1)
if __name__=='__main__':
    AlgorithmVisualizer().mainloop()
