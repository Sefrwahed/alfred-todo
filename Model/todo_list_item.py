class todo_list_items(DBModelBase):
    __tablename__ = 'todo_list'
    id = Column(Integer, primary_key=True)
    list_items = Column(String(300))
    
    def __init__(item):
        self.list_item = item
