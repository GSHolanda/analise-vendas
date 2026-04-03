from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',          # ← sua senha aqui
        database='vendas_db'
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/dados')
def dados():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) as total FROM vendas")
    total = cursor.fetchone()['total']

    cursor.execute("SELECT ROUND(SUM(total), 2) as receita FROM vendas")
    receita = cursor.fetchone()['receita']

    cursor.execute("SELECT ROUND(AVG(rating), 2) as nota FROM vendas")
    nota = cursor.fetchone()['nota']

    cursor.execute("""
        SELECT product_line as label,
            ROUND(SUM(total), 2) as valor
        FROM vendas
        GROUP BY product_line
        ORDER BY valor DESC
    """)
    por_produto = cursor.fetchall()

    cursor.execute("""
        SELECT city as label,
            COUNT(*) as valor
        FROM vendas
        GROUP BY city
        ORDER BY valor DESC
    """)
    por_filial = cursor.fetchall()

    cursor.execute("""
        SELECT HOUR(time_venda) as label,
            COUNT(*) as valor
        FROM vendas
        GROUP BY label
        ORDER BY label
    """)
    por_hora = cursor.fetchall()

    conn.close()
    return jsonify({
        'total_vendas': total,
        'receita_total': float(receita),
        'avaliacao_media': float(nota),
        'por_produto': por_produto,
        'por_filial': por_filial,
        'por_hora': por_hora
    })

if __name__ == '__main__':
    app.run(debug=True)