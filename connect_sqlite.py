import sqlite3
import pandas as pd

# Connects to an existing database file in the current directory
# If the file does not exist, it creates it in the current directory
db_connect = sqlite3.connect('test.db')

# Instantiate cursor object for executing queries
cursor = db_connect.cursor()

# String variable for passing queries to cursor

#Department table

query = """
    CREATE TABLE Department(
    DName VARCHAR(100) CHECK(DName LIKE'Department%'),
    CName VARCHAR(100),
    FNmuber INT,
    PRIMARY KEY(DName)
    );
    """
    
# Execute query, the result is stored in cursor
cursor.execute(query)


#Student table
query = """
    CREATE TABLE Student(
    Student_id INT,
    SName VARCHAR(100),
    SInitial VARCHAR(100) NOT NULL,
    PRIMARY KEY(Student_id)
    );
    """
    
cursor.execute(query)


#Major table
query = """
    CREATE TABLE Major(
    MName VARCHAR(100),
    MCode VARCHAR(100) CHECK(LENGTH(MCode) = 3),
    DName VARCHAR(100),
    PRIMARY KEY(MName),
    FOREIGN KEY(DName) REFERENCES Department(DName) ON UPDATE CASCADE
    );
    """
    
cursor.execute(query)

#Event table
query = """
    CREATE TABLE Event(
    EName VARCHAR(100),
    SDate DATE,
    EDate DATE CHECK(EDate > SDate),
    PRIMARY KEY(EName)
    );
    """
    
cursor.execute(query)

#StudentMajor table
query = """
    CREATE TABLE StudentMajor(
    Student_id INT,
    MName VARCHAR(100),
    PRIMARY KEY(Student_id, MName),
    FOREIGN KEY(Student_id) REFERENCES Student(Student_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(MName) REFERENCES Major(MName) ON UPDATE CASCADE ON DELETE CASCADE
    );
    """
    
cursor.execute(query)

#StudentEvent table
query = """
    CREATE TABLE StudentEvent(
    Student_id INT,
    EName VARCHAR(100),
    PRIMARY KEY(Student_id, EName),
    FOREIGN KEY(Student_id) REFERENCES Student(Student_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(EName) REFERENCES Event(EName) ON UPDATE CASCADE ON DELETE CASCADE
    );
    """
    
cursor.execute(query)

#DepartEvent table
query = """
    CREATE TABLE DepartEvent(
    DName VARCHAR(100),
    EName VARCHAR(100),
    PRIMARY KEY(DName, EName),
    FOREIGN KEY(DName) REFERENCES Department(DName) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY(EName) REFERENCES Event(EName) ON UPDATE CASCADE ON DELETE CASCADE
    );
    """
    
cursor.execute(query)

#StudentEvent table

# Insert row into table

# Insert row into Department
query = """
    INSERT INTO Department
    VALUES ("Department phy", "c1", 10);
    """
cursor.execute(query)

query = """
    INSERT INTO Department
    VALUES ("Department bio", "c2", 12);
    """
    
cursor.execute(query)

query = """
    INSERT INTO Department
    VALUES ("Department csc", "c3", 14);
    """
cursor.execute(query)

query = """
    INSERT INTO Department
    VALUES ("Department eco", "c4", 16);
    """
cursor.execute(query)

query = """
    INSERT INTO Department
    VALUES ("Department art", "c5", 18);
    """
cursor.execute(query)

# Insert row into Student
query = """
    INSERT INTO Student
    VALUES (1, "A", "A");
    """
cursor.execute(query)

query = """
    INSERT INTO Student
    VALUES (2, "B", "B");
    """
cursor.execute(query)

query = """
    INSERT INTO Student
    VALUES (3, "C", "C");
    """
cursor.execute(query)

query = """
    INSERT INTO Student
    VALUES (4, "D", "D");
    """
cursor.execute(query)

query = """
    INSERT INTO Student
    VALUES (5, "E", "E");
    """
cursor.execute(query)

# Insert row into Major
query = """
    INSERT INTO Major
    VALUES ("Physics", "PHY", "Department phy");
    """
cursor.execute(query)

query = """
    INSERT INTO Major
    VALUES ("Biology", "BIO", "Department bio");
    """
cursor.execute(query)

query = """
    INSERT INTO Major
    VALUES ("Economy", "ECO", "Department eco");
    """
cursor.execute(query)

query = """
    INSERT INTO Major
    VALUES ("ComputerSience", "CSC", "Department csc");
    """
cursor.execute(query)

query = """
    INSERT INTO Major
    VALUES ("Art", "ART", "Department art");
    """
cursor.execute(query)

# Insert row into Event
query = """
    INSERT INTO Event
    VALUES ("E1", "2000-01-01", "2000-01-02");
    """
cursor.execute(query)

query = """
    INSERT INTO Event
    VALUES ("E2", "2001-01-01", "2001-01-02");
    """
cursor.execute(query)

query = """
    INSERT INTO Event
    VALUES ("E3", "2002-01-01", "2002-01-02");
    """
cursor.execute(query)

query = """
    INSERT INTO Event
    VALUES ("E4", "2003-01-01", "2003-01-02");
    """
cursor.execute(query)

query = """
    INSERT INTO Event
    VALUES ("E5", "2004-01-01", "2004-01-02");
    """
cursor.execute(query)

# Insert row into StudentMajor
query = """
    INSERT INTO StudentMajor
    VALUES (1,"Physics");
    """
cursor.execute(query)

query = """
    INSERT INTO StudentMajor
    VALUES (2,"Biology");
    """
cursor.execute(query)

query = """
    INSERT INTO StudentMajor
    VALUES (3,"Economy");
    """
cursor.execute(query)

query = """
    INSERT INTO StudentMajor
    VALUES (4,"ComputerSience");
    """
cursor.execute(query)

query = """
    INSERT INTO StudentMajor
    VALUES (5,"Art");
    """
cursor.execute(query)

# Insert row into StudentEvent
query = """
    INSERT INTO StudentEvent
    VALUES (1,"E1");
    """
cursor.execute(query)

query = """
    INSERT INTO StudentEvent
    VALUES (2,"E2");
    """
cursor.execute(query)

query = """
    INSERT INTO StudentEvent
    VALUES (3,"E3");
    """
cursor.execute(query)

query = """
    INSERT INTO StudentEvent
    VALUES (4,"E4");
    """
cursor.execute(query)

query = """
    INSERT INTO StudentEvent
    VALUES (5,"E5");
    """
cursor.execute(query)

#Insert row into DepartEvent
query = """
    INSERT INTO DepartEvent
    VALUES ("Department phy","E1");
    """
cursor.execute(query)

query = """
    INSERT INTO DepartEvent
    VALUES ("Department bio","E2");
    """
cursor.execute(query)

query = """
    INSERT INTO DepartEvent
    VALUES ("Department csc","E3");
    """
cursor.execute(query)

query = """
    INSERT INTO DepartEvent
    VALUES ("Department eco","E4");
    """
cursor.execute(query)

query = """
    INSERT INTO DepartEvent
    VALUES ("Department art","E5");
    """
cursor.execute(query)




# Select data
#print Department table
query = """
    SELECT *
    FROM Department
    """
cursor.execute(query)


# Extract column names from cursor
column_names = [row[0] for row in cursor.description]

# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)

# Examine dataframe
print(df)
print(df.columns)

#print Student table
query = """
    SELECT *
    FROM Student
    """
cursor.execute(query)

column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)
print(df)
print(df.columns)

#print Major table
query = """
    SELECT *
    FROM Major
    """
cursor.execute(query)

column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)
print(df)
print(df.columns)

#print Event table
query = """
    SELECT *
    FROM Event
    """
cursor.execute(query)

column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)
print(df)
print(df.columns)

#print StudentMajor table
query = """
    SELECT *
    FROM StudentMajor
    """
cursor.execute(query)

column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)
print(df)
print(df.columns)

#print StudentEvent table
query = """
    SELECT *
    FROM StudentEvent
    """
cursor.execute(query)

column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)
print(df)
print(df.columns)

query = """
    SELECT *
    FROM DepartEvent
    """
cursor.execute(query)

column_names = [row[0] for row in cursor.description]
table_data = cursor.fetchall()
df = pd.DataFrame(table_data, columns=column_names)
print(df)
print(df.columns)


# Commit any changes to the database
db_connect.commit()

# Close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db_connect.close()
