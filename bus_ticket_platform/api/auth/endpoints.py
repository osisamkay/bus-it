from ninja import Router
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from ninja.security import HttpBearer
from ninja.errors import HttpError
from .models import UserProfile
from .schemas import SignUpSchema, LoginSchema

router = Router()


class AuthBearer(HttpBearer):
    def authenticate(self, request, token: str):
        try:
            user = Token.objects.get(key=token).user
            return user
        except Token.DoesNotExist:
            raise HttpError(401, "Invalid token")


@router.post("/signup", response={200: dict, 400: dict}, tags=["Authentication"])
def signup(request, payload: SignUpSchema):
    try:
        user = User.objects.create_user(
            **payload.dict(exclude={"company", "contact_number", "company_logo_url", "company_slogan", "user_type"}))
        UserProfile.objects.create(user=user, **payload.dict(include={
                                   "company", "contact_number", "company_logo_url", "company_slogan", "user_type"}))
        return {"message": "User created successfully"}
    except Exception as e:
        return {"message": str(e)}, 400


@router.post("/login", tags=["Authentication"])
def login(request, payload: LoginSchema):
    user = authenticate(username=payload.username, password=payload.password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return {"token": token.key}
    else:
        raise HttpError(401, "Invalid credentials")


@router.get("/secure-endpoint", auth=AuthBearer(), tags=["Authentication"])
def secure_endpoint(request):
    return {"message": f"Hello, {request.auth.username}!"}
