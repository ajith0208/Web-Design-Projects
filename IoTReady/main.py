import json
from flask import Flask,render_template

with open('data.json') as file:
    data = json.load(file)

crate_table = data['crate_table']
sku_table = data['sku_table']

app = Flask(__name__)

@app.route('/')
def tables():
    return render_template('index.html', datas=data, skus=sku_table, crates = crate_table)


if __name__ == '__main__':
    app.run(debug=True)