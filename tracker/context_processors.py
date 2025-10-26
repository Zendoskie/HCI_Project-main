def app_name(request):
    """Context processor to add app name globally"""
    return {
        'app_name': 'Task Tracker Demo'
    }
