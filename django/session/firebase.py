# Create your views here.
import firebase_admin
from firebase_admin import credentials, auth
import os

cred = credentials.Certificate({
    "type": "service_account",
    "project_id": os.getenv('FIREBASE_PROJECT_ID'),
    "private_key_id": os.environ.get('FIREBASE_PRIVATE_KEY_ID'),
    "private_key": os.environ.get('FIREBASE_PRIVATE_KEY').replace('\\n', '\n'),
    "client_email": os.environ.get('FIREBASE_CLIENT_EMAIL'),
    "client_id": os.environ.get('FIREBASE_CLIENT_ID'),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://accounts.google.com/o/oauth2/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": os.environ.get('FIREBASE_CLIENT_CERT_URL')
})

default_app = firebase_admin.initialize_app(cred)


def firebase_validation(id_token):
    """
    This function receives id token sent by Firebase and
    validate the id token then check if the user exist on
    Firebase or not if exist it returns True else False
    """
    try:
        decoded_token = auth.verify_id_token(id_token, check_revoked=True)
    except auth.RevokedIdTokenError:
        raise Exception("Your auth token expired")
    except Exception:
        raise Exception("invalid auth token")

    try:
        # firebaseから取得してきた情報からuidを取り出す
        uid = decoded_token['uid']
        # uidを使って該当のユーザーデータを取得する
        fetch_user = auth.get_user(uid)
        # Firebaseから取得してきたデータは特殊なのでvarsで変換する
        dict_userData = vars(fetch_user)
        # varsで変換すると辞書型になるので任意のデータにアクセスする
        test = dict_userData['_data']['providerUserInfo']
        # 辞書型から任意の指定したデータを取り出すためにリスト内表記でfor文とget()を使う
        provider = [d.get('providerId')
                    for d in test if d.get('providerId')]
        # ソーシャルログインに使ったプロパイダ名
        provider = str(provider[0])
        # username持ってくる
        username = [d.get('displayName')
                    for d in test if d.get('displayName')]
        email = [d.get('email')
                 for d in test if d.get('email')]
        email = str(email[0])
        username = str(username[0])
        return {"username": username, "provider": provider, "email": email, "uid": uid}
    except Exception:
        raise Exception("firebase error")
