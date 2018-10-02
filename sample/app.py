
class App(object):

    constant = 100

    @classmethod
    def sum(cls, x, y):
        return x + y

    def dont_cover(self, a):
        return self.constant + a

    def __str__(self):
        return "App"

    def test(self):
        print("This is a test!")
    
