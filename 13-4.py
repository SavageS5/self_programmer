# Создайте классы Horse и Rider. Используйте композицию,
# чтобы смоделировать лошадь с всадником на ней
#
class Horse():
    def __init__(self, h_name, rider):    # Имя лошади и всадника
        self.h_name = h_name
        self.rider =rider

class Rider():
    def __init__(self, name):
        self.name = name

pol = Rider('Pol Maslov')       # Создали всадника(экземпляр класса)
black = Horse('Blacky', pol)    # лошадке дали наездника в переменной
print(black.rider.name)         # атрибутом name из класса Rider получили
                                # имя всадника лошадки Blacky из класса Horse
                                # КОМПОЗИЦИЯ!
