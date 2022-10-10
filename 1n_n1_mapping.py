from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

URL = "mysql+mysqlconnector://aluno:aluno123@localhost:3306/ORM_1N_N1"

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

    telefones = relationship("Telefone")


class Telefone(Base):
    __tablename__ = "Telefone"
    id_telefone = Column(Integer, primary_key=True)
    numero = Column(String(20))

    id_pessoa = Column(Integer, ForeignKey("Pessoa.id_pessoa"))


def main():
    engine = create_engine(url=URL)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    # mysql> DESC Pessoa;

    Session = sessionmaker(engine, expire_on_commit=False)

    with Session.begin() as session:
        pessoa = Pessoa(nome="Alice Rossinholi Venezian")

        pessoa.telefones.append(
            Telefone(numero="+5512999999999", id_pessoa=pessoa.id_pessoa))

        session.add(pessoa)


if __name__ == "__main__":
    main()
