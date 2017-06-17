from alfred.modules.api.view_components import AActionIcon, ACheckbox, ACompositeComponent, AParagraph


class Checklist(ACompositeComponent):
    def __init__(self, items=[], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_items = list(map(
            lambda x: ACheckbox(
                x[0],
                x[1],
                AActionIcon("delete", "red", "delete", x[2]),
                id="item_{}".format(x[2])
            ),
            items
        ))
        self.root_component = AParagraph(*self.list_items)

    def add_item(self, item):
        element = ACheckbox(
            item.text,
            item.status,
            AActionIcon("delete", "red", "delete", item.id),
            id="item_{}".format(item.id)
        )
        self.list_items.append(element)
        return element

    def get_element_by_id(self, id):
        return next(filter(lambda item: item.dom_id == id, self.list_items))