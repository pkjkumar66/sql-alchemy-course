from sqlalchemy import create_engine, or_, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

############# connect with the Driver ##########################

## <which_sql>:://<user_name>:<password>@<host_name>:<port>/<db_name>
engine = create_engine("postgresql://localhost:5432/postgres", echo=False)

Session = sessionmaker(bind=engine)
session = Session()




############# create table ##########################

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))

# Migrate all the tables
# Base.metadata.create_all(engine)





############# insert entries in table ##########################

# student1 = Student(name="pankaj", age=25, grade="pg")
# session.add(student1)
# session.commit()

# student2 = Student(name="kamlesh", age=24, grade="ug")
# student3 = Student(name="ankita", age=23, grade="mba")
# session.add_all([student2, student3])
# session.commit()





############# read entries from table ##########################

## get all the entries of a table

# students = session.query(Student)
# for student in students:
#     print(student.name)


## get data in order

# students = session.query(Student).order_by(Student.name)
# for student in students:
#     print(student.name)


## get data by filtering : [https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query.filter]

# student = session.query(Student).filter(Student.name == "ankita").first()
# print(student.name, student.age)

# students = session.query(Student).filter(or_(Student.name == "ankita", Student.name == "pankaj"))
# for student in students:
#     print(student.name, student.age)


## count the number of results

# students_count = session.query(Student).count()
# print(students_count)




############# update entries of table ##########################

# student = session.query(Student).filter(Student.name == "ankita").first()
# print(student.name, student.age, student.grade)
# student.grade = "ug"
#
# student = session.query(Student).filter(Student.name == "ankita").first()
# print(student.name, student.age, student.grade)
#
# session.commit()



############# delete entries of table ##########################

# student = session.query(Student).filter(Student.name == "kamlesh").first()
# print(student.name, student.age, student.grade)
# session.delete(student)
# session.commit()
#
# student = session.query(Student).filter(Student.name == "kamlesh").first()
# print(student.name, student.age, student.grade)