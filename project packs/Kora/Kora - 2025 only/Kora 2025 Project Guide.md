<!-- Editable GitHub source for Kora 2025 Project Guide.md. Edit using GitHub's pencil icon. -->

# Kora free starter project pack

CadencePlus Solutions™ · Version 1.0 · 27 October 2026 Kora Workplace Supply Ltd is a fictional Nigerian supplier. This pack contains seven related tables, 29,066 records and two project briefs, it is free to use for learning. In this pack you will:

-  Load a local database (see Database Setup Guide for details).
- Load a local database (see Database Setup Guide for details).
- Investigate two business questions.
- Explain what the evidence supports.
## Understand the data

Kora Workplace Supply Ltd supplies workplace technology, furniture and business supplies to fictional organisations in Nigeria. This free extract contains orders placed from 1 January to 31 December 2025, their order lines and associated consignments recorded through 31 December 2025. Values are NGN and order value excludes tax.

### Table Details

- regions: one row per geographic region.
- branches: one row per distribution centre.
- customers: one row per customer in the source snapshot, including customers with no 2025 orders.
- products: one row per product in the source snapshot.
- orders: one row per order placed in 2025.
- order_lines: one row per product line within an order. Repeated product IDs are expected.
- deliveries: one row per delivery consignment attached to a selected order. Several consignments can belong to one order.
### Join rules

Every table has an ID primary key. A foreign key links a child to its parent. Joins

- customers.customer_id to orders.customer_id;
- orders.order_id to order_lines.order_id;
- products.product_id to order_lines.product_id;
- orders.order_id to deliveries.order_id;
- Join branches on branch_id.
*Customer region and branch region may differ.*
Joining orders to order_lines repeats each order for every line, COUNT(*) then counts lines, not orders. Joining order_lines and deliveries directly repeats both sets of measures. For a combined order summary, aggregate lines and deliveries independently to one row per order before joining.

### What is deliberately outside the starter pack

Invoices, returns, payments, costs of goods, inventory quantities, delivery-line quantities, HR and finance ledgers are not included. You can investigate order demand and delivery service; you cannot calculate recognized revenue, gross profit, cash collection, order-fill quantity or a full company financial statement from this extract. No anomalies have been added.

### Database Schema

![Kora database schema diagram](Kora%202025%20Database%20Schema.png)

## Project 1: Sales demand and cancellations

### The decision

Kora's Commercial Manager wants to know where the next quarter's account management attention should go. Orders are arriving, but how much demand survives cancellation, and where are discounts highest? Recommend two priorities supported by evidence.

### Your data

Use orders, order_lines, products and customers. You may add branches and regions when useful. The extract includes orders placed in 2025 and their related deliveries through 31 December 2025. Customer and product tables are snapshot reference lists, including customers with no orders in this extract.

### Questions to answer

1. How many orders were placed each month? Show all order value, cancelled order value and non- cancelled order value separately.
2. Which three product categories have the highest non-cancelled order value? Does that ranking change when using units requested? Explain why categories with different units may not be directly comparable by unit count.
3. Which branches have the highest cancellation rate?
*counts may tell a different story and rate can be misleading.*
4. What is the weighted discount rate for each category on non-cancelled orders?
*averaging line percentages can be misleading, you can try to explain why.*
5. Distinguish customer location from the fulfilling branch and does this impact the business in any way?
*some customers do not have orders in 2025*
6. Recommend at least two actions, you may attempt to call out the limitations of the dataset (what can you not establish?), if there is additional data that you would request to help with your analysis, you can name then in your report.
### Main measures

- All order value = sum of net_order_value_ngn across all order statuses, including cancelled orders.
- Non-cancelled order value = the same amount excluding orders with status Cancelled. Includes Delivered, partially delivered and Pending orders. This is not invoiced sales, recognized revenue, cash or profit.
- Cancelled order value = value attached to orders with status Cancelled at the snapshot.
- Cancellation rate = cancelled orders divided by all orders placed. Count at order level or use distinct order IDs after joining lines.
- Weighted discount rate = total discount_value_ngn divided by total gross_order_value_ngn, on the same population. Multiply by 100 to display a percentage.
- Average non-cancelled order value = non-cancelled order value divided by the number of distinct non- cancelled orders. Do not divide by line count.
### Expected deliverables

- One SQL file containing your queries, readable aliases and comments explaining important lines.
- One report page in a BI tool of your choice (Excel, Google Sheets, any tool you can use for visualization and reporting is acceptable) with no more than five visuals and clear labelling.
- One report page explaining at least two recommendations, supporting numbers, limitations and proposed follow-up measures.
- One Report Page explaining your methodology (include quality checks and all assumptions too if you have any).
### Optional Work

- Compare weighted discount rates between channels, accounting for category mix and try to propose a policy around this.
- Create a reusable monthly summary SQL view and walk us through it.
## Project 2 Delivery reliability

### The decision

Kora's Operations Manager needs an investigation shortlist. Which branches or carriers deserve attention, and what evidence should be collected before changing service arrangements? Assess delivery reliability for consignments attached to 2025 orders.

### Your data

Start with deliveries and branches. Remember one delivery row is one consignment, not one order! An order can also have several consignments. The snapshot was taken on 31 December 2025.

### Questions to answer

1. Analyze Delivered, Failed, In transit and Scheduled consignments. The idea is to keep failed and unresolved work visible.
2. Calculate on-time delivery rate among Delivered consignments, overall and by branch, carrier and any other dimension you deem important.
3. Among unresolved consignments, which were already overdue before the data snapshot was taken?
*separating promises before, on and after 31 December 2025 may help here*
4. Compare recorded shipping cost by branch and status. Explain why total cost and cost per delivered consignment answer different questions. **The cost of delivery on failed consignments is not reimbursed
5. Find the ten latest Delivered consignments by “days late”. For SQLite use julianday(delivered_date)- julianday(promised_delivery_date); for SQL Server use DATEDIFF(day,promised_delivery_date,delivered_date).
6. Recommend two investigation priorities. Please consider the sample size, customer/product mix and unresolved work before blaming a carrier or branch.
### Measures

- Delivered consignments = rows with status Delivered.
- On-time delivered consignments = Delivered rows with delivered_date on or before promised_delivery_date.
- On-time delivery rate = on-time delivered consignments divided by Delivered consignments. **Failed, In transit and Scheduled are not in this denominator but you can report them alongside.
- Unresolved consignments = In transit + Scheduled. **Failed consignments are a separate status.
- Overdue before cutoff = unresolved consignments with promise date before 2025-12-31.
- Total recorded shipping cost = sum shipping_cost_ngn across the stated population, including failures. **Making an inference about unrecorded future cost for unresolved or failed deliveries is not supported.
- Consignment delay = delivered date minus promise date for delivered consignment, snapshot date minus promise date for unresolved consignment.
### Expected deliverables

- One SQL file containing your queries, readable aliases and comments explaining important lines.
- One report page in a BI tool of your choice (Excel, Google Sheets, any tool you can use for visualization and reporting is acceptable) with no more than five visuals and clear labelling.
- One report page explaining at least two recommendations, supporting numbers, limitations and proposed follow-up measures.
- One Report Page explaining your methodology (include quality checks and all assumptions too if you have any).
### Optional extensions

- Produce an order-level table of consignment counts and recorded shipping cost using a CTE or a subquery.
- Join order value and delivery cost after independently aggregating both tables to one row per order. Demonstrate how joining the raw child tables can inflate your totals.
## Files and control totals

Table Expected rows regions 6 branches 6 customers 1,100 products 54 orders 6,001 order_lines 15,491 deliveries 6,408 All-order net value is 17,713,266,033.00 NGN. This includes cancelled orders. It is an import control, not recognized revenue.

### Reuse and credit

You may analyse, modify and publish your SQL, dashboards and findings using this free training dataset with credit to CadencePlus Solutions™️. Keep the fictional and synthetic labels. Do not present its values as real customer, employee or market data. Third-party software has its own licences. This starter extract is separate from the paid Jathan Project Pack.
