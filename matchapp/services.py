def get_context_for_mail(user):
    return {
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name
    }

