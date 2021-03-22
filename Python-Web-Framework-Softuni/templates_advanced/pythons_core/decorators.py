from django.http import HttpResponse


def groups_required(groups=[]):
    groups_set = set(groups)
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user = request.user
            user_groups = set(user.groups.all())

            # if user has the group
            if user_groups.intersection(groups_set):
                return view_func(request, *args, **kwargs)
            else:
                # user it not authorized if he doesn't have the group
                return HttpResponse('You are nto authorized')

        return wrapper
    return decorator