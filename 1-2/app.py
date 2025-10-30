from flask import Flask, render_template

app = Flask(__name__)

# 기본 라우트
@app.route('/')
def index():
    return "<h1>Welcome to the Coffee Shop!</h1>"

# 문제 5에서 추가할 /menu 라우트
@app.route('/menu')
def menu():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True)