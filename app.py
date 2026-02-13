from flask import Flask, render_template, redirect, flash, request
import requests

ENDPOINT = 'https://api.thecatapi.com/v1/images/search'

app = Flask(__name__)
app.secret_key = "segredo"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cat', methods=['POST'])
def cat():

    nome = request.form.get('nome')

    if not nome:
        flash('Preencha o campo nome')
        return redirect('/')

    resposta = requests.get(ENDPOINT)

    if resposta.status_code == 200:
        dados = resposta.json()
        url_imagem = dados[0]['url']
    else:
        flash('Os gatos estão dormindo... volta mais tarde.')
        return redirect('/')

    return render_template('index.html', nome=nome, url_imagem=url_imagem)

if __name__ == '__main__':
    app.run(debug=True)
