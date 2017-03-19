import jinja2

class AList():

    def __init__(self, type, listItems):
        self.type = type
        self.list_items = listItems
        self.render_list()

    def render_list(self):
        template_loader = jinja2.FileSystemLoader(searchpath="..")
        template_env = jinja2.Environment(loader=template_loader)
        # template_file = self.which_list()
        template_file = "List"
        template = template_env.get_template("/templates/" + template_file)
        template_vars = {"list_items": self.list_items, 
                         "type":self.type,
                         "x":self.x,
                         "y":self.y }
        output = template.render(template_vars)
        result_file = open(self.type + "_output_file.html", 'a')
        result_file.write(output)
        result_file.close()
