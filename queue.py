# Класс Queue. Очередь. FIFO - First In First Out - первый зашел -первый вышел. 
# Ассоциация - очередь..ну пусть за билетами в кино, например
#
#
#
class Queue():

    def __init__(self):
        self.items = []

# Очередь пуста? True, если да
    def is_empty(self):
        return self.items == []

# добавляем в очередь
    def enqueue(self, item):
        self.items.insert(0, item)

# Удаляем
    def dequeue(self):
        return self.items.pop()

# Определяем размер
    def sizequeue(self):
        return len(self.items)
