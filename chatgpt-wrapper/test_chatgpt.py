from chatgpt_wrapper import ChatGPT

def call():
    bot = ChatGPT()
    prompt = "Write a story"
    success, response, message = bot.ask(prompt)
    file1 = open('mystory.txt', 'w')
    if success:
        file1.write(response)
    else:
        file1.write(message)
    file1.close()

if __name__ == '__main__':
    call()
