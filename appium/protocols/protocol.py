import sys

if sys.version_info >= (3, 8):
    # noinspection PyUnresolvedReferences
    from typing import Protocol
else:
    # noinspection PyUnresolvedReferences
    from typing_extensions import Protocol
