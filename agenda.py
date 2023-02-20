SCHEDULE = {
    "pedrinho":{
        "Telefone": "93132-4123",
        "Email": "pedrinho@solyd.com",
        "Endereço": "Não tem"
    }
}


def read_contact(name):
    print(name+":")
    for info in SCHEDULE[name]:
        print(f"\t{info}: {SCHEDULE[name][info]}")

def show_all_schedule():
    for contact in SCHEDULE:
        print(contact.upper())
        for info in SCHEDULE[contact]:
            print(f"\t{info}: {SCHEDULE[contact][info]}")        


def create_contact():
    name = input("nome do contato: ")
    SCHEDULE[name]={
        "Telefone": input(f"telefone do {name}: "),
        "Email": input(f"email do {name}: "),
        "Endereco": input(f"endereco do {name}: ")
    }
    print("\ncontato criado\n")

show_all_schedule()