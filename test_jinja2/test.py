import jinja2

class Ctx:
    pass

env = jinja2.Environment(loader=jinja2.FileSystemLoader('./'))

print(env.get_template('2.j2').render(ctx=Ctx()))
