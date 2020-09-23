from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from django.http import HttpResponseBadRequest
from restaurants.models import Restaurant
from django.http import HttpResponse


def anonymous_required(function=None, redirect_url=None):
    if not redirect_url:
        redirect_url = settings.LOGIN_REDIRECT_URL

    actual_decorator = user_passes_test(
        lambda u: u.is_anonymous,
        login_url=redirect_url
    )

    if function:
        return actual_decorator(function)
    return actual_decorator

def ajax_required(f):
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return f(request, *args, **kwargs)

    wrap.__doc__=f.__doc__
    wrap.__name__=f.__name__
    return wrap

def must_be_owner(f):
    def check_owner(request, *args, **kwargs):
        restaurant_slug = kwargs['restaurant']
        restaurant = Restaurant.objects.get(slug=restaurant_slug)
        if not restaurant.owner.id == request.user.id:
            return HttpResponse('Esta tienda no te pertenece, acceso denegado', content_type='application/json', status=403)
        return f(request, *args, **kwargs)
    return check_owner



