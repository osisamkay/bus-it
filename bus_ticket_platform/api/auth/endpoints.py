from ninja import Router
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from ninja.security import HttpBearer
from ninja.errors import HttpError
from .schemas import SignUpSchema, LoginSchema

router = Router()


class AuthBearer(HttpBearer):
    def authenticate(self, request, token: str):
        try:
            user = Token.objects.get(key=token).user
            return user
        except Token.DoesNotExist:
            raise HttpError(401, "Invalid token")


@router.post("/signup")
def signup(request, payload: SignUpSchema):
    user = User.objects.create(
        username=payload.username,
        password=make_password(payload.password),
        email=payload.email
    )
    return {"message": "User created successfully"}


@router.post("/login")
def login(request, payload: LoginSchema):
    user = authenticate(username=payload.username, password=payload.password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return {"token": token.key}
    else:
        raise HttpError(401, "Invalid credentials")


@router.get("/secure-endpoint", auth=AuthBearer())
def secure_endpoint(request):
    return {"message": f"Hello, {request.auth.username}!"}
