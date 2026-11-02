<!-- Editable GitHub source for Kora 2025 Database Setup Guide.md. Edit using GitHub's pencil icon. -->

# Kora database setup

5
+		**SQLite · SQL Server · PostgreSQL · MySQL**

## Load Kora into a local database

### Start with the extracted folder

Download the learner ZIP and extract it. On Windows choose Extract All; on Mac open the ZIP to extract it. Read the [Kora 2025 Project Guide](Kora%202025%20Project%20Guide.md) for the dataset and project requirements. Keep your own queries and reports in a separate working folder.

**Choose a database engine and follow the applicable instructions.**

### Route A SQLite on Mac or Windows

If you already have SQLite on your windows, you can skip to number 2 If you are already comfortable loading databases? Open Database/SQLite/Kora_Starter.sqlite directly. It contains the same data but skips the import lesson.

1. Install DB Browser for SQLite from https://sqlitebrowser.org/dl/ and open the application. Choose the download for your operating system. SQLite runs locally; it does not require a separate database server or login.
2. Start with no database open. Choose File > Import > Database from SQL file.
3. Select Database/SQLite/01_Load_Kora_Starter.sql from the extracted pack. If asked whether to create a new database, choose Yes.
4. Save the new database in your working folder as My_Kora_Starter.sqlite. Use a new filename rather than the supplied preloaded copy.
5. Wait for the import to finish. If prompted to save, confirm; use Write Changes if enabled. The seven tables should appear under Database Structure.
6. In Execute SQL, run SELECT COUNT(*) AS orders_loaded FROM orders; using the execute button. Expect 6001.
7. Open Database/SQLite/02_Check_Load.sql in the SQL editor and run its statements. Compare counts to the table below. integrity_check should return ok; foreign_key_check should return no problem rows.
8. Close the application, reopen My_Kora_Starter.sqlite and repeat the count to confirm the file was saved. Now start Project 1. Already comfortable loading databases? Open Database/SQLite/Kora_Starter.sqlite directly. It contains the same data but skips the import lesson.

### Route B SQL Server on Windows

If you already have SQL Server on your windows, you can skip to number 3

1. Install the free SQL Server Express database engine from https://www.microsoft.com/en-us/sql-server/sql-server-downloads and keep the instance name shown by setup. Basic installation is suitable for a local learning instance. Use Windows Authentication for this route.
2. Install SQL Server Management Studio from https://learn.microsoft.com/en-us/ssms/install/install . SSMS is the interface you will use to interact with your local database engine.
3. Open SSMS and connect to the local Database Engine using Windows Authentication and the instance name from setup. A named instance commonly looks like localhost\SQLEXPRESS; a default instance can use localhost. Use your actual instance name.
4. Open Database/SQL_Server/00_Create_Database.sql with File > Open > File. Run the whole file with Execute. Expect current_database = KoraStarter.
5. Open Database/SQL_Server/01_Load_Kora_Starter.sql and execute the whole file with no text selected. It creates the kora schema, all tables, relationships and data in KoraStarter. Expect Kora starter loaded successfully. It will stop if the kora schema already exists.
6. Run Database/SQL_Server/02_Check_Load.sql. Compare the results with the controls. Refresh Object Explorer > Databases > KoraStarter > Tables.
7. Open a new query connected to KoraStarter and run SELECT COUNT(*) AS orders_loaded FROM kora.orders; Expect 6001.

### Route C PostgreSQL

Windows or Mac. Use PostgreSQL and pgAdmin to create and query your local Kora database. You only need one database engine for this pack.

### Install and connect

1. Install PostgreSQL from https://www.postgresql.org/download/. Include pgAdmin if it is offered by your installer. Set a local administrator password and keep it safe.
2. Open pgAdmin, connect to your local server and create an empty database named kora_starter. Open Query Tool while connected to kora_starter, not the default postgres maintenance database.

### Load the data

3. Open Database/PostgreSQL/01_Load_Kora_Starter.sql in Query Tool. Execute the entire script without selecting just one statement. It creates the kora schema and the seven related tables and inserts all records.
4. Open and run Database/PostgreSQL/02_Check_Load.sql in kora_starter. It sets your session search path to kora, public and checks the load. Every missing-parent count should be zero.

### Your first query

Run: SET search_path TO kora, public; then SELECT * FROM orders LIMIT 10; Alternatively, use the fully qualified name kora.orders. A new connection may need the search path set again.

### If something fails

Check that Query Tool is connected to kora_starter. Do not paste MySQL or SQL Server scripts into PostgreSQL. Re-running the PostgreSQL script replaces the existing Kora practice tables, so keep your own work in separate query files.

### Route D MySQL

Windows or Mac. Use MySQL Server and MySQL Workbench to work with the same seven Kora tables. This setup does not require cloud accounts.

### Install and connect

1. Install MySQL Server and MySQL Workbench from https://dev.mysql.com/downloads/. The database server and the Workbench interface are separate components. Keep your local login details safe.
2. Start the MySQL server. Open MySQL Workbench and connect to it using an account permitted to create databases and tables.

### Load the data

3. Open Database/MySQL/01_Load_Kora_Starter.sql in MySQL Workbench. Execute the entire SQL script. It creates and selects kora_starter, creates the seven tables and inserts the data.
4. Open Database/MySQL/02_Check_Load.sql and execute it. It starts with USE kora_starter; and verifies record counts, relationships, dates and money totals.

### Your first query

Run: USE kora_starter; then SELECT * FROM orders LIMIT 10; You can also query kora_starter.orders without relying on the selected database.

### If something fails

Check that MySQL Server is running and that the Workbench connection uses the expected account. The loader recreates its Kora tables if run again. Do not mix syntax from other engines.

### What a successful load looks like

- All seven tables exist.
- Orders has 6001 rows.
- Order dates range from 2025-01-01 to 2025-12-31.
- Sum net_order_value_ngn is 17713266033.00 NGN across all order statuses.
- Detailed controls are in Reference/Load_Control_Totals.json.

### First query

SQLite: SELECT * FROM orders LIMIT 10; SQL Server: SELECT TOP (10) * FROM kora.orders; These show up to ten rows. Without ORDER BY, SQL does not promise which ten rows appear or their order. Add ORDER BY order_date, order_id for a repeatable display.

### Common problems

- Tables already exist or the kora schema exists: the data may already be loaded. Run the count checks. For a new SQLite import, start a separate new file; do not import over the supplied database. For SQL Server, keep the loaded copy and use it rather than re-running the loader. No reset or deletion script is included.
- SQL Server cannot find the server: confirm the engine is installed and running and use the actual local instance name. SSMS alone is not the engine.
- A local SQL Server certificate is not trusted: confirm the host is your own local learning instance. SSMS has a Trust Server Certificate option for that local connection. Use validated certificates for remote services.
- GO or kora.orders causes an error in SQLite: that is the SQL Server file. Switch to the SQLite folder. SQLite tables here have no kora prefix.
- LIMIT causes an error in SQL Server: use the supplied SQL Server query file, which uses TOP. Do not mix the routes.
- A blank CSV date becomes 0 in a spreadsheet: blank means missing or not yet applicable, not a date of zero. The SQL loader preserves SQL NULL.
- SQLite says database is locked: close other tools using that same file, save or discard pending edits deliberately, and retry the read query.
- Counts differ: confirm you used this starter extract rather than the original 45-table simulation and did not filter the Browse Data view. Run COUNT(*) in SQL.

### Use the data in Power BI or Excel

The CSV files can be imported directly for reporting. Keep IDs as text, parse dates as ISO year-month-day, and set NGN values to decimal numbers using a locale that recognises the decimal point. Do not append the CSVs to the database after loading the SQL file; that would try to load the data twice. In Power BI, avoid blindly activating both Regions > Customers > Orders and Regions > Branches > Orders filter paths. Customer geography and branch geography represent different roles. Use separate role- playing region tables or one deliberate active path. Keep order_lines and deliveries as separate facts. Joining both raw tables on order_id duplicates values when an order has multiple lines and consignments. For a direct SQL Server connection, choose Get Data > SQL Server, enter your local instance and KoraStarter, and select the kora tables. SQLite does not use the SQL Server connector; use the CSV route for an accessible starter reporting workflow.

### What a successful load looks like

In your chosen database engine, run its 02_Check_Load.sql file. The expected rows are: regions 6; branches 6; customers 1,100; products 54; orders 6,001; order_lines 15,491; deliveries 6,408. Total: 29,066. The order date range is 2025-01-01 to 2025-12-31. The net order value (including cancelled orders) is 17,713,266,033.00 NGN. The definitive controls are in Reference/Load_Control_Totals.json.

### Keep the project files separate

Use your own copies of the starter query files in Projects/ to write answers and save your SQL. For project questions, table definitions, the schema diagram and expected submissions, open Kora 2025 Project Guide.md. Do not load the CSVs again after executing a self-contained SQL loader. That would duplicate data or create key errors. You can import the CSVs separately into Excel or Power BI instead.
