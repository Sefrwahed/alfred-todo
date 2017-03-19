from alfred.modules.api.a_base_module import ABaseModule
from alfred.modules.api.a_heading import AHeading

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker


class AlfredTodo(ABaseModule):
	def __init__(self, *args, **kwargs):
        ABaseModule.__init__(self,*args,**kwargs)
        self.todo_list = []
        self.todo_table = None

    def callback(self, action, item):
    	if(action=="add"):
    		self.add_item_to_list(item)
    	elif(action=="remove"):
    		self.remove_item_from_list(item)
    	elif(action=="view"):
    		self.todo_list = self.get_list()
    		self.construct_view()

    def add_item_to_list(self,item):
	    module = todo_list(item)
	    session = make_session()
	    session.add(item)
	    session.commit()
	    session.close()

	def remove_item_from_list(item):
	    session = make_session()
	    session.query(todo_list_items).filter(todo_list_items.list_item == item).delete()
	    session.commit()
	    session.close()

   
     def get_list(self, id):
	    session = make_session()
	    result = session.query(todo_list_items).all()
	    session.close()
	    return result
    
    def construct_view(self):
        h1 = AHeading(1, "Your List :")
        todo = AList(self.todo_list)
        self.add_component(h1)
        self.add_component(todo)




   