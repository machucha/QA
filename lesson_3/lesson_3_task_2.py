from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "S26", "+795632511"),
    Smartphone("Nokia", "C15", "+795632581"),
    Smartphone("TECNO", "Nova 2", "+796932511"),
    Smartphone("Realme", "12+", "+795845511"),
    Smartphone("HONOR", "400", "+7956324851")
]

for phone in catalog:
    print(phone.tel_brend, "-", phone.tel_model + ".", phone.tel_number)
