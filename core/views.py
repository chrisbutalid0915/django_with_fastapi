# from django.shortcuts import render
from fastapi import APIRouter, Depends, FastAPI
from .api import hello_world
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from core import urls as core_urls

# Create your views here.
api = FastAPI()


def configure():
    api.include_router(hello_world.router)
