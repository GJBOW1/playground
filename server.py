from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play')
def playing():
    return render_template('play.html')

@app.route('/play/<int:num>')
def multiply_boxes(num):
    return render_template("multiple_boxes.html", _number=num)

@app.route('/play/<int:num>/<color>')
def change_color(num, color):
    return render_template("color.html", _number=num, color=color)


if __name__ == "__main__":
    app.run(debug = True, port=5001)
