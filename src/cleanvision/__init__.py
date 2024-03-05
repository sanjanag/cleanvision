import importlib.metadata
import sys
from typing import Any, Union

from cleanvision.imagelab import Imagelab as _Imagelab

PYTHON_VERSION_INFO = sys.version_info


def get_version() -> Union[str, Any]:
    return importlib.metadata.version("cleanvision")


__version__ = get_version()
Imagelab = _Imagelab
