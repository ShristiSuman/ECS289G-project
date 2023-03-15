import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

def process_text(input_text):
    # Replace this with your own function that processes the input
    output_text = "Output:  " + input_text #+" where the genre is "+ genre+ "with"+ no_char+" characters whose names are "
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

    # Create a canvas widget
    canvas = tk.Canvas(root, width=256, height=256)
    canvas.pack()

    # Use the canvas widget's create_image() method to display the image on the canvas
    img_tk = ImageTk.PhotoImage(Image.open("image.png"))
    canvas.create_image((10,10),anchor='nw',image=img_tk)

# Create the GUI
root = tk.Tk()
root.title('ECS 289G - Short Story Long - Project')
# Create the input text box
genre_label = ttk.Label(root, text='Description', anchor='center')
genre_label.pack(pady=5, fill='x')
input_box = tk.Text(root, height=10, width=50)
input_box.pack(padx=0,pady=10)

genre_label = ttk.Label(root, text='Genre', anchor='center')
genre_label.pack(pady=5, fill='x')
genre_box = tk.Text(root, height=1, width=50)
genre_box.pack(padx=0,pady=10)

char_label = ttk.Label(root, text='Number of Characters', anchor='center')
char_label.pack(pady=5, fill='x')
no_character_box = tk.Text(root, height=2, width=5)
no_character_box.pack(pady=10)

nochar_text = no_character_box.get('1.0', 'end-1c')
i=0
char_list=[]
#while(i<int(nochar_text)):
    
    #i=i+1





# Create the process button
process_button = ttk.Button(root, text='Process', command=process_input)
process_button.pack(pady=10)

# Create the output label and text box
output_label = ttk.Label(root, text='Output:', anchor='center')
output_label.pack(pady=10, fill='x')
output_box = tk.Text(root, height=10, width=50, state='disabled')
output_box.pack(pady=10)

#Create input prompt for character generation
char_viz_label = ttk.Label(root, text='Describe the character', anchor='center')
char_viz_label.pack(pady=5, fill='x')
char_viz_box = tk.Text(root, height=10, width=50)
char_viz_box.pack(padx=0,pady=10)

# Create the generate button
gen_button = ttk.Button(root, text='Generate', command=generate_image)
gen_button.pack(pady=10)

# Start the GUI
root.mainloop()
