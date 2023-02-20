SCHEDULE = {
  
}


def read_contact(name):
    print(name+":")
    for info in SCHEDULE[name]:
        print(f"\t{info}: {SCHEDULE[name][info]}")


def create_contact():
    name = input("nome do contato: ")
    SCHEDULE[name]={
        "tel": input(f"telefone do {name}: "),
        "email": input(f"email do {name}: "),
        "endereco": input(f"endereco do {name}: ")
    }
    print("\ncontato criado\n")
    read_contact(name)

create_contact()
