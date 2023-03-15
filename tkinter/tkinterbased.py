import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from chatgpt_wrapper import ChatGPT
import requests
import shutil
import dalle


def process_text(input_text):
    # Replace this with your own function that processes the input
    print("Inside process_text")
    bot = ChatGPT()
    success, response, message = bot.ask(input_text)
    print("Got resp")
    if success:
        output_text = response
    else:
        output_text = message
    # output_text = "Output:  " + input_text #+" where the genre is "+ genre+ "with"+ no_char+" characters whose names are "
    return output_text

def process_input():
    # Get the input text from the text box
    input_text = input_box.get('1.0', 'end-1c')
    genre_text = genre_box.get('1.0', 'end-1c')
    nochar_text = no_character_box.get('1.0', 'end-1c')
    # input_text = input_box.get('1.0', 'end-1c')
    # input_text = input_box.get('1.0', 'end-1c')
    # Process the input and display the output
    output_text = process_text(input_text)
    output_box.configure(state='normal')
    output_box.delete('1.0', 'end')
    output_box.insert('end', output_text)
    output_box.configure(state='disabled')

def generate_image():
    input_text = char_viz_box.get('1.0', 'end-1c')
    canvas_img = tk.Canvas(frame, width=256, height=256)
    canvas_img.pack()

    url = dalle.generate_visual_character(input_text)
    res = requests.get(url, stream = True)
    file_name = "char.png"
    with open(file_name,'wb') as f:
        shutil.copyfileobj(res.raw, f)

    img_tk = ImageTk.PhotoImage(Image.open(file_name))
    canvas_img.img_tk = img_tk
    canvas_img.create_image((10,10),anchor='nw',image=img_tk)
    

# Create the GUI
root = tk.Tk()
root.title('ECS 289G - Short Story Long - Project')

canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(root, command=canvas.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

frame = tk.Frame(canvas, height=200)
canvas.create_window((0, 0), window=frame, anchor='nw')

canvas.configure(scrollregion=canvas.bbox('all'))
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))


# Create the input text box
genre_label = ttk.Label(frame, text='Description', anchor='center')
genre_label.pack(pady=5, fill='x')
input_box = tk.Text(frame, height=10, width=50)
input_box.pack(padx=0,pady=10)

genre_label = ttk.Label(frame, text='Genre', anchor='center')
genre_label.pack(pady=5, fill='x')
genre_box = tk.Text(frame, height=1, width=50)
genre_box.pack(padx=0,pady=10)

char_label = ttk.Label(frame, text='Number of Characters', anchor='center')
char_label.pack(pady=5, fill='x')
no_character_box = tk.Text(frame, height=2, width=5)
no_character_box.pack(pady=10)

nochar_text = no_character_box.get('1.0', 'end-1c')
i=0
char_list=[]


# Create the process button
process_button = ttk.Button(frame, text='Process', command=process_input)
process_button.pack(pady=10)

# Create the output label and text box
output_label = ttk.Label(frame, text='Output:', anchor='center')
output_label.pack(pady=10, fill='x')
output_box = tk.Text(frame, height=10, width=50, state='disabled')
output_box.pack(pady=10)

#Create input prompt for character generation
char_viz_label = ttk.Label(frame, text='Describe the character', anchor='center')
char_viz_label.pack(pady=5, fill='x')
char_viz_box = tk.Text(frame, height=10, width=50)
char_viz_box.pack(padx=0,pady=10)

# Create the generate button
gen_button = ttk.Button(frame, text='Generate', command=generate_image)
gen_button.pack(pady=10)

# Start the GUI
root.mainloop()
