def check_authentication(request, context):
    if request.user.is_authenticated:
        context["authenticated"] = True
    else:
        context["authenticated"] = False
    return context
