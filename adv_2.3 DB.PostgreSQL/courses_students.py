import psycopg2 as pg
from config import DBNAME, USERNAME, PASSWORD

def create_tables():
    with pg.connect(dbname = DBNAME, user = USERNAME, password = PASSWORD) as conn:
        with conn.cursor() as curs:
            curs.executescript('''
                    CREATE TABLE IF NOT EXISTS Student (
                        id integer PRIMARY KEY NOT NULL,
                        name varchar(100) NOT NULL,
                        gra numeric(10,2) NULL,
                        birth timestamptz NULL
                    ); 

                    CREATE TABLE IF NOT EXISTS Course (
                        id integer PRIMARY KEY NOT NULL,
                        name varchar(100) NOT NULL
                    );  

                    CREATE TABLE IF NOT EXISTS Courses_Students (
                        id serial PRIMARY KEY,
                        course_id integer REFERENCES Course(id),
                        student_id integer REFERENCES Student(id)
                    );  
                ''')

def add_course(courses): 
    for course in courses:
        with pg.connect(dbname = DBNAME, user = USERNAME, password = PASSWORD) as conn:
            with conn.cursor() as curs:
                curs.execute(
                                '''
                                    INSERT INTO Course(id, name) VALUES(%s, %s);
                                ''', (course[0], course[1])
                            )  

def get_students(course_id): # возвращает студентов определенного курса
     with pg.connect(dbname = DBNAME, user = USERNAME, password = PASSWORD) as conn:
        with conn.cursor() as curs:
            curs.execute(
                    '''
                        SELECT Student.id, Student.name, Student.gra, Student.birth FROM Courses_Students
                        JOIN Student ON Student.id = Courses_Students.student_id
                        JOIN Course ON Course.id = Courses_Students.course_id
                        WHERE Courses_Students.course_id = %s;
                    ''', (str(course_id))
                 )

            students_list = curs.fetchall()

            for student in students_list:
                print(f"Номер: {student[0]}\nИмя: {student[1]}\nСредний балл: {student[2]}\nДата рождения: {student[3]}")

def add_students(course_id, students): # создание студентов с зачислением их на курс
    for student in students:
        with pg.connect(dbname = DBNAME, user = USERNAME, password = PASSWORD) as conn:
            with conn.cursor() as curs:
                curs.execute(
                        '''
                            INSERT INTO Student(id, name, gra, birth) VALUES(%s, %s, %s, %s);
                        ''', (student['id'], student['name'], student['gra'], student['birth'])
                    )

                curs.execute(
                        '''
                            INSERT INTO Courses_Students(course_id, student_id) VALUES(%s, %s);
                        ''', (course_id, student['id'])
                    )

def add_student(students): # создание студентов без зачисления на курс
    for student in students:
        with pg.connect(dbname = DBNAME, user = USERNAME, password = PASSWORD) as conn:
            with conn.cursor() as curs:
                curs.execute(
                        '''
                            INSERT INTO Student(id, name, gra, birth) VALUES(%s, %s, %s, %s);
                        ''', (student['id'], student['name'], student['gra'], student['birth'])
                    )

def get_student(student_id): #получение информации о студенте 
     with pg.connect(dbname = DBNAME, user = USERNAME, password = PASSWORD) as conn:
        with conn.cursor() as curs:
            curs.execute(
                    '''
                        SELECT Student.name, Student.gra, Student.birth, Course.name FROM Courses_Students
                        JOIN Student ON Student.id = Courses_Students.student_id
                        JOIN Course ON Course.id = Courses_Students.course_id
                        WHERE Courses_Students.student_id = %s;
                    ''', (str(student_id))
                 )

            student_info = curs.fetchall()
           
            for info in student_info:
                print(f"Имя: {info[0]}\nСредний балл: {info[1]}\nДата рождения: {info[2]}\nУчится на курсе(ах): {info[3]}")
                
if __name__ == "__main__":
    # create_tables()
    # add_course([[1, 'Основы Python'], [2, 'Основы SQL'], [3, 'Python для анализа данных']])
    # add_student([{'id': 1, 'name': 'Krylova Tatiana', 'gra': 4.8, 'birth': '25.03.1993'}])
    # add_student([{'id': 2, 'name': 'Jon', 'gra': 3.8, 'birth': None}, {'id': 3, 'name': 'Kim', 'gra': None, 'birth': '12.12.12'}])
    # add_students(1, [{'id': 4, 'name': 'Max', 'gra': 5, 'birth': None}])
    get_student(4)
    