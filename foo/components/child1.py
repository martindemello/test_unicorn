from django_unicorn.components import UnicornView


class Child1View(UnicornView):
    def hello(self):
        print('called on child1')
