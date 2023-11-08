from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/')
def home():
   return send_from_directory('swagger', 'index.html')

@app.route('/hi')
def test():
   return "This is a test page"

if __name__ == '__main__':
   app.run()