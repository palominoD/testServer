from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/searvices.html')
def searvices():
    return render_template('searvices.html')

@app.route('/shop.html')
def shop():
    return render_template('shop.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 2020)
