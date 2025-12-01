import os
import django
import secrets
import string

# setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "whisper.settings")
django.setup()

from scribble.models import ScribblePointInfo

def generate_token(length=6):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

# quanti token vuoi creare
NUM_TOKENS = 12
NAMES = ['Gli innamorati', 'La fava di aronne', 'Dio cane', 'Puttana Eva', 'Culo', 'Sesso',
         'Il pipo', 'Il culino', 'La mammaccia', 'Sus', 'Dio Brando', 'Omega mr bean']
for _ in range(NUM_TOKENS):
    while True:
        token = generate_token()
        if not ScribblePointInfo.objects.filter(token=token).exists():
            ScribblePointInfo.objects.create(token=token,name=NAMES[_])
            break

print("Token generati e salvati nel DB")