# Kora - 2025 only | PostgreSQL and MySQL setup

CadencePlus Solutions™ | Synthetic practice data | Nigerian naira (NGN)

These loaders contain all seven Kora tables and all 29,066 records. They are **self-contained SQL**: you do not have to import CSV files or edit local file paths. Existing SQL Server and SQLite versions are unchanged.

## PostgreSQL (pgAdmin or psql)

1. Create a fresh empty database named `kora_starter` in pgAdmin. Alternatively, from a terminal run `createdb kora_starter` if PostgreSQL client tools are configured.
2. Connect to **kora_starter** in pgAdmin Query Tool.
3. Open `Database/PostgreSQL/01_Load_Kora_Starter.sql` and execute the whole script. In psql: `psql -d kora_starter -v ON_ERROR_STOP=1 -f 01_Load_Kora_Starter.sql`.
4. Run `Database/PostgreSQL/02_Check_Load.sql` in the same database. It sets `search_path` to `kora`.
5. Your seven tables live in the **kora schema**, for example `SELECT * FROM kora.orders LIMIT 10;`. Set the query's search path or qualify table names.

**Important:** the loader replaces tables in the `kora` schema if they already exist. Use a dedicated learning database; do not run in a production database. PostgreSQL setup is transactional.

## MySQL (MySQL Workbench or mysql command line)

1. Start a local MySQL server and connect with an account allowed to create databases/tables.
2. Open `Database/MySQL/01_Load_Kora_Starter.sql` in MySQL Workbench and execute the **entire** file. From a terminal: `mysql -u YOUR_USER -p < 01_Load_Kora_Starter.sql`.
3. Run `Database/MySQL/02_Check_Load.sql`. Both scripts select database `kora_starter`.
4. Example: `SELECT * FROM kora_starter.orders LIMIT 10;`.

**Important:** the loader recreates Kora tables on rerun and will overwrite previous work in those tables. MySQL DDL is not transactional; if loading fails, correct the error and run the whole script again in a dedicated practice database.

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

All eight foreign-key relationship checks must return **zero** missing parents. Order dates run from **2025-01-01** to **2025-12-31**. Financial controls, in NGN:

- Gross order value: 21,021,553,238.50
- Discount value: 3,308,287,205.50
- Net order value: 17,713,266,033.00

Use the included `Reference/Load_Control_Totals.json` for the published control figures.

### Notes

- The scripts use `DECIMAL(18,2)` for financial values to avoid floating-point rounding.
- Optional fields are genuine SQL `NULL` values, not blank text.
- IDs are source keys, not auto-generated integers.
- Load statements contain all data so each script is roughly 2.7 MB. Your SQL editor may take time to open/run such a file.
- These new files are available individually in the GitHub repository branch. The existing published ZIP and PDF have **not yet been rebuilt**. Do not assume the downloadable ZIP includes the new engines.
- These scripts were derived and checked against the seven published CSV files. Full execution against live PostgreSQL and MySQL instances remains to be tested before a release announcement.
