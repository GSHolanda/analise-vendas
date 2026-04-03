# Dashboard de Análise de Vendas

Uma aplicação web que conecta Python, Flask, MySQL e JavaScript para transformar dados brutos de vendas em insights visuais. Construída do zero como projeto prático de análise de dados.

---

## O que esse projeto faz

Você acessa o dashboard no navegador e vê, em tempo real, três perguntas de negócio respondidas com dados:

- **Qual linha de produto gera mais receita?** Alimentos e Bebidas lidera com R$ 282 mil — 37% a mais que Eletrônicos, o último colocado
- **Qual filial performa melhor?** Brasília com 357 vendas, contra 303 do Rio de Janeiro
- **Quando as pessoas mais compram?** O pico é às 11h, com uma queda de 23% às 17h — horário ideal para promoções

Não é um CRUD. É uma ferramenta que responde perguntas reais de gestão.

---

## Stack

| Camada | Tecnologia |
|---|---|
| Back-end | Python 3 + Flask |
| Banco de dados | MySQL |
| Manipulação de dados | Pandas |
| Visualizações estáticas | Matplotlib |
| Front-end | HTML5 + CSS3 + JavaScript |
| Gráficos interativos | Chart.js |

---

## Como rodar localmente

**Pré-requisitos:** Python 3, MySQL instalado e rodando

**1. Clone o repositório**
```bash
git clone https://github.com/SEU_USUARIO/analise-vendas.git
cd analise-vendas
```

**2. Instale as dependências**
```bash
pip install pandas matplotlib mysql-connector-python flask
```

**3. Configure o banco**

Crie o banco e a tabela no MySQL:
```sql
CREATE DATABASE vendas_db;
USE vendas_db;
```
Depois rode o script de criação da tabela em `importar.py` (as instruções estão nos comentários do arquivo).

**4. Importe os dados**
```bash
python importar.py
```
Saída esperada: `✅ 1000 registros importados!`

**5. Suba o dashboard**
```bash
cd dashboard
python app.py
```

Acessa **http://localhost:5000** e o dashboard já aparece com os dados.

---

## Estrutura do projeto

```
analise-vendas/
├── importar.py              # lê o CSV e popula o MySQL
├── analise.py               # análises com pandas + gráficos matplotlib
├── vendas.csv               # dataset com 1000 registros de vendas
├── grafico1_produtos.png    # receita por linha de produto
├── grafico2_filiais.png     # desempenho por filial
├── grafico3_horarios.png    # volume por hora do dia
└── dashboard/
    ├── app.py               # API Flask com 2 rotas
    ├── templates/
    │   └── index.html       # front-end com Chart.js
    └── static/
        └── style.css        # layout e estilo
```

---

## Como a API funciona

O Flask expõe uma rota `/api/dados` que consulta o MySQL e retorna um JSON com tudo que o front precisa:

```json
{
  "total_vendas": 1000,
  "receita_total": 1497616.76,
  "avaliacao_media": 7.1,
  "por_produto": [...],
  "por_filial": [...],
  "por_hora": [...]
}
```

O JavaScript faz um `fetch()` nessa rota e monta os gráficos dinamicamente, sem precisar recarregar a página.

---

## Aprendizados

Esse projeto surgiu como forma de praticar a integração entre as tecnologias que estou estudando. A parte mais interessante foi perceber que a mesma pergunta pode ser respondida de formas diferentes dependendo de como você escreve a query SQL — e que a visualização certa muda completamente a interpretação do dado.

Ainda pretendo adicionar filtros por filial e por período diretamente no dashboard, sem precisar alterar o código.

---

## Autor

**Gabriel Silva Holanda**
Estudante de Análise e Desenvolvimento de Sistemas — Cruzeiro do Sul (4º semestre)
Desenvolvedor Full Stack em formação — EBAC

holandadev2@gmail.com
