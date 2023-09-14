class Event:
    def __init__(self):
        self.__callbacks = []

    def register(self, callback):
        self.__callbacks.append(callback)

    def remove(self, callback):
        self.__callbacks.remove(callback)

    def trigger(self, *args, **kwargs):
        for callback in self.__callbacks:
            return callback(*args, **kwargs)

    def clear(self):
        self.__callbacks.clear()

    def destroy(self):
        self.clear()

    def __iadd__(self, callback):
        self.register(callback)
