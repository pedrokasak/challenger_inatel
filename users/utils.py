def get_ip(request):
    try:
        real_ip = request.META.get('HTTP_X_FORWARDED_FOR').split(', ')[0]
    except AttributeError:
        real_ip = request.META.get('HTTP_X_REAL_IP')
    if not real_ip:
        real_ip = request.META.get('REMOTE_ADDR')

    return real_ip

