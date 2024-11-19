class Mailing:
    def __init__(self, track, to_address, from_address, cost):
        self.track = track
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost


    def __str__(self):
        return (f"Отправление {self.track} из {self.from_address} в {self.to_address}. Стоимость {self.cost} рублей.")