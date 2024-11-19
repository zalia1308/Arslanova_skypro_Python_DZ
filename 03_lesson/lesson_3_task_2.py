from smartphone import Smartphone

# Создаем список телефонов (картотеку)
catalog = [
    Smartphone("Apple", "iPhone 16 Pro Max", "+79968178802"),
    Smartphone("Xiaomi", "15 Pro", "+79016230290"),
    Smartphone("Samsung", "Galaxy S24 Ultra", "+79354417058"),
    Smartphone("Honor", "Magic6 Pro", "+79839997638"),
    Smartphone("realme", "GT 6", "+79084093971")

]

# Печатаем картотеку
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")