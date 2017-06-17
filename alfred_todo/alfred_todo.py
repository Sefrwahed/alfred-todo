from alfred.modules.api.a_base_module import ABaseModule
from alfred.modules.api.view_components import AForm, ATextField, ATextField, ADivider
from .models.todo_list_item import TodoListItem
from .views.checklist import Checklist

class AlfredTodo(ABaseModule):
    def __init__(self, *args, **kwargs):
        ABaseModule.__init__(self, *args, **kwargs)
        self.todo_list = []

    def callback(self):
        self.todo_list = TodoListItem.all()

    def construct_view(self):
        self.add_component(AForm(
            True,
            "add_circle_outline",
            ATextField("new_item", "New Item"),
            id="new_item_form"
        ))
        self.add_component(Checklist(
            list(map(
                lambda item: (item.text, bool(item.status), item.id),
                self.todo_list
            ))
        ))

    def on_new_item_form_submitted(self, form_data):
        item = TodoListItem()

        if form_data.get("new_item") == "":
            return

        item.text = form_data["new_item"]
        item.status = 0
        item.save()

        self.components = []
        self.callback()
        self.construct_view()
        self.populate_view()

    def on_checkbox_click(self, attrs):
        item = TodoListItem.find(int(attrs['data-id']))
        item.status = 1 if item.status == 0 else 0
        item.save()


    def on_i_click(self, attrs):
        if attrs.get('data-action') == "delete":
            TodoListItem.find(int(attrs['data-id'])).delete()
            self.components = []
            self.callback()
            self.construct_view()
            self.populate_view()