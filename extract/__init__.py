"""
extract  - Universal archive extraction tool for linux.
"""

__version__ = "1.0.0"

from .archive import extract_file 
from .formats import detect_format, list_supported_extensions

__all__ = ["extract_file", "detect_format", "list_supported_extensions", "__version__"]
