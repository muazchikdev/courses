from django.conf import settings
from django.core.mail import send_mail


def send_welcome_email(user):
    """
    Отправка письма после регистрации пользователя
    """

    send_mail(
        subject='Добро пожаловать!',
        message=f'''
        Здравствуйте, {user.username}!
        
        Спасибо за регистрацию в системе онлайн-курсов.
        
        Желаем успешного обучения!
        ''',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=False,
    )


def send_enroll_email(user, course):
    """
    Отправка письма после записи на курс
    """

    send_mail(
        subject='Запись на курс',
        message=f'''
        Здравствуйте, {user.username}!

        Вы успешно записались на курс:

        {course.title}

        Удачного обучения!
        ''',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=False,
    )


def send_homework_notification(student, lesson):
    """
    Уведомление об успешной отправке домашнего задания
    """

    send_mail(
        subject='Домашнее задание отправлено',
        message=f'''
        Здравствуйте, {student.username}!

        Ваше домашнее задание по уроку:

        {lesson.title}

        успешно отправлено.
        ''',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[student.email],
        fail_silently=False,
    )


def send_new_lesson_notification(student, lesson):
    """
    Уведомление о новом уроке
    """

    send_mail(
        subject='Новый урок доступен',
        message=f'''
        Здравствуйте, {student.username}!

        Для вас доступен новый урок:

        {lesson.title}

        Можете приступать к изучению материала.
        ''',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[student.email],
        fail_silently=False,
    )