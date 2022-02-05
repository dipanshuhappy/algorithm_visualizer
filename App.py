
from tkinter import Frame, ttk, Tk
class AlgorithmVisualizer(Tk):
    def __init__(self):
        super().__init__()
        self.title('Algorithm Visualizer')
        self.geometry(f'{self.winfo_screenwidth()}x{self.winfo_screenheight()}')
        self.create_algorithm_buttons()
    def create_algorithm_buttons(self):
        button_frame=ttk.Frame(self)
        button_frame.place(rely=0.5)
        game_of_life=ttk.Button(button_frame,text='Game of Life',width=50,command=self.on_game_of_life)
        game_of_life.grid(row=0,column=0)
        self.config(bg = "skyblue")      
        towers_of_hanoi=ttk.Button(button_frame,text='Towers of Hanoi',width=50,command=self.on_towers_of_hanoi)
        towers_of_hanoi.grid(row=1,column=1)
        selection_sort=ttk.Button(button_frame,text='Selection Sort',width=50,command=self.on_selection_sort)
        selection_sort.grid(row=0,column=2)
        quick_sort=ttk.Button(button_frame,text='Quick Sort',width=50,command=self.on_quick_sort)
        quick_sort.grid(row=1,column=3)
        bubble_sort=ttk.Button(button_frame,text='Bubble Sort',width=50,command=self.on_game_of_life)
        bubble_sort.grid(row=0,column=4)
    def on_game_of_life(self):
        from game_of_life.game_of_life import run_game_of_life
        run_game_of_life()
    def on_towers_of_hanoi(self):
        from towers_of_hanoi.towers_of_hanoi import run_towers_of_hanoi
        run_towers_of_hanoi()
    def on_selection_sort(self):
        from selection_sort.SelectionSortVisualisation import run_sort_visualisation
        run_sort_visualisation()
    def on_quick_sort(self):
        from quick_sort.finalcseproject2 import run_quick_sort
        self.destroy()
        run_quick_sort()
if __name__=='__main__':
    AlgorithmVisualizer().mainloop()
