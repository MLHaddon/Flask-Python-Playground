from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
  return render_template('index.html')

@app.route('/play')
def play():
  return render_template('play.html', x = 3, color = 'blue')

@app.route('/play/<x>')
def playNum(x):
  return render_template('play.html', x = int(x), color = 'blue')

@app.route('/play/<x>/<color>')
def color(x, color):
  return render_template('play.html', x = int(x), color = color)

if __name__ == '__main__':
  app.run(debug = True, port = 8000)