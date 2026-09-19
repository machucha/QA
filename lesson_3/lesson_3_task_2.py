from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "S26", 895632511),
    Smartphone("Nokia", "C15", 895632581),
    Smartphone("TECNO", "Nova 2", 896932511),
    Smartphone("Realme", "12+", 895845511),
    Smartphone("HONOR", "400", 8956324851)
]

for phone in catalog:
    print(Smartphone.tel_brend, Smartphone.tel_model, Smartphone.tel_number)
