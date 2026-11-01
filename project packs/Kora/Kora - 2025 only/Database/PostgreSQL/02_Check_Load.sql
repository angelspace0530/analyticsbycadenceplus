SET search_path TO kora, public;
-- Expected counts: 6,6,1100,54,6001,15491,6408.
SELECT 'regions' AS table_name, COUNT(*) AS row_count FROM regions
UNION ALL
SELECT 'branches' AS table_name, COUNT(*) AS row_count FROM branches
UNION ALL
SELECT 'customers' AS table_name, COUNT(*) AS row_count FROM customers
UNION ALL
SELECT 'products' AS table_name, COUNT(*) AS row_count FROM products
UNION ALL
SELECT 'orders' AS table_name, COUNT(*) AS row_count FROM orders
UNION ALL
SELECT 'order_lines' AS table_name, COUNT(*) AS row_count FROM order_lines
UNION ALL
SELECT 'deliveries' AS table_name, COUNT(*) AS row_count FROM deliveries;
-- Missing-parent counts should all be zero.
SELECT 'branches.region_id' AS relationship, COUNT(*) AS missing_parent_rows FROM branches c LEFT JOIN regions p ON c.region_id=p.region_id WHERE p.region_id IS NULL
UNION ALL
SELECT 'customers.region_id' AS relationship, COUNT(*) AS missing_parent_rows FROM customers c LEFT JOIN regions p ON c.region_id=p.region_id WHERE p.region_id IS NULL
UNION ALL
SELECT 'orders.customer_id' AS relationship, COUNT(*) AS missing_parent_rows FROM orders c LEFT JOIN customers p ON c.customer_id=p.customer_id WHERE p.customer_id IS NULL
UNION ALL
SELECT 'orders.branch_id' AS relationship, COUNT(*) AS missing_parent_rows FROM orders c LEFT JOIN branches p ON c.branch_id=p.branch_id WHERE p.branch_id IS NULL
UNION ALL
SELECT 'order_lines.order_id' AS relationship, COUNT(*) AS missing_parent_rows FROM order_lines c LEFT JOIN orders p ON c.order_id=p.order_id WHERE p.order_id IS NULL
UNION ALL
SELECT 'order_lines.product_id' AS relationship, COUNT(*) AS missing_parent_rows FROM order_lines c LEFT JOIN products p ON c.product_id=p.product_id WHERE p.product_id IS NULL
UNION ALL
SELECT 'deliveries.order_id' AS relationship, COUNT(*) AS missing_parent_rows FROM deliveries c LEFT JOIN orders p ON c.order_id=p.order_id WHERE p.order_id IS NULL
UNION ALL
SELECT 'deliveries.branch_id' AS relationship, COUNT(*) AS missing_parent_rows FROM deliveries c LEFT JOIN branches p ON c.branch_id=p.branch_id WHERE p.branch_id IS NULL;
-- Expected date range: 2025-01-01 to 2025-12-31.
SELECT MIN(order_date) AS first_order, MAX(order_date) AS last_order FROM orders;
-- Expected NGN totals: 21021553238.50 / 3308287205.50 / 17713266033.00.
SELECT ROUND(SUM(gross_order_value_ngn),2) AS gross_order_value_ngn, ROUND(SUM(discount_value_ngn),2) AS discount_value_ngn, ROUND(SUM(net_order_value_ngn),2) AS net_order_value_ngn FROM order_lines;
