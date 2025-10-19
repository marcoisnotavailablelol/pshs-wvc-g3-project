"""Application layer for pesoIQ.

Exposes the `main` entrypoint used by both `python -m pesoIQ` and the
root `main.py` shim.
"""

from .run import main

__all__ = ["main"]

