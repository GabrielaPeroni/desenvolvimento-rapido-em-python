def login_status(request):
    return {
        'username': request.session.get('username', None)
    }
