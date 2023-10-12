from models import PessoaCRUD

def main():
    crud = PessoaCRUD()

    # CREATE
    crud.create("João", 30)
    crud.create("Maria", 28)

    # READ
    print(crud.read())  # Lista todas as pessoas
    print(crud.read(1))  # Exibe a pessoa com ID 1

    # UPDATE
    crud.update(1, "João Carlos", 31)

    # DELETE
    crud.delete(2)

    # READ após as operações
    print(crud.read())

if __name__ == "__main__":
    main()
