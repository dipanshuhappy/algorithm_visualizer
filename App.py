
from tkinter import Frame, ttk, Tk
class AlgorithmVisualizer(Tk):
    def __init__(self):
        super().__init__()
        self.title('Algorithm Visualizer')
        self.geometry('500x500')
        self.create_algorithm_buttons()
    def create_algorithm_buttons(self):
        button_frame=ttk.Frame(self)
        button_frame.place(rely=0.5)
        game_of_life=ttk.Button(button_frame,text='Game of Life',width=50)
        game_of_life.grid(row=0,column=0)
        self.config(bg = "skyblue")      
        towers_of_hanoi=ttk.Button(button_frame,text='Towers of Hanoi',width=50)
        towers_of_hanoi.grid(row=1,column=1)
        selection_sort=ttk.Button(button_frame,text='Selection Sort',width=50)
        selection_sort.grid(row=0,column=2)
        quick_sort=ttk.Button(button_frame,text='Quick Sort',width=50)
        quick_sort.grid(row=1,column=3)
        bubble_sort=ttk.Button(button_frame,text='Bubble Sort',width=50)
        bubble_sort.grid(row=0,column=4)
if __name__=='__main__':
    AlgorithmVisualizer().mainloop()
