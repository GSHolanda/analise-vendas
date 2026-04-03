import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',          
    database='vendas_db'
)
print("✅ Conectado ao banco!")

df = pd.read_sql("SELECT * FROM vendas", conn)
print(f"📊 {len(df)} registros carregados\n")



query1 = """
    SELECT product_line,
        COUNT(*) as total_vendas,
        ROUND(SUM(total), 2) as receita_total
    FROM vendas
    GROUP BY product_line
    ORDER BY receita_total DESC
"""
df1 = pd.read_sql(query1, conn)
print("--- Receita por Linha de Produto ---")
print(df1.to_string(index=False))

plt.figure(figsize=(10, 5))
plt.barh(df1['product_line'], df1['receita_total'], color='steelblue')
plt.title('Receita Total por Linha de Produto')
plt.xlabel('Receita (R$)')
plt.tight_layout()
plt.savefig('grafico1_produtos.png')
plt.show()
print("\n✅ Gráfico 1 salvo!\n")

query2 = """
    SELECT branch, city,
        COUNT(*) as total_vendas,
        ROUND(AVG(total), 2) as ticket_medio,
        ROUND(AVG(rating), 2) as avaliacao_media
    FROM vendas
    GROUP BY branch, city
    ORDER BY total_vendas DESC
"""
df2 = pd.read_sql(query2, conn)
print("--- Desempenho por Filial ---")
print(df2.to_string(index=False))

fig, ax = plt.subplots(figsize=(8, 4))
bars = ax.bar(df2['city'], df2['total_vendas'],
        color=['#2196F3', '#4CAF50', '#FF9800'])
ax.set_title('Total de Vendas por Filial')
ax.set_ylabel('Número de vendas')
for bar, val in zip(bars, df2['total_vendas']):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
            str(val), ha='center', fontsize=11, fontweight='bold')
plt.tight_layout()
plt.savefig('grafico2_filiais.png')
plt.show()
print("✅ Gráfico 2 salvo!\n")


query3 = """
    SELECT HOUR(time_venda) as hora,
        COUNT(*) as total_vendas
    FROM vendas
    GROUP BY hora
    ORDER BY hora
"""
df3 = pd.read_sql(query3, conn)
print("--- Vendas por Hora do Dia ---")
print(df3.to_string(index=False))

plt.figure(figsize=(12, 4))
plt.plot(df3['hora'], df3['total_vendas'],
        marker='o', color='purple', linewidth=2)
plt.fill_between(df3['hora'], df3['total_vendas'],
        alpha=0.2, color='purple')
plt.title('Vendas por Hora do Dia')
plt.xlabel('Hora')
plt.ylabel('Nº de vendas')
plt.xticks(df3['hora'])
plt.tight_layout()
plt.savefig('grafico3_horarios.png')
plt.show()
print("✅ Gráfico 3 salvo!\n")


conn.close()
print("🎉 Análise concluída! 3 gráficos salvos na pasta.")