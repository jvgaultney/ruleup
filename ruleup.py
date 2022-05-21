# RuleUp module
# 2022.05.21 Initial version - VG
# Scale is 10 pixels per mm

import math

layouts = {
    'A4L': { 'page': { 'height' : 2100, 'width': 2970 }, 'frame': { 'top' : 200, 'right': 200, 'bottom': 200, 'left': 200 } },   # A4 portrait, 20mm frame margins
}

class Canvas:
    def __init__(self, **kwargs):
        settings = {
            'pageheight': 2970,
            'pagewidth': 2100,
            'frame': { 'top' : 0, 'right': 0, 'bottom': 0, 'left': 0 }
        }
        settings.update(kwargs)
        for key, value in settings.items():
            self.__setattr__(key, value)

    def xset(self):
        pass
