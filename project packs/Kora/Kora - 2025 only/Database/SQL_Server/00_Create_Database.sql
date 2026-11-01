-- Local SQL Server only. Run the WHOLE file in SSMS.
USE [master];
GO
IF DB_ID(N'KoraStarter') IS NULL
    EXEC(N'CREATE DATABASE [KoraStarter]');
GO
USE [KoraStarter];
GO
SELECT DB_NAME() AS current_database;
