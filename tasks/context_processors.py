def app_name(request):
    """
    Context processor to add application name to all templates.
    
    This demonstrates how context processors work in Django.
    The data returned here will be available in ALL templates
    without needing to pass it from each view.
    
    Returns:
        dict: Dictionary containing app_name key
    """
    return {
        'app_name': 'To-Do MVT Demo',
        'app_version': '1.0.0',
        'app_description': 'Django MVT Architecture Demonstration',
    }
