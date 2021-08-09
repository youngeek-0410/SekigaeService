from django.contrib.auth.backends import BaseBackend

from .firebase import *

from django.contrib.auth import get_user_model
import uuid

User = get_user_model()


class FirebaseAuthBackend(BaseBackend):  # TODO: ModelBackendとの違いを調べる
    def authenticate(self, request, **credentials):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            raise Exception("No auth token provided")

        id_token = auth_header.split(" ").pop()
        data = firebase_validation(id_token)
        user, _ = User.objects.get_or_create(
            email=data["email"], uid=data["uid"], username=data["username"])
        return user

    # TODO: get_user関数が必須とドキュメントにあったがこの実装で大丈夫か確認
    def get_user(self, user_uuid):
        try:
            return User.objects.get(pk=user_uuid)
        except User.DoesNotExist:
            return None
