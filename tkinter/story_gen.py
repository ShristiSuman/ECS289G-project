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
    output_text="passed"
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
    global char_list
    global trait_list
    # Get the input text from the text box
    input_text = input_box.get('1.0', 'end-1c')
    genre_text = genre_box.get('1.0', 'end-1c')
    intro_text = intro_box.get('1.0', 'end-1c')
    climax_text = climax_box.get('1.0', 'end-1c')
    input_prompt = 'Write an story '
    if genre_text:
        genre_string = 'based on '+ genre_text + ' genre '
        input_prompt+=genre_string
    if input_text:
        input_string = 'based on '+ input_text
        input_prompt+=input_string
    if char_list:
        character_string = ' with' +str(len(char_list))+ ' characters with the names ' + str(char_list) +' and their corresponding traits being '+ str(trait_list)
        input_prompt+=character_string
    if intro_text:
        intro_string = 'that starts with '+ intro_text
        input_prompt+=intro_string
    if climax_text:
        climax_string = 'that ends with'+climax_text
        input_prompt+=climax_string
    # input_text = input_box.get('1.0', 'end-1c')
    # input_text = input_box.get('1.0', 'end-1c')
    # Process the input and display the output
    print(input_prompt)
    output_text = process_text(input_prompt)
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
    
def calc():
    global x
    print("calc")
    x=0
    x=int(a.get())
    print(x)
    x=x-1
    create_character()

def gettingfunc(character_box,trait_box,character_label,trait_label,button2):
    root.after(0, button2.destroy)
    print("gettingfunc")
    character_text = character_box.get('1.0', 'end-1c')
    char_list.append(character_text)
    print(char_list)
    trait_text = trait_box.get('1.0', 'end-1c')
    trait_list.append(trait_text)
    print(trait_list)
    button_1 = tk.Button(root, text ="Finish", command = lambda:[character_box.destroy(),character_label.destroy(),trait_box.destroy(),trait_label.destroy(),add_character(button_1)])
    
#Exteral paddign for the buttons
    button_1.pack(pady = 40)
    #add_character()

def add_character(button_1):
    root.after(0, button_1.destroy)
    button_1.destroy
    print("add character")
    global char_list
    global trait_list
    global x
    print(x)
    if(x>0):
        x=x-1
        create_character()

def create_character():
    print("create character")
    character_label = ttk.Label(root, text='Character Name', anchor='center')
    character_label.pack(pady=50, fill='x')
    character_box = tk.Text(root, height=1, width=50)
    character_box.pack(padx=0,pady=10)
    
#character_box.config(command=character_box.pack_forget) 
    trait_label = tk.Label(root, text='Character Traits', anchor='center')
    trait_label.pack(pady=5, fill='x')
    trait_box = tk.Text(root, height=1, width=50)
    trait_box.pack(padx=0,pady=10)
    #trait_box.config(command=trait_box.pack_forget) 
    button2=tk.Button(root,text="Record Data",command=lambda:[gettingfunc(character_box,trait_box,character_label,trait_label,button2)])
    button2.pack(pady = 40)

   







# Create the GUI
root = tk.Tk()
root.title('ECS 289G - Short Story Long - Project')

canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar.config(command=canvas.yview)


# scrollbar = tk.Scrollbar(root, command=canvas.yview)
# scrollbar.pack(side=tk.LEFT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

frame = tk.Frame(canvas, height=1000)
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

intro_label = ttk.Label(frame, text='Intro', anchor='center')
intro_label.pack(pady=5, fill='x')
intro_box = tk.Text(frame, height=1, width=50)
intro_box.pack(padx=0,pady=10)

climax_label = ttk.Label(frame, text='Climax', anchor='center')
climax_label.pack(pady=5, fill='x')
climax_box = tk.Text(frame, height=1, width=50)
climax_box.pack(padx=0,pady=10)

char_list=[]
trait_list=[]

tk.Label(frame, text="Enter Number of Characters", font=('Calibri 10')).pack()
a=tk.Entry(frame, width=35)
a.pack()
gen_button = ttk.Button(frame, text='Enter Details', command=calc)
gen_button.pack(pady=10)

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
