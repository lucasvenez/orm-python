from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

URL = "mysql+mysqlconnector://aluno:aluno123@localhost:3306/ORM"

# $ cd C:\Program Files\MySQL\MySQL Server 8.0\bin
# $ .\mysql.exe -u aluno -p
# mysql> CREATE DATABASE ORM;
# mysql> USE ORM;
# mysql> SHOW TABLES;
Base = declarative_base()


class Pessoa(Base):
    __tablename__ = "Pessoa"
    id_pessoa = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)


def main():
    engine = create_engine(url=URL)
    #Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    # mysql> DESC Pessoa;

    Session = sessionmaker(engine, expire_on_commit=False)

    with Session.begin() as session:
        pessoa = Pessoa(nome="Jhon Snow")
        id_pessoa = pessoa.id_pessoa
        session.add(pessoa)

    with Session.begin() as session:
        pessoa.nome = "Jhon Snow, The King Forever"
        id_pessoa = pessoa.id_pessoa
        session.add(pessoa)



if __name__ == "__main__":
    main()
