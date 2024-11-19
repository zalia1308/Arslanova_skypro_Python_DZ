from address import Address
from mailing import Mailing

to_address = Address("442280", "Алексеевка", "Огородная", "2", "38")
from_address = Address("198411", "Ломоносов", "Верещагина", "101", "5")


mailing = Mailing("157785", to_address, from_address, "10520")

print(mailing)