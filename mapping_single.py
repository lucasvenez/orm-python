from sqlalchemy import create_engine, inspect

URL = "mysql+mysqlconnector://aluno:aluno123@localhost"


def main():
    engine = create_engine(url=URL)

    insp = inspect(engine)
    db_list = insp.get_schema_names()
    print(db_list)


if __name__ == "__main__":
    main()
