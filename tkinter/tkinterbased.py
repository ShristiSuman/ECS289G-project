import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from chatgpt_wrapper import ChatGPT
import requests
import shutil
import os
import re
import dalle

bot = ChatGPT()

def process_text(input_text):
    print("Inside process_text")
    success, response, message = bot.ask(input_text)
    print("Got resp")
    if success:
        output_text = response
    else:
        output_text = message
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

    #write the story to a text file for later usage
    generated_story_text_file = open("./dynamically_gen_files/story.txt", "w")
    generated_story_text_file.write(output_text)
    generated_story_text_file.close()

    output_box.configure(state='normal')
    output_box.delete('1.0', 'end')
    output_box.insert('end', output_text)
    output_box.configure(state='disabled')

def generate_character_profile():

    generated_story_file = open("./dynamically_gen_files/story.txt", "r")
    generated_story = generated_story_file.read()
    generated_story_file.close()
    char_profile_prompt_file = open("./char_profile_prompt.txt")
    char_profile_prompt = char_profile_prompt_file.read()
    char_profile_prompt_file.close()
    fin_char_profile_prompt = generated_story + "\n" + char_profile_prompt
    
    success, response, message = bot.ask(fin_char_profile_prompt)

    if success:
        output_text = response
    else:
        output_text = message

    # Split the contents into separate character profiles
    print(output_text)
    profiles = output_text.split('##########\n')
    print(profiles)

    char_file_names = []

    # Process each character profile
    for i in range(1, len(profiles)):
        profile = profiles[i]

        name_regex = r"Name: (\w+)"
        name_match = re.search(name_regex, profile)
        if name_match:
            name = name_match.group(1)
        print("\n" + name)

        # Create a new file with the name of the character
        char_file_name = './dynamically_gen_files/char_' + name + '.txt'
        char_file_names.append(char_file_name)
        with open(char_file_name, 'w') as outfile:
            # Write the character's profile to the file
            outfile.write(profile)
            print("File created")
    
    # iterate over the file paths and create a text box for each file
    # for i, file_path in enumerate(char_file_names):
        
    #     with open(file_path, "r") as f:
    #         contents = f.read()

    #         canvas_img = tk.Canvas(frame, width=256, height=256)
    #         canvas_img.pack()

    #         url = dalle.generate_visual_character(contents + "\nGenerate a character which suits the above description")
    #         res = requests.get(url, stream = True)
    #         new_file_path = file_path[:-3] + "png"
    #         with open(new_file_path,'wb') as f:
    #             shutil.copyfileobj(res.raw, f)
            
    #         char_text_box = tk.Text(frame, height=10, width=50, state='disabled')
    #         char_text_box.pack(pady=10)
    #         char_text_box.configure(state='normal')
    #         char_text_box.delete('1.0', 'end')
    #         char_text_box.insert('end', contents)
    #         char_text_box.configure(state='disabled')

    #         img_tk = ImageTk.PhotoImage(Image.open(new_file_path))
    #         canvas_img.img_tk = img_tk
    #         canvas_img.create_image((10,10),anchor='nw',image=img_tk)

    # Create a frame to contain the text box and canvas
    bb_frame = tk.Frame(frame)
    bb_frame.pack()

    # iterate over the file paths and create a text box for each file
    for i, file_path in enumerate(char_file_names):
        
        with open(file_path, "r") as f:
            contents = f.read()

            canvas_img = tk.Canvas(bb_frame, width=256, height=256)
            canvas_img.grid(row=i, column=1, padx=10, pady=10)

            url = dalle.generate_visual_character(contents + "\nGenerate a character which suits the above description")
            res = requests.get(url, stream = True)
            new_file_path = file_path[:-3] + "png"
            with open(new_file_path,'wb') as f:
                shutil.copyfileobj(res.raw, f)
            
            char_text_box = tk.Text(bb_frame, height=10, width=50, state='disabled')
            char_text_box.grid(row=i, column=0, padx=10, pady=10)
            char_text_box.configure(state='normal')
            char_text_box.delete('1.0', 'end')
            char_text_box.insert('end', contents)
            char_text_box.configure(state='disabled')

            img_tk = ImageTk.PhotoImage(Image.open(new_file_path))
            canvas_img.img_tk = img_tk
            canvas_img.create_image((10,10),anchor='nw',image=img_tk)


def cleanup():
    dir = './dynamically_gen_files'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

#cleanup of the dynamically gen files
cleanup()

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

# Create the generate button
gen_button = ttk.Button(frame, text='Generate character profile', command=generate_character_profile)
gen_button.pack(pady=10)

# Start the GUI
root.mainloop()
