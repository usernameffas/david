import socket
from flask import Flask, render_template

app = Flask(__name__)

# 기본 라우트 (문제 8 요구사항에 따라 render_template을 사용하도록 수정)
@app.route('/')
def index():
    # 문제 8: 컴퓨터 이름 표시 기능 추가
    # app.debug는 app.run(debug=True) 설정 시 True가 됨
    if app.debug:
        # socket.gethostname()을 사용하여 현재 컴퓨터의 이름(호스트네임)을 가져옴
        hostname = '컴퓨터(인스턴스) : ' + socket.gethostname()
    else:
        hostname = ' ' # 디버그 모드가 아닐 경우 공백으로 설정

    # computername=hostname 인자를 추가하여 템플릿으로 전달
    return render_template('index.html', computername=hostname)

# 문제 5에서 추가할 /menu 라우트
@app.route('/menu')
def menu():
    return render_template('menu.html')
@app.route("/test1")
def test1():
    return render_template('test1.html')

if __name__ == '__main__':
    # 문제 8: app.run() 실행 시 debug=True 옵션 설정 (기존 코드에 이미 있음)
    app.run(debug=True)
