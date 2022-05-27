# file names
FOLDER_CSV = "csv"
FOLDER_DATABASE = "database"
FILE_DATABASE = "school.db"
FILE_CSV_PERSONS = "Persons_School_Python.csv"
FILE_CSV_COURSES = "Courses_School_Python.csv"
FILE_CSV_POSITIONS = "Positions_School_Python.csv"
TABLE_NAME_PERSONS = "persons"
TABLE_NAME_COURSES = "courses"
TABLE_NAME_POSITIONS = "positions"

# Colors
SET_INFO_MESSAGE_COLOR = "\u001b[48;5;2m"
SET_ERROR_MESSAGE_COLOR = "\u001b[48;5;1m"
SET_HEADER_COLOR = "\u001b[38;5;9m"
SET_HIGHLIGHT_TEXT_COLOR = "\u001b[38;5;11m"
RESET_COLOR = "\u001b[0m"

"""
0 - 8 - Basic colors
8 - 15 - intensive colors
0 - black
1, 9 - RED
2, 10 - green
3, 11 - Yellow
4, 12 - blue
5, 13 - magenta
6, 14 - cyan
7, 15 - White
"""

# Tables - headers
PERSONS_HEADERS = "person_id,first_name,last_name,email,address,tel,salary,login,password,position_id,course_id"
COURSES_HEADERS = "course_id,course_name,syllabus,description"
POSITIONS_HEADERS = "position_id,position_name,description"

# lambdas
get_fields_list =  lambda s: s.split(",") 
get_fields_string =  lambda s: "('" + "','".join(get_fields_list(s)[1:]) + "')"
get_values_string =  lambda s: "(" + ("?," * len(get_fields_list(s)[1:]))[:-1] + ")" 

# SQL queries
## Add record 
SQL_ADD_RECORD_PERSONS = F"""
INSERT INTO "{TABLE_NAME_PERSONS}" 
{get_fields_string(PERSONS_HEADERS)}
VALUES 
{get_values_string(PERSONS_HEADERS)};
"""

SQL_ADD_RECORD_COURSES = F"""
INSERT INTO "{TABLE_NAME_COURSES}" 
{get_fields_string(COURSES_HEADERS)}
VALUES 
{get_values_string(COURSES_HEADERS)};
"""

SQL_ADD_RECORD_POSITIONS = F"""
INSERT INTO "{TABLE_NAME_POSITIONS}" 
{get_fields_string(POSITIONS_HEADERS)}
VALUES 
{get_values_string(POSITIONS_HEADERS)};
"""

## Get user
SQL_GET_USER_BY_LOGIN = F"""
SELECT * FROM {TABLE_NAME_PERSONS} WHERE login = ? AND password = ?;
"""

## Check table
SQL_CHECK_TABLE_EXISTS = F"""
SELECT EXISTS (SELECT * FROM sqlite_schema WHERE type = 'table' AND name = ?);
"""

## Check administrators
SQL_CHECK_ADMINISTRATORS = F"""
SELECT EXISTS (SELECT * FROM {TABLE_NAME_PERSONS} WHERE {get_fields_list(PERSONS_HEADERS)[9]} = 5);
"""

## Create tables
SQL_CREATE_TABLE_PERSONS = F"""
CREATE TABLE IF NOT EXISTS "{TABLE_NAME_PERSONS}" (
	"{get_fields_list(PERSONS_HEADERS)[0]}"	INTEGER NOT NULL UNIQUE,
	"{get_fields_list(PERSONS_HEADERS)[1]}"	TEXT,
	"{get_fields_list(PERSONS_HEADERS)[2]}"	TEXT,
	"{get_fields_list(PERSONS_HEADERS)[3]}"	TEXT,
	"{get_fields_list(PERSONS_HEADERS)[4]}"	TEXT,
	"{get_fields_list(PERSONS_HEADERS)[5]}"	TEXT,
	"{get_fields_list(PERSONS_HEADERS)[6]}"	INTEGER,
	"{get_fields_list(PERSONS_HEADERS)[7]}"	TEXT UNIQUE,
	"{get_fields_list(PERSONS_HEADERS)[8]}"	TEXT,
	"{get_fields_list(PERSONS_HEADERS)[9]}"	INTEGER,
	"{get_fields_list(PERSONS_HEADERS)[10]}"	INTEGER,
	FOREIGN KEY("{get_fields_list(PERSONS_HEADERS)[9]}") REFERENCES "{TABLE_NAME_POSITIONS}"("{get_fields_list(POSITIONS_HEADERS)[0]}"),
	FOREIGN KEY("{get_fields_list(PERSONS_HEADERS)[10]}") REFERENCES "{TABLE_NAME_COURSES}"("{get_fields_list(COURSES_HEADERS)[0]}"),
	PRIMARY KEY("{get_fields_list(PERSONS_HEADERS)[0]}" AUTOINCREMENT)
);

"""
SQL_CREATE_TABLE_COURSES = F"""
CREATE TABLE  IF NOT EXISTS "{TABLE_NAME_COURSES}" (
	"{get_fields_list(COURSES_HEADERS)[0]}"	INTEGER NOT NULL UNIQUE,
	"{get_fields_list(COURSES_HEADERS)[1]}"	TEXT UNIQUE,
	"{get_fields_list(COURSES_HEADERS)[2]}"	TEXT,
	"{get_fields_list(COURSES_HEADERS)[3]}"	TEXT,
	PRIMARY KEY("{get_fields_list(COURSES_HEADERS)[0]}" AUTOINCREMENT)
);
"""
SQL_CREATE_TABLE_POSITIONS = F"""
CREATE TABLE IF NOT EXISTS "{TABLE_NAME_POSITIONS}" (
	"{get_fields_list(POSITIONS_HEADERS)[0]}"	INTEGER NOT NULL UNIQUE,
	"{get_fields_list(POSITIONS_HEADERS)[1]}"	TEXT UNIQUE,
	"{get_fields_list(POSITIONS_HEADERS)[2]}"	TEXT,
	PRIMARY KEY("{get_fields_list(POSITIONS_HEADERS)[0]}" AUTOINCREMENT)
);
"""

## Drop table
SQL_DROP_TABLE_PERSONS = F"""
DROP TABLE IF EXISTS "{TABLE_NAME_PERSONS}"
"""
SQL_DROP_TABLE_POSITIONS = F"""
DROP TABLE IF EXISTS "{TABLE_NAME_POSITIONS}"
"""
SQL_DROP_TABLE_COURSES = F"""
DROP TABLE IF EXISTS "{TABLE_NAME_COURSES}"
"""

## Get positions for add record menu
SQL_GET_POSITIONS = F"""
SELECT {get_fields_list(POSITIONS_HEADERS)[0]}, {get_fields_list(POSITIONS_HEADERS)[1]} FROM {TABLE_NAME_POSITIONS};
"""

SQL_GET_COURSES = F"""
SELECT {get_fields_list(COURSES_HEADERS)[0]}, {get_fields_list(COURSES_HEADERS)[1]} FROM {TABLE_NAME_COURSES};
"""

SQL_GET_LOGIN_NAMES = F"""
SELECT {get_fields_list(PERSONS_HEADERS)[7]} FROM {TABLE_NAME_PERSONS};
"""

SQL_UPDATE_TABLE_PERSONS = F"""
UPDATE "{TABLE_NAME_PERSONS}" SET "__FIELD_NAME_TO_CHANGE__" = ? WHERE "__FIELD_NAME_TO_FILTER__" = ? 
"""

# menu items
MENU_ADMIN = (
    "Create table: PERSONS",
    "Add record to table: PERSONS",
    "Import table: PERSONS from csv (removing old DB table)",
    "Drop table: PERSONS",
    "Update table record: PERSONS\n",
    
    "Create table: POSITIONS",
    "Add record to table: POSITIONS",
    "Import table: POSITIONS from csv (removing old DB table)",
    "Drop table: POSITIONS",
    "Update table record: POSITIONS\n",
    
    "Create table: COURSES",
    "Add record to table: COURSES",
    "Import table: COURSES from csv (removing old DB table)",
    "Drop table: COURSES"
    "Update table record: COURSES\n",
   
)

MENU_STUDENT = ()
MENU_TEACHER = ()
