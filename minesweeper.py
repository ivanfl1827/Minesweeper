from tkinter import *
import settings
import utilities

root = Tk()
#Override the settings of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='red', #change later to black
    width = settings.WIDTH,
    height = utilities.height_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='blue', #change later to black
    width = utilities.width_prct(25),
    height = utilities.height_prct(75)

)
left_frame.place(x=0, y=utilities.height_prct(25))

#Run the window
root.mainloop()