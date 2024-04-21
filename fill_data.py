from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_TUTORS = 5
NUMBER_SUBJECTS = 8
NUMBER_MARKS = 20


def generate_fake_data(number_tutors, number_subjects, number_groups, number_students, number_marks) -> tuple():
    fake_tutors = []  
    fake_subjects = []  
    fake_groups = []  
    fake_students = []  
    # fake_marks = [] 

    fake_data = faker.Faker()

    for _ in range(number_tutors):
        fake_tutors.append(fake_data.name())

    for _ in range(number_subjects):
        fake_subjects.append(fake_data.job())

    for _ in range(number_groups):
        fake_groups.append(f'{fake_data.random_number(1,50)} {fake_data.random_uppercase_letter()}')

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    # 
    # for _ in range(number_marks):
    #     fake_marks.append(fake_data.random_int(1, 5))

    return fake_tutors, fake_subjects, fake_groups, fake_students

def prepare_data(tutors, subjects, groups, students) -> tuple():
    fake_data = faker.Faker()
    for_tutors = []
    for tutor in tutors:
        for_tutors.append((tutor, ))

    for_subjects = []
    for sub in subjects:
        for_subjects.append((sub, randint(1, NUMBER_TUTORS), ))

    for_groups = []
    for grp in groups:
        for_groups.append((grp, ))

    for_students = []
    for std in students:
        for_students.append((std, randint(1, NUMBER_GROUPS), ))

    for_marks = []
    for s in range(1,  NUMBER_STUDENTS+1):
            for m in range(1, NUMBER_MARKS+1):
                mark = randint(1, 5)
                sub = randint(1, NUMBER_SUBJECTS)
                date = fake_data.date_time_between(datetime(2019,1,1), datetime.today())
                for_marks.append((mark, sub, s, date))


    return for_tutors, for_subjects, for_groups, for_students, for_marks


def insert_data_to_db(tutors, subjects, groups, students, marks) -> None:
    with sqlite3.connect('test.db') as con:
        cur = con.cursor()

        sql_to_tutors = """INSERT INTO tutors(name)
                               VALUES (?)"""
        cur.executemany(sql_to_tutors, tutors)


        sql_to_subjects = """INSERT INTO subjects(name, tutor_id)
                               VALUES (?, ? )"""
        cur.executemany(sql_to_subjects, subjects )

        sql_to_groups = """INSERT INTO groups(name)
                              VALUES (?)"""
        cur.executemany(sql_to_groups, groups)

        sql_to_students = """INSERT INTO students(name, group_id)
                              VALUES (?, ?)"""
        cur.executemany(sql_to_students, students)

        sql_to_marks = """INSERT INTO marks(mark, subject_id, student_id, fake_date)
                              VALUES (?, ?, ?, ?)"""
        cur.executemany(sql_to_marks, marks)

        con.commit()


if __name__ == '__main__':
    tutors, subjects, groups, students, marks = prepare_data(*generate_fake_data(
        NUMBER_TUTORS,NUMBER_SUBJECTS, NUMBER_GROUPS, NUMBER_STUDENTS, NUMBER_MARKS))
    # print(tutors)
    # print(subjects)
    # print(groups)
    # print(students)
    # print(marks)
    insert_data_to_db(tutors, subjects, groups, students, marks)


