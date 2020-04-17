
--  creating tables in sql.......

-- Create Table --name_of_table (
--     column_name column_datatype optional constraint,
--     column_name column_datatype optional constraint,
--     .........
--     column_name column_datatype optional constraint,
--     CONSTRAINT  name_of_table_PK    primary key(column_name)
--     CONSTRAINT  name_of_table_FK    foreign key(column_name)
--     
-- );

USE demo;

CREATE TABLE Human (
	HumanId			Integer			NOT NULL,
    Name			Char(35)		NOT NULL,
    Color			Char(30)		NOT NULL,
    Sex				Char(10)		NULL,
    BloodGrup		Char(35)		NULL,
    CONSTRAINT		Human_PK			PRIMARY KEY(HumanId)

);

CREATE TABLE Games (
	OrderNumber		Integer			NOT NULL,
    StoreNumber		Integer			NOT NULL,
    StoreZIP		Char (9)		NULL,
    OrderMonth		Char (12)		NOT NULL,
    OrderYear		integer			NOT NULL,
    OrderTotal		Numeric(4,2)	NULL,
    HumanId			Integer			NOT NULL,
    CONSTRAINT		Games_PK		PRIMARY KEY(OrderNumber),
    CONSTRAINT		Games_FK		FOREIGN KEY(HumanId)
							REFERENCES Human(HumanId)
);