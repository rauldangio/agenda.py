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

read_contact("pedrinho")