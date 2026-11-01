-- CadencePlus Solutions™ | Kora 2025 only | PostgreSQL / MySQL starter queries
-- PostgreSQL: run SET search_path TO kora, public; first.
-- MySQL: run USE kora_starter; first.
-- Select the appropriate statement below for your database:
-- PostgreSQL: SET search_path TO kora, public;
-- MySQL: USE kora_starter;

SELECT * FROM orders LIMIT 10;
SELECT * FROM order_lines LIMIT 10;
SELECT * FROM deliveries LIMIT 10;

-- Project 1: Summarise orders placed by month.
-- Next: separate cancelled order value from non-cancelled order value.
-- Next: calculate cancellation rate at order grain.
-- Next: compare categories and calculate a weighted discount rate.

-- Project 2: Count delivered, failed and unresolved consignments separately.
-- Next: calculate on-time rate among Delivered consignments.
-- Next: find unresolved promises overdue at 2025-12-31.
-- Before joining order_lines and deliveries, aggregate each to order grain.
