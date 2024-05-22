from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///responses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar o objeto SQLAlchemy
db = SQLAlchemy(app)

# Definir o modelo de dados para o SQLAlchemy
class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    escuro_vs_escuro_30 = db.Column(db.String(150))
    escuro_vs_escuro_40 = db.Column(db.String(150))
    escuro_30_vs_escuro_40 = db.Column(db.String(150))
    claro_vs_claro_30 = db.Column(db.String(150))
    claro_vs_claro_40 = db.Column(db.String(150))
    claro_30_vs_claro_40 = db.Column(db.String(150))
    escuro_vs_claro_30 = db.Column(db.String(150))
    escuro_vs_claro_40 = db.Column(db.String(150))
    escuro_vs_claro = db.Column(db.String(150))

# Criar tabelas no banco de dados usando o contexto da aplicação
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Coletar dados do formulário e criar um objeto Response
        response = Response(
            familiarity = request.form['familiarity'],
            escuro_vs_escuro_30=request.form['escuro_vs_escuro_30'],
            escuro_vs_escuro_40=request.form['escuro_vs_escuro_40'],
            escuro_30_vs_escuro_40=request.form['escuro_30_vs_escuro_40'],
            claro_vs_claro_30=request.form['claro_vs_claro_30'],
            claro_vs_claro_40=request.form['claro_vs_claro_40'],
            claro_30_vs_claro_40=request.form['claro_30_vs_claro_40'],
            escuro_vs_claro_30=request.form['escuro_vs_claro_30'],
            escuro_vs_claro_40=request.form['escuro_vs_claro_40'],
            escuro_vs_claro=request.form['escuro_vs_claro']
        )
        db.session.add(response)
        db.session.commit()
        return render_template('result.html', data=request.form)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
