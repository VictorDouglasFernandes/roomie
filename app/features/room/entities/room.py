class Room:
    def __init__(self, price: float, image: str):
        if isinstance(price, str):
            self.price = price
        if isinstance(image, str):
            self.image = image
