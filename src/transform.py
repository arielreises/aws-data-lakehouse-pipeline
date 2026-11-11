"""Valida pedidos e calcula o faturamento por produto."""
import csv
from collections import defaultdict
from pathlib import Path

pasta = Path(__file__).resolve().parents[1] / 'data'
resumo = defaultdict(lambda: {'orders': 0, 'revenue': 0.0})
with (pasta / 'orders.csv').open(encoding='utf-8', newline='') as arquivo:
    for pedido in csv.DictReader(arquivo):
        quantidade = int(pedido['quantity'])
        preco = float(pedido['unit_price'])
        if quantidade <= 0 or preco < 0:
            continue
        item = resumo[pedido['product_id']]
        item['orders'] += 1
        item['revenue'] += quantidade * preco

with (pasta / 'sales_by_product.csv').open('w', encoding='utf-8', newline='') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(['product_id', 'orders', 'revenue'])
    for produto, valores in sorted(resumo.items()):
        writer.writerow([produto, valores['orders'], f"{valores['revenue']:.2f}"])
print('Resumo gerado em data/sales_by_product.csv')
