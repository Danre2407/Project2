from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/hi')
def test():
   return "This is a test page"

if __name__ == '__main__':
   app.run()