import sqlite3

""" Розкоментуйте рядки 4 і 5 за потреби вводу аргументів через консоль """
# id = int(input("id 1 >>>"))
# id2 = int(input("id 2 >>>"))


def run_query():
    """ Вкажіть відповідну назву файла з запитом """
    with open('query_7.sql', 'r') as f:
        sql = f.read()
        
    with sqlite3.connect('test.db') as con:
        cur = con.cursor()
        """ Розкоментуйте рядок 15 за потреби вводу аргументів через консоль,
        не забудьте розкоментувати відповідні рядки в замих запитах """
        # cur.execute(sql, (id, ))може бути більше одного аргумента
        cur.execute(sql)
        print(cur.fetchall())


if __name__ == "__main__":
    run_query()