class Product:
    def __init__(self, name, price, product_id):
        self.name=name
        self.price=price
        self.product_id=product_id
    def get_info(self):
        return f"Товар: {self.name}, цена: {self.price} руб."
class Cart:
    def __init__(self):
        self.items=[]
    def add_product(self, product):
        self.items.append(product)
    def remove_product(self, product_id):
        if product_id in self.items:
            for i, product in enumerate(self.items):
                if product_id==product.product_id:
                    del self.items[i]
                    break
    def total_price(self):
        return sum(product.price for product in self.items)
    def clear(self):
        self.items.clear()
class Order:
    def __init__(self,order_id,cart,customer_name):
        self.order_id=order_id
        self.cart=cart
        self.customer_name=customer_name
        self.is_paid=False
    def get_total(self):
        return self.cart.total_price()
    def pay(self):
        self.is_paid=True
        return f"Заказ №{self.order_id} оплачен на сумму {self.get_total()} руб."
    def receipt(self):
        res=[]
        res.append(f'Заказ {self.order_id}')
        res.append(f'Покупатель: {self.customer_name}')
        res.append('---')
        for i, product in enumerate(self.cart.items):
            res.append(f'{i+1}. {product.name} - {product.price} руб.')
        res.append('---')
        res.append(f'Итого: {self.get_total()} руб.')
        if self.is_paid:
            res.append('Оплачен: Да')
        else:
            res.append('Оплачен: Нет')
        return '\n'.join(res)

