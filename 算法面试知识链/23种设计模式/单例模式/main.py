class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            cls._instance = super(Singleton,cls).__new__(cls)

        return cls._instance


class writeQuote(Singleton):
    def __init__(self,quote):
        self.quote =quote

    def print_quote(self):
        print(self.quote)


a =writeQuote("a")
b= writeQuote("b")
a.print_quote()
b.print_quote()
