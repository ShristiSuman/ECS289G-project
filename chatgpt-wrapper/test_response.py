# # from chatgpt_wrapper import ChatGPT

# # bot = ChatGPT()
# # prompt = "Write a story"
# # success, response, message = bot.ask(prompt)
# # if success:
# #     print(response)
# # else:
# #     raise RuntimeError(message)

# from flask import Flask
# from flask import jsonify
# from flask_cors import CORS
# import datetime
# from chatgpt_wrapper import ChatGPT
# import nest_asyncio

# nest_asyncio.apply()
  
# x = datetime.datetime.now()
# bot = ChatGPT()
  
# # Initializing flask app
# app = Flask(__name__)
# CORS(app)
  
  
# # Route for seeing a data
# @app.route('/data')
# def get_time():
  
#     # Returning an api for showing in  reactjs
#     # res = {
#     #     'Name':"geek", 
#     #     "Age":"22",
#     #     "Date":x, 
#     #     "programming":"python"
#     #     }
#     success, response, message = bot.ask("Write a story")
#     print(response)

#     if success:
#         res = {'Story': response}
#     else:
#        res = {'Story': message}

#     return jsonify(res)
  
      
# # Running app
# if __name__ == '__main__':
#     app.run(port=5000, debug=True)


from flask import Flask, jsonify
from flask_cors import CORS
from chatgpt_wrapper import ChatGPT

  
# Initializing flask app
app = Flask(__name__)
CORS(app)


# Route for seeing a data
@app.route('/data')
def get_time():

    bot = ChatGPT()
    prompt = "Write a story"
    success, response, message = bot.ask(prompt)

    if success:
        res = {'Story': response}
    else:
        res = {'Story': message}

    return jsonify(res)


# Running app
if __name__ == '__main__':
    app.run(port=5000, debug=False)


