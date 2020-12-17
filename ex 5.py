class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки ручкой'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки карандашом'


class Paintbrush(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки маркером'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
paintbrush = Paintbrush('Маркер')
print(pen.draw())
print(pencil.draw())
print(paintbrush.draw())
