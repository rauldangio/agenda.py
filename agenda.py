SCHEDULE = {
  
}

def create_contact():
    name = input("nome do contato: ")
    SCHEDULE[name]={
        "tel": input(f"telefone do {name}: "),
        "email": input(f"email do {name}: "),
        "endereco": input(f"endereco do {name}: ")
    }
    print("\ncontato criado")

create_contact()
print(SCHEDULE)