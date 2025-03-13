"""
Author(s)
---------
- Pietro Ferraiuolo : written in 2025

Description
-----------
Gentle is a package for the control of the 4D PhaseCam interferometer.

How to Use:
-----------
```python
> import gentle
> interf = gentle.PhaseCam('193.206.155.218', 8011)
> img = interf.acquire_map()
```
"""

from . import analyzer
from .interferometer import PhaseCam
from .core import zernike as zern
from .utils.osutils import (
    load_fits,
    save_fits,
    getFileList,
)
from .core.root import (
    I4D_IP as _I4D_IP,
    I4D_PORT as _I4D_PORT,
    CAPTURE_FOLDER_NAME_4D_PC  as _CAPTURE_FOLDER_NAME_4D_PC,
    PRODUCE_FOLDER_NAME_4D_PC as _PRODUCE_FOLDER_NAME_4D_PC,
    PRODUCE_FOLDER_NAME_M4OTT_PC as _PRODUCE_FOLDER_NAME_M4OTT_PC,
    SETTINGS_CONF_FILE_M4OTT_PC as _SETTINGS_CONF_FILE_M4OTT_PC,
    BASE_PATH as _BASE_PATH,
    BASE_DATA_PATH as _BASE_DATA_PATH,
    OPD_IMAGES_ROOT_FOLDER as _OPD_IMAGES_ROOT_FOLDER,
    OPD_SERIES_ROOT_FOLDER as _OPD_SERIES_ROOT_FOLDER,
    LOGGING_FILE_PATH as _LOGGING_FILE_PATH,
)

class _folds():
    """Wrapper class for the folder tree of the package"""
    def __init__(self):
        self.CAPTURE_FOLDER_NAME_4D_PC = _CAPTURE_FOLDER_NAME_4D_PC
        self.PRODUCE_FOLDER_NAME_4D_PC = _PRODUCE_FOLDER_NAME_4D_PC
        self.PRODUCE_FOLDER_NAME_M4OTT_PC = _PRODUCE_FOLDER_NAME_M4OTT_PC
        self.SETTINGS_CONF_FILE_M4OTT_PC = _SETTINGS_CONF_FILE_M4OTT_PC
        self.BASE_PATH = _BASE_PATH
        self.BASE_DATA_PATH = _BASE_DATA_PATH
        self.OPD_IMAGES_ROOT_FOLDER = _OPD_IMAGES_ROOT_FOLDER
        self.OPD_SERIES_ROOT_FOLDER = _OPD_SERIES_ROOT_FOLDER
        self.LOGGING_FILE_PATH = _LOGGING_FILE_PATH
        self.I4D_IP = _I4D_IP
        self.I4D_PORT = _I4D_PORT

folders = _folds()

try:
    import os as _os
    _os.system("mount 4d && mount 4dConfig")
except Exception as e:
    raise e



__all__ = [
    'PhaseCam',
    'analyzer',
    'zern',
    'load_fits',
    'save_fits',
    'getFileList',
    'folders',
]
