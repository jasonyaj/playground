from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', times = 0, color="")

@app.route('/play')
def play():
    return render_template('index.html', times = 3, color = 'blue')

@app.route('/play/<int:num>')
def multiply(num):
    return render_template('index.html', times=num, color = 'blue')

@app.route('/play/<int:num>/<string:color>')
def change_color(num, color):
    return render_template('index.html', times=num, color=color)

if __name__=='__main__':
    app.run(debug=True)