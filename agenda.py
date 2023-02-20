agenda = {
    "joao":{
        "tel": "99312-3131",
        "email": "joao@email.com",
        "endereco": "av. 1"
    },
    "maria": {
        "tel": "78954-6241",
        "email": "maria@email.com",
        "endereco": "av. 2"
    },
    "raul": {
        "tel": "21233-6542",
        "email": "raul@email.com",
        "endereco": "av. 3"
    }
}

agenda['samanta'] = {
        "tel": "51234-3123",
        "email": "samanta@email.com",
        "endereco": "av. Pisca"
}

for contato in agenda:
    print(f"{contato}: ")
    for chaves in agenda[contato]:
        print(f"\t {chaves}: {agenda[contato][chaves]}")