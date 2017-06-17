from alfred.modules.api.view_components import AActionIcon, ACheckbox, ACompositeComponent, AParagraph


class Checklist(ACompositeComponent):
    def __init__(self, items=[], *args, **kwargs):
        super().__init__(*args, **kwargs)
        list_items = list(map(
            lambda x: ACheckbox(x[0], x[1], x[2], AActionIcon("delete", "red", "delete", x[2])),
            items
        ))
        self.root_component = AParagraph(*list_items)

    def add_item(self, item):
        self.root_component.add_to_content(
            ACheckbox(item[0], item[1], item[2], AActionIcon("delete", "red", "delete", item[2]))
        )