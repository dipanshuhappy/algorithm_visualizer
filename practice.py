\\changes

  def run_mainloop(self):
         self.reset_screen()
         self.get_random_grid()
         self.draw_grid()
         while True:
            #  pygame.time.Clock().tick(100)
             self.handle_events()
             self.update_screen()
             self.draw_grid()
            #  self.get_random_grid()
             pygame.display.flip()
def run_game_of_life():
    Game((1400,800)).run_mainloop()
if __name__=='__main__':
    g=Game(( 1400, 800))



def quick_sort(data, head, tail, drawData, timeTick):
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, timeTick)

        #LEFT PARTITION
        quick_sort(data, head, partitionIdx-1, drawData, timeTick)

        #RIGHT PARTITION
        quick_sort(data, partitionIdx+1, tail, drawData, timeTick)
