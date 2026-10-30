USE [KoraStarter];
GO
SELECT 'regions' AS table_name, COUNT(*) AS row_count FROM kora.regions
UNION ALL
SELECT 'branches' AS table_name, COUNT(*) AS row_count FROM kora.branches
UNION ALL
SELECT 'customers' AS table_name, COUNT(*) AS row_count FROM kora.customers
UNION ALL
SELECT 'products' AS table_name, COUNT(*) AS row_count FROM kora.products
UNION ALL
SELECT 'orders' AS table_name, COUNT(*) AS row_count FROM kora.orders
UNION ALL
SELECT 'order_lines' AS table_name, COUNT(*) AS row_count FROM kora.order_lines
UNION ALL
SELECT 'deliveries' AS table_name, COUNT(*) AS row_count FROM kora.deliveries;

-- If every relationship is intact, each missing-parent count is zero.
SELECT 'orders without customer' AS check_name, COUNT(*) AS problem_rows
FROM kora.orders o LEFT JOIN kora.customers c ON c.customer_id=o.customer_id
WHERE c.customer_id IS NULL
UNION ALL
SELECT 'lines without order', COUNT(*)
FROM kora.order_lines l LEFT JOIN kora.orders o ON o.order_id=l.order_id WHERE o.order_id IS NULL
UNION ALL
SELECT 'deliveries without order', COUNT(*)
FROM kora.deliveries d LEFT JOIN kora.orders o ON o.order_id=d.order_id WHERE o.order_id IS NULL;

SELECT MIN(order_date) AS first_order, MAX(order_date) AS last_order FROM kora.orders;
SELECT ROUND(SUM(gross_order_value_ngn),2) AS gross_order_value_ngn,
       ROUND(SUM(discount_value_ngn),2) AS discount_value_ngn,
       ROUND(SUM(net_order_value_ngn),2) AS all_order_value_ngn
FROM kora.order_lines;
