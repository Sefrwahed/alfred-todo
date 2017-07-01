import random

from alfred.modules.api.a_base_widget import ABaseWidget
from alfred.modules.api.view_components import AHeading

from .models.todo_list_item import TodoListItem

class AlfredTodoWidget(ABaseWidget):
    def callback(self):
        unchecked_tasks = TodoListItem.find_by(status=0)
        self.random_unchecked_task = None
        if unchecked_tasks:
            self.random_unchecked_task = random.choice(unchecked_tasks)

    def construct_view(self):
        self.color = random.choice(["yellow", "green accent-2", "light-blue accent-2", "indigo accent-1"])
        if self.random_unchecked_task is None:
            self.title = "Nothing To Do"
            self.content.append(AHeading(3, "All Caught Up! Have Fun :)"))
        else:
            self.title = "You Have Things To Do"
            self.content.append(AHeading(3, self.random_unchecked_task.text))
