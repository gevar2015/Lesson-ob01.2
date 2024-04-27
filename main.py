class Item:
    def __init__(self, name, price, category=None, description=None):
        self.name = name
        self.price = price
        self.category = category
        self.description = description

    def __str__(self):
        return f"{self.name} (цена: {self.price}, категория: {self.category}, описание: {self.description})"
class Store:
    def __init__(self, name, address):
        """Инициализирует новый магазин с названием, адресом и пустым списком товаров."""
        self.name = name
        self.address = address
        self.items = []

    def add_item(self, item):
        """Добавляет объект Item в ассортимент магазина."""
        self.items.append(item)
        print(f"Товар '{item.name}' добавлен с ценой {item.price}.")

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента магазина по имени."""
        original_len = len(self.items)
        self.items = [item for item in self.items if item.name != item_name]
        if len(self.items) < original_len:
            print(f"Товар '{item_name}' удален из ассортимента.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def get_price(self, item_name):
        """Возвращает цену товара по его названию. Если товар отсутствует, возвращает None."""
        for item in self.items:
            if item.name == item_name:
                return item.price
        return None

    def update_price(self, item_name, new_price):
        """Обновляет цену товара. Если товар отсутствует, сообщает об этом."""
        for item in self.items:
            if item.name == item_name:
                item.price = new_price
                print(f"Цена товара '{item_name}' обновлена до {new_price}.")
                return
        print(f"Товар '{item_name}' не найден для обновления цены.")
# Создание объектов магазинов
store1 = Store("FreshMarket", "100 Avenue Rd")

# Добавление товаров в магазины
store1.add_item(Item("apples", 0.5, "Фрукты"))
store1.add_item(Item("bananas", 0.75, "Фрукты"))

# Протестировать методы на одном из магазинов
print("\nТестирование методов для 'FreshMarket':")
store1.add_item(Item("pears", 0.6, "Фрукты"))
store1.update_price("apples", 0.65)
store1.remove_item("bananas")
print("Цена яблок:", store1.get_price("apples"))
print("Цена бананов:", store1.get_price("bananas"))
