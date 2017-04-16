from alfred.modules.api.a_base_module import ABaseModule

from .models.todo_list_item import TodoListItem


class AlfredTodo(ABaseModule):
    def __init__(self, *args, **kwargs):
        ABaseModule.__init__(self, *args, **kwargs)
        self.todo_list = []
        TodoListItem.db_path(self.database_path)

    def callback(self):
        self.todo_list = TodoListItem.all()

    def construct_view(self):
        self.render_template('List.html', list_items=self.todo_list)

    def on_new_item_submitted(self, value):
        if value == "":
            return

        item = TodoListItem()

        item.text = value
        item.status = 0
        item.save()

        self.todo_list.append(item)
        self.render_template('List.html', list_items=self.todo_list)
