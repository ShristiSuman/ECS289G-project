import tkinter as tk
from chatgpt_wrapper import ChatGPT
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
    return output_text

def process_input():
    # Get the input text from the text box
    input_text = input_box.get('1.0', 'end-1c')

    # Process the input and display the output
    output_text = process_text(input_text)
    output_box.configure(state='normal')
    output_box.delete('1.0', 'end')
    output_box.insert('end', output_text)
    output_box.configure(state='disabled')

def generate_image():
    # Get the input text from the text box
    input_text = input_box_character.get('1.0', 'end-1c')

    # Process the input and display the output
    output = dalle.generate_visual_character(input_text)
    output_box.configure(state='normal')
    output_box.delete('1.0', 'end')
    output_box.insert('end', output_text)
    output_box.configure(state='disabled')

# Create the GUI
root = tk.Tk()
root.title('Text Processor')

# Create the input text box
input_box = tk.Text(root, height=10, width=50)
input_box.pack(pady=10)

# Create the process button
process_button = tk.Button(root, text='Process', command=process_input)
process_button.pack()

# Create the output text box
output_box = tk.Text(root, height=10, width=50, state='disabled')
output_box.pack(pady=10)

# Create the input text box
input_box_character = tk.Text(root, height=10, width=50)
input_box_character.pack(pady=10)

# Create the generate button
gen_button = tk.Button(root, text='Generate', command=generate_image)
gen_button.pack()

# Start the GUI
root.mainloop()
