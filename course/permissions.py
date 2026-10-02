from django.core.exceptions import PermissionDenied


def teacher_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied("Необходимо авторизоваться")

        if request.user.role != "teacher":
            raise PermissionDenied("Доступ только для преподавателей")

        return view_func(request, *args, **kwargs)

    return wrapper


def student_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied("Необходимо авторизоваться")

        if request.user.role != "student":
            raise PermissionDenied("Доступ только для студентов")

        return view_func(request, *args, **kwargs)

    return wrapper


def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied("Необходимо авторизоваться")

        if request.user.role != "admin":
            raise PermissionDenied("Доступ только для администратора")

        return view_func(request, *args, **kwargs)

    return wrapper