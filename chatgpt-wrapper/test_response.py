# # from chatgpt_wrapper import ChatGPT

# # bot = ChatGPT()
# # prompt = "Write a story"
# # success, response, message = bot.ask(prompt)
# # if success:
# #     print(response)
# # else:
# #     raise RuntimeError(message)

from flask import Flask
from flask import jsonify
from flask_cors import CORS
import datetime
  
x = datetime.datetime.now()
  
# Initializing flask app
app = Flask(__name__)
CORS(app)
  
  
# Route for seeing a data
@app.route('/data')
def get_time():
  
    # Returning an api for showing in  reactjs
    res = {
        'Name':"geek", 
        "Age":"22",
        "Date":x, 
        "programming":"python"
        }
    
    return jsonify(res)
  
      
# Running app
if __name__ == '__main__':
    app.run(port=5000, debug=True)
