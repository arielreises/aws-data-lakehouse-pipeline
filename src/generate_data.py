"""Gera pedidos fictícios para testar o pipeline localmente."""
import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)
saida = Path(__file__).resolve().parents[1] / 'data' / 'orders.csv'
saida.parent.mkdir(exist_ok=True)
with saida.open('w', newline='', encoding='utf-8') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(['order_id', 'product_id', 'quantity', 'unit_price', 'order_date'])
    for i in range(1, 101):
        produto = random.choice(['P001', 'P002', 'P003'])
        writer.writerow([i, produto, random.randint(1, 5), {'P001': 19.9, 'P002': 49.9, 'P003': 89.9}[produto], (date(2026, 1, 1) + timedelta(days=i % 31)).isoformat()])
print(f'Arquivo criado: {saida}')
