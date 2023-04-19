# SQLAlchemy-course

It's a SQL toolkit and ORM that gives developers the full power and flexibility of SQL.


### About
This tutorial will help you to get basic understanding of :
- what is SQLAlchemy
- how to use it
- installation
- crud operation

---
### Installation

        # download postgres: $brew install postgresql@14
        # postgres driver: $pip3 install psycopg2
        # install SQLAlchemy: $pip3 install sqlalchemy


### run postgres server
        
        # start: $brew services start postgresql
        # stop: $brew services stop postgresql
        # verify if postgres running: $psql postgres
        # list all dbs: postgres=# \l
        # list all tables: mydatabase=# \dt

---

### How to use SQLAlchemy:

- To connect with SQLAlchemy ORM, use create_engine class and provide the basic info like: 
which sql you want to use, user_name, password, host_name, port, db_name


        engine = create_engine("postgresql://localhost:5432/postgres", echo=False)

- create a session of above engine, now we are ready to run sql queries using SQLAlchemy ORM

        Session = sessionmaker(bind=engine)
        session = Session()




#### Part 1: [create Table]
- declare an instance of `declarative_base` which is a base class for declarative models in SQLAlchemy.

        Base = declarative_base()

- create a model, here I'm creating a simple model named `Student` with its properties: name, age, grade
        
        class Student(Base):
            __tablename__ = 'student'
    
            id = Column(Integer, primary_key=True)
            name = Column(String(50))
            age = Column(Integer)
            grade = Column(String(50))


- Let's create `Student` table in the `postgres db` using SQLAlchemy ORM

        Base.metadata.create_all(engine)


#### Part 3: [insert Table]
        

#### Part 3: [read Table]


#### Part 4: [update Table]
        

#### Part 5: [delete Table]


