from django_unicorn.components import UnicornView


class ParentView(UnicornView):
    active_view = "child1"

    def toggle(self):
        self.active_view = 'child1' if self.active_view == 'child2' else 'child2'
