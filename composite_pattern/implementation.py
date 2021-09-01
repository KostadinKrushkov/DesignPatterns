class BaseTodo:  # Component
    def get_html(self):
        pass


class Todo(BaseTodo):  # Leaf
    text = None

    def __init__(self, text):
        self.text = text

    def get_html(self):
        return self.text


class TodoList(BaseTodo):  # Composite
    title = None
    todos = None

    def __init__(self, title, todos=None):
        self.title = title
        self.todos = todos if todos else []

    def get_html(self):
        html = "\n<h1>{0}</h1>\n<ul>".format(self.title)
        for todo in self.todos:
            html += "\n<li>{}</li>".format(todo.get_html())
        html += "\n</ul>\n"
        return html

    def add_todo(self, todo):
        self.todos.append(todo)

    def remove_todo(self, todo):
        self.todos.remove(todo)

    def remove_todo_by_index(self, index):
        if 0 <= index < len(self.todos):
            del self.todos[index]
        else:
            raise Exception("Index does not match any todo in list.")


if __name__ == "__main__":
    inner_todo_list = TodoList("4", [Todo("4 - One"), Todo("4 - Two"), Todo("4 - Three")])
    todo_list = TodoList("Some list", [Todo("1"), Todo("2"), Todo("3"), inner_todo_list])

    todo_list.add_todo(Todo("5"))
    todo_list.add_todo(Todo("6"))
    inner_todo_list.remove_todo_by_index(2)

    print(todo_list.get_html())