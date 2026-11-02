# Kora - 2025 only | PostgreSQL and MySQL setup

CadencePlus Solutions™ | Synthetic practice data | Nigerian naira (NGN)


## PostgreSQL (pgAdmin or psql)

1. Create a fresh empty database named `kora_starter` in pgAdmin. Alternatively, from a terminal run `createdb kora_starter` if PostgreSQL client tools are configured.
2. Connect to **kora_starter** in pgAdmin Query Tool.
3. Open `Database/PostgreSQL/01_Load_Kora_Starter.sql` and execute the whole script. In psql: `psql -d kora_starter -v ON_ERROR_STOP=1 -f 01_Load_Kora_Starter.sql`.
4. Run `Database/PostgreSQL/02_Check_Load.sql` in the same database.


## MySQL (MySQL Workbench or mysql command line)

1. Start a local MySQL server and connect with an account allowed to create databases/tables.
2. Open `Database/MySQL/01_Load_Kora_Starter.sql` in MySQL Workbench and execute **OR** From a terminal: `mysql -u YOUR_USER -p < 01_Load_Kora_Starter.sql`.
3. Run `Database/MySQL/02_Check_Load.sql`. Both scripts select database `kora_starter`.


## How to check your result

| Table | Expected records |
| --- | ---: |
| regions | 6 |
| branches | 6 |
| customers | 1,100 |
| products | 54 |
| orders | 6,001 |
| order_lines | 15,491 |
| deliveries | 6,408 |
| **Total** | **29,066** |

All eight foreign-key relationship checks must return **zero** missing parents. Order dates run from **2025-01-01** to **2025-12-31**.

- Gross order value: 21,021,553,238.50
- Discount value: 3,308,287,205.50
- Net order value: 17,713,266,033.00

Use the included `Reference/Load_Control_Totals.json` for the published control figures.
