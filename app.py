from flask import Flask
app=Flask(__name__)
counter = 0

@app.route('/')
def index():
    global counter
    counter += 1
    return f'{counter}'

if __name__=="__main__":
  app.run(host='0.0.0.0', debug=True)