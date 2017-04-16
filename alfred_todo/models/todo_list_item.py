from alfred.modules.api.a_base_model import ABaseModel


class TodoListItem(ABaseModel):
    def __str__(self):
        return self.text
