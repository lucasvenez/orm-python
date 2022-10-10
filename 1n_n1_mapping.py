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

    telefones = relationship("Telefone", backref="pessoa")

    def __str__(self):
        return "Pessoa(id_pessoa={}, nome=\"{}\")".format(
            self.id_pessoa, self.nome)


class Telefone(Base):
    __tablename__ = "Telefone"
    id_telefone = Column(Integer, primary_key=True)
    numero = Column(String(20))

    id_pessoa = Column(Integer, ForeignKey("Pessoa.id_pessoa"))

    def __str__(self):
        return "Telefone(id_telefone={}, numero=\"{}\")".format(
            self.id_telefone, self.numero)


def main():
    engine = create_engine(url=URL)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    # mysql> DESC Pessoa;

    Session = sessionmaker(engine, expire_on_commit=False)

    with Session.begin() as session:
        pessoa = Pessoa(nome="Alice Rossinholi Venezian")

        for i in range(10):
            pessoa.telefones.append(
                Telefone(numero="+551299999999{}".format(i)))

        session.add(pessoa)

    with Session.begin() as session:

        print("============================================")

        pessoa = session.query(Pessoa).get(1)

        print(pessoa)

        for telefone in pessoa.telefones:
            print("   * " + str(telefone))

    with Session.begin() as session:

        print("\n============================================")

        telefone = session.query(Telefone).get(5)

        print(telefone)
        print(telefone.pessoa)


if __name__ == "__main__":
    main()
