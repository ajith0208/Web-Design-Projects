import requests
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/anagram_pairs', methods=['POST'])
def anagram():
    if request.method == 'POST':
        n = request.form.get('values').split(' ')
        c = request.form.get('values').split(' ')
        t = []
        while len(n) != 0:
            for j in n:
                if n[0] == j:
                    pass
                elif sorted(n[0]) == sorted(j):
                    t.append((n[0], j))
            n.remove(n[0])
    return render_template('anagram.html', words=c, pairs=t)


if __name__ == '__main__':
    app.run(debug=True)
