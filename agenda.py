SCHEDULE = {
    "pedrinho":{
        "Telefone": "93132-4123",
        "Email": "pedrinho@solyd.com",
        "Endereço": "Não tem"
    }
}


def search_contact(name):
    print('-'*30)
    print(name.upper()+":")
    for info in SCHEDULE[name]:
        print(f"\t{info}: {SCHEDULE[name][info]}")
    print('-'*30)


def show_all_schedule():
    for contact in SCHEDULE:
        search_contact(contact)    


def create_contact():
    name = input("nome do contato: ")
    SCHEDULE[name]={
        "Telefone": input(f"telefone do {name}: "),
        "Email": input(f"email do {name}: "),
        "Endereco": input(f"endereco do {name}: ")
    }
    print(f"\n>>>>>> contato {name} criado\n")


def update_contact(name):
    print('oque deseja mudar?')
    upd = int(input(f"1 -> telefone\n2 -> email\n3 -> endereço\n4 -> tudo\n5 -> não quero mudar nada\nopção: "))
    if upd == 1:
        SCHEDULE[name]['Telefone'] = input("novo telefone: ")
    elif upd == 2:
        SCHEDULE[name]['Email'] = input("novo email: ")
    elif upd == 3:
        SCHEDULE[name]['Endereco'] = input("novo endereco: ")
    elif upd == 4:
        SCHEDULE[name]['Telefone'] = input("novo telefone: ")
        SCHEDULE[name]['Email'] = input("novo email: ")
        SCHEDULE[name]['Endereco'] = input("novo endereco: ")
    elif upd == 5:
        pass
    print(f">>>>>> contato {name} atualizado")

def delete_contact(name):
    SCHEDULE.pop(name)
    print(f">>>>>> contato {name} removido")


def show_menu():
    print('-'*40)
    print("1 -> criar contato")
    print("2 -> buscar contato")
    print("3 -> ver todos os contatos")
    print("4 -> remover contato")
    print("5 -> atualizar contato")
    print("6 -> sair da agenda")
    print('-'*40)


while True:
    show_menu()
    op = int(input('escolha uma opção: '))
    if op == 1:
        create_contact()
    elif op == 2:
        search_contact(input("contado: "))
    elif op == 3:
        show_all_schedule()
    elif op == 4:
        delete_contact(input("contado: "))
    elif op == 5:
        contact = input("contato: ")
        update_contact(contact)
    elif op == 6:
        break