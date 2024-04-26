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

# Создание объектов магазинов
store1 = Store("FreshMarket", "100 Avenue Rd")
store2 = Store("GreenGrocer", "200 Shopping Ln")
store3 = Store("Organic Foods", "300 Eco Park")

# Добавление товаров в магазины
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2.add_item("oranges", 0.8)
store2.add_item("tomatoes", 1.2)

store3.add_item("milk", 1.5)
store3.add_item("bread", 1.0)

# Протестировать методы на одном из магазинов
print("\nТестирование методов для 'FreshMarket':")
store1.add_item("pears", 0.6)
store1.update_price("apples", 0.65)
store1.remove_item("bananas")
print("Цена яблок:", store1.get_price("apples"))
print("Цена бананов:", store1.get_price("bananas"))

