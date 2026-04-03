import pandas as pd
import mysql.connector

df = pd.read_csv('vendas.csv')
print(f"CSV carregado: {len(df)} registros encontrados")

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',      
        database='vendas_db',
        connection_timeout=10
    )
    print("✅ Conexão com MySQL OK!")
except Exception as e:
    print(f"❌ Erro de conexão: {e}")
    exit()

cursor = conn.cursor()

inseridos = 0
erros = 0
for _, row in df.iterrows():
    try:
        cursor.execute("""
            INSERT INTO vendas (
                invoice_id, branch, city, customer_type, gender,
                product_line, product, unit_price, quantity, tax, total,
                date_venda, time_venda, payment, cogs,
                gross_margin, gross_income, rating
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (
            row['invoice_id'], row['branch'], row['city'],
            row['customer_type'], row['gender'], row['product_line'],
            row['product'], row['unit_price'], row['quantity'],
            row['tax'], row['total'], row['date_venda'],
            row['time_venda'], row['payment'], row['cogs'],
            row['gross_margin'], row['gross_income'], row['rating']
        ))
        inseridos += 1
    except Exception as e:
        print(f"Erro na linha {inseridos+1}: {e}")
        erros += 1

conn.commit()
cursor.close()
conn.close()
print(f"\n✅ {inseridos} registros importados!")
print(f"❌ {erros} erros")