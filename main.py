import tkinter as tk
from tkinter import ttk


class Shops:
    def __init__(self, shop1, shop2):
        self.shop1 = shop1
        self.shop2 = shop2

    def compare_prices(self, product, quantity):
        if product in self.shop1 and product in self.shop2:
            price_shop1 = self.shop1[product] * quantity
            price_shop2 = self.shop2[product] * quantity

            if price_shop1 < price_shop2:
                return f"Цена за {quantity} шт. = {price_shop1} евро, {product} дешевле в магазине Lidl"
            elif price_shop1 > price_shop2:
                return f"Цена за {quantity} шт. = {price_shop2} евро, {product} дешевле в магазине Rewe"
            else:
                return f"Цена за {quantity} шт. = {price_shop1} евро, {product} одинаковые в обоих магазинах"
        else:
            return f"Продукт {product} отсутствует в магазине выберите другой продукт "


class ShopCompareGUI:
    def __init__(self, master, shop_comparator):
        self.master = master
        self.master.title("Сравнение цен в магазинах")
        self.shop_comparator = shop_comparator

        self.label = tk.Label(master, text="Выберите продукт для сравнения цен:")
        self.label.pack()

        # Задайте ваши продукты для выбора
        products = ['Яблоки', 'Бананы', 'Груши', 'Апельсины', 'Ананасы', 'Лимоны', 'Сливы', 'Манго', 'Виноград',
                    'Лаймы', 'Клубника', 'Картошка', 'Вишня', 'Малина', 'Хлеб', 'Молоко', 'Черника', 'Арбузы']

        self.product_combobox = ttk.Combobox(master, values=products)
        self.product_combobox.pack()

        self.label_quantity = tk.Label(master, text="Введите количество:")
        self.label_quantity.pack()

        self.quantity_entry = tk.Entry(master)
        self.quantity_entry.pack()

        self.compare_button = tk.Button(master, text="Сравнить цены", command=self.compare_prices)
        self.compare_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        master.minsize(400, 300)

    def compare_prices(self):
        selected_product = self.product_combobox.get().lower()
        quantity = int(self.quantity_entry.get()) if self.quantity_entry.get().isdigit() else 1
        result = self.shop_comparator.compare_prices(selected_product, quantity)
        self.result_label.config(text=result)


# Создан словарь класса Shops
Li_dl = {'яблоки': 3.50, 'бананы': 1.45, 'груши': 2.00,
         'апельсины': 1.90, 'ананасы': 5.55, 'лимоны': 0.98,
         'сливы': 4.35, 'манго': 3.40, 'виноград': 3.00, 'лаймы': 1.40,
         'клубника': 2.80, 'картошка': 3.50, 'вишня': 3.00,
         'малина': 2.40, 'хлеб': 2.60, 'молоко': 1.40, 'черника': 1.09, 'арбузы': 3.99}

Re_we = {'яблоки': 2.50, 'бананы': 0.45, 'груши': 2.00,
         'апельсины': 2.90, 'ананасы': 4.55, 'лимоны': 1.98,
         'сливы': 1.35, 'манго': 2.40, 'виноград': 2.00, 'лаймы': 2.40,
         'клубника': 3.80, 'картошка': 2.50, 'вишня': 4.00,
         'малина': 3.40, 'хлеб': 1.60, 'молоко': 2.40, 'черника': 1.40, 'арбузы': 4.99}
shop_all = Shops(Li_dl, Re_we)

# интерфейс
root = tk.Tk()
app = ShopCompareGUI(root, shop_all)
root.mainloop()
