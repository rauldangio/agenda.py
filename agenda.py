SCHEDULE = {
    "pedrinho":{
        "Telefone": "93132-4123",
        "Email": "pedrinho@solyd.com",
        "Endereço": "Não tem"
    }
}


def read_contact(name):
    print('-'*30)
    print(name.upper()+":")
    for info in SCHEDULE[name]:
        print(f"\t{info}: {SCHEDULE[name][info]}")
    print('-'*30)


def show_all_schedule():
    for contact in SCHEDULE:
        read_contact(contact)    


def create_contact():
    name = input("nome do contato: ")
    SCHEDULE[name]={
        "Telefone": input(f"telefone do {name}: "),
        "Email": input(f"email do {name}: "),
        "Endereco": input(f"endereco do {name}: ")
    }
    print("\ncontato criado\n")


def update_contact(name,tel,email,end):
    SCHEDULE[name] = {
        "Telefone": tel,
        "Email": email,
        "Endereco": end
    }
    print(f">>>>>> contato {name} foi atualizado!")


def delete_contact(name):
    SCHEDULE.pop(name)
    print(f">>>>>> contato {name} removido")


def show_menu():
    print()
    print("1 -> criar contato")
    print("2 -> buscar contato")
    print("3 -> ver todos os contatos")
    print("4 -> remover contato")
    print("5 -> atualizar contato")
    print("6 -> sair da agenda")
    print()
