import os

JWT_SECRET = os.environ.get('JWT_SECRET', 'secret')
ALGORITHM = os.environ.get('ALGORITHM', 'HS256')
