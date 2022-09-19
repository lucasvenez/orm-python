from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import declarative_base

URL = "mysql+mysqlconnector://aluno:aluno123@localhost/ORM"

# $ cd C:\Program Files\MySQL\MySQL Server 8.0\bin
# $ .\mysql.exe -u aluno -p
# mysql> CREATE DATABASE ORM;
# mysql> USE ORM;
# mysql> SHOW TABLES;
Base = declarative_base()


class Pessoa(Base):
    __tablename__ = "Pessoa"
    id_pessoa = Column(Integer, primary_key=True)


def main():
    engine = create_engine(url=URL)

    with engine.connect() as connection:
        pass


if __name__ == "__main__":
    main()
