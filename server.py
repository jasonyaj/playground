from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def play():
    return render_template('play.html', times=3)

@app.route('/play/<int:num>')
def multiply(num):
    return render_template('num.html', times=num)

@app.route('/play/<int:num>/<string:color>')
def change_color(num, color):
    return render_template('color.html', times=num, color=color)

if __name__=='__main__':
    app.run(debug=True)