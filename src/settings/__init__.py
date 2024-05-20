from settings.databases import *  # noqa
from settings.jwt import *  # noqa

try:
    from settings.private import *  # noqa
except ModuleNotFoundError:
    pass
