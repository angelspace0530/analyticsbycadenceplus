USE [KoraStarter];
GO
-- Kora free starter. Your working query file.
-- Start by inspecting the tables, then write your own answers.
SELECT TOP (10) * FROM kora.orders;
SELECT TOP (10) * FROM kora.order_lines;
SELECT TOP (10) * FROM kora.deliveries;

-- Project 1: Summarise orders placed by month.
-- Next: separate cancelled order value from non-cancelled order value.
-- Next: calculate cancellation rate at order grain.
-- Next: compare categories and calculate a weighted discount rate.

-- Project 2: Count delivered, failed and unresolved consignments separately.
-- Next: calculate on-time rate among Delivered consignments.
-- Next: find unresolved promises that were overdue at 2025-12-31.
-- Before joining order_lines to deliveries, aggregate each to order grain.
