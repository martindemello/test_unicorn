from django_unicorn.components import UnicornView


class Child2View(UnicornView):
    def hello(self):
        print('called on child2')
