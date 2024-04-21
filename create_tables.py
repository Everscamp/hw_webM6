from sqlite3 import Error

from connection import create_connection, database


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


if __name__ == '__main__':
    sql_create_tutors_table = """
    CREATE TABLE IF NOT EXISTS tutors (
     id integer PRIMARY KEY,
     name text NOT NULL
    );
    """

    sql_create_subjects_table = """
    CREATE TABLE IF NOT EXISTS subjects (
     id integer PRIMARY KEY,
     name text NOT NULL,
     tutor_id integer NOT NULL,
     FOREIGN KEY (tutor_id) REFERENCES tutors (id)
    );
    """

    sql_create_groups_table = """
    CREATE TABLE IF NOT EXISTS groups (
     id integer PRIMARY KEY,
     name text NOT NULL
    );
    """

    sql_create_students_table = """
    CREATE TABLE IF NOT EXISTS students (
     id integer PRIMARY KEY,
     name text NOT NULL,
     group_id int NOT NULL,
     FOREIGN KEY (group_id) REFERENCES groups (id)
    );
    """

    sql_create_marks_table = """
    CREATE TABLE IF NOT EXISTS marks (
     id integer PRIMARY KEY,
     mark integer,
     subject_id integer NOT NULL,
     student_id integer NOT NULL,
     fake_date TIMESTAMP, 
     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
     FOREIGN KEY (subject_id) REFERENCES subjects (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE,
     FOREIGN KEY (student_id) REFERENCES students (id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
    );
    """

    with create_connection(database) as conn:
        if conn is not None:
            # create tutors table
            create_table(conn, sql_create_tutors_table)
            # create subjects table
            create_table(conn, sql_create_subjects_table)
            # create groups table
            create_table(conn, sql_create_groups_table)
            # create students table
            create_table(conn, sql_create_students_table)
            # create marks table
            create_table(conn, sql_create_marks_table)
        else:
            print("Error! cannot create the database connection.")
