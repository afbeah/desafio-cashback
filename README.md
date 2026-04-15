# 💰 Calculadora de Cashback

Projeto desenvolvido como desafio técnico com o objetivo de simular o cálculo de cashback para diferentes tipos de clientes, incluindo persistência de dados e visualização de histórico.

---

## 🚀 Funcionalidades

- Cálculo de cashback com base em:
  - Valor da compra
  - Percentual de desconto
  - Tipo de cliente (Comum ou VIP)

- Regras de negócio:
  - Cashback base: 5% sobre o valor final da compra
  - Cliente VIP: +10% sobre o cashback base
  - Compras acima de R$500: cashback dobrado

- Registro de histórico por IP
- Exibição do histórico no frontend

---

## 🧠 Regra de cálculo

1. Aplicar desconto na compra:
valor_final = valor_compra * (1 - desconto / 100)

2. Calcular cashback base:
cashback_base = valor_final * 0.05

3. Se for VIP:
+10% sobre o cashback_base

4. Se valor_final > 500:
cashback_total *= 2


---

## ⚠️ Observação importante

Dependendo do cenário, o cliente VIP pode receber menos cashback que o cliente comum.

Isso acontece porque o desconto aplicado ao VIP reduz o valor final da compra, podendo impedir que ele atinja a regra de cashback dobrado (> R$500).

Essa análise foi considerada durante o desenvolvimento como um possível ponto de melhoria na regra de negócio.

---

## 🛠️ Tecnologias utilizadas

### Backend
- Python
- Flask
- SQLite

### Frontend
- HTML
- JavaScript (Fetch API)

---

## 📁 Estrutura do projeto

desafio-cashback/
│
├── backend/
│ ├── app.py
│ └── database.db
│
├── frontend/
│ └── index.html
│
└── cashback.py


---

## ▶️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/afbeah/desafio-cashback.git
cd desafio-cashback 
```

### 2. Rodar o backend
```bash
cd backend
pip install flask flask-cors
python app.py
```

- Servidor disponível em: http://127.0.0.1:5000

### 3. Rodar o frontend
```bash
cd ../frontend
py -m http.server 5500
```

- Abrir no navegador: http://127.0.0.1:5500

## 📸 Exemplo de uso
Tipo: Comum
Valor: 600
Desconto: 10

Resultado: 
 - Cashback: R$ 54.00