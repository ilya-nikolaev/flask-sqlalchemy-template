from db.utils.create import get_engine, create_db


def main():
    create_db(get_engine())


if __name__ == '__main__':
    main()
