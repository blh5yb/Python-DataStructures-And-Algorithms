
# update, use @lru.cache

class MemoizeData:
    def __init__(self):
        self.memory = {}

    def memoize(self, f):
        def inner(key, **kwargs):
            if key not in self.memory:
                self.memory[key] = f(kwargs)

            return self.memory[key]

        return inner

# decorator

def outer(f):
    def inner(*args):
        # do something before
        f(*args)
        # do something after?
        return
    return inner