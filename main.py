class Store:
    def __init__(self, name, address):
        """Инициализирует новый магазин с названием, адресом и пустым словарем товаров."""
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент магазина с указанной ценой."""
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price}.")

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента магазина."""
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def get_price(self, item_name):
        """Возвращает цену товара по его названию. Если товар отсутствует, возвращает None."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара. Если товар отсутствует, сообщает об этом."""
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена до {new_price}.")
        else:
            print(f"Товар '{item_name}' не найден для обновления цены.")

# Пример использования класса
store = Store("GoodFoods", "123 Main St")
store.add_item("apples", 0.5)
store.add_item("bananas", 0.75)
print("Цена яблок:", store.get_price("apples"))

store.update_price("apples", 0.60)
print("Обновленная цена яблок:", store.get_price("apples"))

store.remove_item("bananas")
print("Цена бананов после удаления:", store.get_price("bananas"))
