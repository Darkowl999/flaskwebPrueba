from flask import Flask,render_template

app = Flask(__name__)

#esta es la ruta de la pagina principal
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run()
