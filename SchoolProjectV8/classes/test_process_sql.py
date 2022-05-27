import pathlib
import school_constants as c
import datetime, sqlite3
# universal query
PATH_TO_FILE_DATABASE = pathlib.Path(__file__).parent.parent.joinpath(c.FOLDER_DATABASE).joinpath(c.FILE_DATABASE)
def execute_sql_query(query_string: str, query_parameters: list | None = None) -> str | None:
    res = None
    last_message = ""
    # common part
    try:
        # query database
        with sqlite3.connect(PATH_TO_FILE_DATABASE) as conn:
            cursor = conn.cursor() # Create cursor object to operate with DB
            last_message += F"\n{datetime.datetime.now()}\t{c.SET_INFO_MESSAGE_COLOR}Reading database started at{c.RESET_COLOR}\n"
            # difference
            match (query_string.split()[0], query_parameters): # structural pattern matching 
                case ("SELECT", None):
                    res = cursor.execute(query_string).fetchall()
                    pass
                case ("DROP", None):
                    if input("Sure?[y]: ") == 'y': cursor.execute(query_string)
                    pass
                case ("CREATE", None):
                    cursor.execute(query_string)
                    pass
                case ("INSERT" | "UPDATE", *parameters):
                    print ("INSERT  | UPDATE")
                    cursor.executemany(query_string, query_parameters)
                    pass
                case _:
                    print ("Undefiner query type")
                    
                    pass
            pass # END SQL
    except sqlite3.Error as err:
        last_message += F"\n{datetime.datetime.now()}\t{c.SET_ERROR_MESSAGE_COLOR}{err}{c.RESET_COLOR}\n"
        pass
    finally:
        last_message += F"\n{datetime.datetime.now()}\t{c.SET_INFO_MESSAGE_COLOR}Reading database ended{c.RESET_COLOR}\n"
        pass 
    return res


# call
Q_1 = """
CREATE TABLE IF NOT EXISTS "test1" (
	"position_id"	INTEGER NOT NULL UNIQUE,
	"position_name"	TEXT UNIQUE,
	"description"	TEXT,
	PRIMARY KEY("position_id" AUTOINCREMENT)
);
"""
Q_2 = """
DROP TABLE IF EXISTS "test1" ;
"""
Q_3 = """
INSERT INTO "test1"("position_name","description") VALUES (?,?);
"""

Q_4 = """
SELECT * FROM 'test1';
"""
positions = [[F"Position_00{i}", F"Position {i} description"] for i in range(20)]
# print (positions)
# print(execute_sql_query(Q_3, positions))
print(execute_sql_query(Q_4))
