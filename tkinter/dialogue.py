import tkinter as tk
from tkinter import ttk
from tkinter import *

from chatgpt_wrapper import ChatGPT

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
    
    generated_indialogue_text_file = open("./dynamically_gen_files/indialogue.txt", "w")
    generated_indialogue_text_file.write(output_text)
    generated_indialogue_text_file.close()

    return output_text

def process_input():
    # Get the input text from the text box
    character_text = character_box.get('1.0', 'end-1c')
    genre_text = genre_box.get('1.0', 'end-1c')
    location_text = location_box.get('1.0', 'end-1c')
    social_outcome_text = social_outcome_box.get('1.0', 'end-1c')
    input_prompt = 'Write an in-dialogue conversation'
    if character_text:
        character_string = 'explicitly between '+ character_text
        input_prompt+=character_string
    if genre_text:
        genre_string = 'based on '+ genre_text + ' genre'
        input_prompt+=genre_string
    if location_text:
        location_string = 'located in '+ location_text
        input_prompt+=location_string
    if social_outcome_text:
        social_outcome_string = 'which leads to an outcome where '+social_outcome_text
        input_prompt+=social_outcome_string
    
    method = sel()
    if method == '1':
        with open('./dynamically_gen_files/story.txt', 'r') as file:
            data = file.read().replace('\n', '')
        print("Read the story")
        temp_prompt = data + ' Use this above story and then '+ input_prompt
    else:
        temp_prompt = input_prompt

    output_text = process_text(temp_prompt)
    output_box.configure(state='normal')
    output_box.delete('1.0', 'end')
    output_box.insert('end', output_text)
    output_box.configure(state='disabled')


# Create the GUI
root = tk.Tk()
root.title('ECS 289G - Short Story Long - Project')

# Create the input text box
character_label = ttk.Label(root, text='Characters Involved', anchor='center')
character_label.pack(pady=5, fill='x')
character_box = tk.Text(root, height=10, width=50)
character_box.pack(padx=0,pady=10)

genre_label = ttk.Label(root, text='Genre', anchor='center')
genre_label.pack(pady=5, fill='x')
genre_box = tk.Text(root, height=1, width=50)
genre_box.pack(padx=0,pady=10)

location_label = ttk.Label(root, text='Location', anchor='center')
location_label.pack(pady=5, fill='x')
location_box = tk.Text(root, height=1, width=50)
location_box.pack(padx=0,pady=10)

social_outcome_label = ttk.Label(root, text='Social outcome', anchor='center')
social_outcome_label.pack(pady=5, fill='x')
social_outcome_box = tk.Text(root, height=1, width=50)
social_outcome_box.pack(padx=0,pady=10)

# Create the radio button
option_label = ttk.Label(root, text='Story Generation Method', anchor='center')
option_label.pack(pady=5, fill='x')

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)
   value = str(var.get())
   return value

var = IntVar()
R1 = Radiobutton(root, text="Take previous generated story into consideration", variable=var, value=1, command=sel)
R1.pack(anchor = 'center')

R2 = Radiobutton(root, text="Build completely new story", variable=var, value=2, command=sel)
R2.pack(anchor = 'center')
label = Label(root)
label.pack()

# Create the process button
process_button = ttk.Button(root, text='Process', command=process_input)
process_button.pack(pady=10)

# Create the output label and text box
output_label = ttk.Label(root, text='Output:', anchor='center')
output_label.pack(pady=10, fill='x')
output_box = tk.Text(root, height=10, width=50, state='disabled')
output_box.pack(pady=10)

# Open the box for writing edited prompt
def open_textbox():
    textbox = tk.Text(root, height=10, width=50)
    textbox.pack()
    
    def get_edit_text():
        edit_text = textbox.get("1.0", "end-1c")
        return edit_text
    
    def show_output():
        edit_input_text = get_edit_text()
        with open('./dynamically_gen_files/indialogue.txt', 'r') as file:
            data = file.read().replace('\n', '')
        # print("Read the in-dialogue story")
        edited_prompt = data + ' Build an in-dialogue conversation based on above conversation with new edits as '+ edit_input_text
        edit_output_text = process_text(edited_prompt)

        # Creating and displaying the output based on new prompt
        edit_output_label = tk.Label(root, text='Edited Output:', anchor='center')
        edit_output_label.pack(pady=10, fill='x')
        edit_output_box = tk.Text(root, height=10, width=50, state='disabled')
        edit_output_box.pack(pady=10)

        edit_output_box.configure(state='normal')
        edit_output_box.delete('1.0', 'end')
        edit_output_box.insert('end', edit_output_text)
        edit_output_box.configure(state='disabled')

    # Creating Submit button
    ok_button = ttk.Button(root, text="OK", command= show_output)
    ok_button.pack()

# Create the edit button
edit_button = ttk.Button(root, text="Edit", command=open_textbox)
edit_button.pack()

# Start the GUI
root.mainloop()
