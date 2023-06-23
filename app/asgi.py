import os
from importlib.util import find_spec

from django.apps import apps
from django.conf import settings
from django.core.wsgi import get_wsgi_application

from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles

# Export Django settings env variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
apps.populate(settings.INSTALLED_APPS)

# This endpoint imports should be placed below the settings env declaration
# Otherwise, django will throw a configure() settings error
from app.api_router import router as api_router

# Get the Django WSGI application we are working with
django_app = get_wsgi_application()

# This can be done without the function, but making it functional
# tidies the entire code and encourages modularity
def get_application() -> FastAPI:
    #Main Fast API application
    app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json",
        debug=settings.DEBUG
    )

    # Include all api endpoints
    app.include_router(api_router, prefix=settings.API_V1_STR)

    # to mount Django
    app.mount("/", WSGIMiddleware(django_app))

    # Set Up the static files and directory to serve django static files
    app.mount('/static',
              StaticFiles(
                  directory=os.path.normpath(
                      os.path.join(find_spec('django.contrib.admin').origin, '..', 'static')
                  )
              ),
              name='static',
              )

    return app

app = get_application()