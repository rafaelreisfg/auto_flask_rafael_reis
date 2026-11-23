from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    gasolina = None
    etanol = None
    result = None
    message = None

    if request.method == 'POST':
        gasolina = float(request.form.get('gasolina','').replace(',','.'))
        etanol = float(request.form.get('etanol','').replace(',','.'))
        result = 'Etanol' if etanol <= gasolina * 0.75 else 'Gasolina'
        message = f'Melhor abasatecer com {result}.'

    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
