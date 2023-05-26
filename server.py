from flask import Flask
from flask import Flask, render_template,  request, redirect, session
import sqlite3 

from flask import Flask, render_template
import pandas as pd
from functools import wraps
import os 


app = Flask('inovatech')
db_file = 'usuarios.db'
app.secret_key = 'In0v4t3chPr0j3ct'


def verificar_banco_dados():
    return os.path.exists(db_file)

def criar_tabela():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''z
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

  

    
def analise_generica_xlsx(arquivo):
    df = pd.read_excel(arquivo)

    #num_linhas, num_colunas = df.shape
    colunas = df.columns.tolist()

    estatisticas = {}

    for coluna in colunas:
        dados_coluna = df[coluna]

        if dados_coluna.dtype == 'object':
            estatisticas[coluna] = {
                'Tipo de dados': dados_coluna.dtype,
                'Valores únicos': dados_coluna.nunique(),
                'Valor mais frequente': dados_coluna.mode().values[0],
            }
        else:
            estatisticas[coluna] = {
                'Tipo de dados': dados_coluna.dtype,
                'Valores únicos': dados_coluna.nunique(),
                'Valor mais frequente': dados_coluna.mode().values[0],
                'Média': dados_coluna.mean(),
                'Mediana': dados_coluna.median(),
                'Desvio padrão': dados_coluna.std()
            }

    return estatisticas
    
def autenticar_usuario(usuario, senha):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM usuarios
        WHERE usuario = ? AND senha = ?
    ''', (usuario, senha))
    result = cursor.fetchone()
    conn.close()
    if result:
        return True
    else:
        return False


def login_required(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        if 'usuario' in session:
            return route_function(*args, **kwargs)
        else:
            return redirect('/')
    return wrapper


@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    if autenticar_usuario(usuario, senha):
        session['usuario'] = usuario
        return redirect('/upload')
    else:
        return redirect('/')

@app.route('/')
def index():
    return render_template('tela_inicial.html', title='SmartSolutions')




@app.route('/upload', methods=['GET', 'POST'])
@login_required
def analisar_arquivo():
    if request.method == 'POST':
        arquivo = request.files['file']
        arquivo.save('arquivo.xlsx')
        estatisticas = analise_generica_xlsx('arquivo.xlsx')
      
        return render_template('grafico2.html', estatisticas=estatisticas)
    
    return render_template('uploadpage.html')

@app.route('/cadastro', methods=['POST'])
def cadastrar_usuario():
    usuario = request.form['usuario']
    senha = request.form['senha']
    senha_confirm = request.form['confirma_senha']
    
    if senha_confirm != senha:
        return "CONFIRMAÇÃO INCORRETA FODASE"

    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM usuarios WHERE usuario = ?
    ''', (usuario,))
    result = cursor.fetchone()

    if result:
        conn.close()
        return redirect('/?alert=exists')  # Redirect to '/' route with query parameter indicating user exists
    else:
        cursor.execute('''
            INSERT INTO usuarios (usuario, senha)
            VALUES (?, ?)
        ''', (usuario, senha))
        conn.commit()
        conn.close()
        return redirect('/?alert=success')  



if __name__ == '__main__':
    if not verificar_banco_dados():
        criar_tabela()
        print("novo banco de dados criado.")
    app.run(debug=True)
