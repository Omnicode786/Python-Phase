import tkinter as tk

window = tk.Tk()
window.title("Drawing App")
window.geometry("800x600")
window.configure(bg = "white")

































canvas = tk.Canvas(window, bg="white", width=800, height=600)
canvas.pack(fill=tk.BOTH, expand=True)

last_x, last_y = None, None

def on_press(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y
def on_drag(event):
    global last_x, last_y
    canvas.create_line(last_x,last_y,event.x,event.y,fill="black", width = 2)
    last_x,last_y = event.x, event.y
































canvas.bind("<Button-1>", on_press)      
canvas.bind("<B1-Motion>", on_drag)      

# Run the application
window.mainloop()
