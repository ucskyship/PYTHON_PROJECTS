class BasketSize:

    def __int__(self, basket_size: int) -> None:
        self.basket_size = basket_size
        self.basket = []

    def buy_item(self, item: str) -> None:
        self.basket.append(item)
        if len(self.basket) > self.basket_size:
            self.basket.pop(0)
