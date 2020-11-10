from django import template

register = template.Library()


@register.inclusion_tag('templates_advanced/tags/todo-item.html')
def todo_details(todo):
    return {
        'todo': todo,
    }
