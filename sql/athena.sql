-- Exemplo para uma tabela orders previamente catalogada no Athena.
SELECT product_id,
       COUNT(*) AS total_pedidos,
       SUM(quantity * unit_price) AS faturamento
FROM orders
GROUP BY product_id
ORDER BY faturamento DESC;
