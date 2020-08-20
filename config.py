#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os
import sys 
from termcolor import colored, cprint 
import colored as pycolor
""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    SUBSCRIPTION_KEY = os.environ.get("SubscriptionKey", "8a09b1b978db4e8c85dcb4a2b218985d")
    # SUBSCRIPTION_REGION = os.environ.get("SubscriptionRegion", "eastasia")

""" Color Config """
class ColorFunctions():
    def red(self, txt):
        text = colored(txt, 'red')
        print(text, end="")
        return " "
        
    def yellow(self, txt):
        text = colored(txt, 'yellow')
        print(text, end="")
        return " "

    def magenta(self, txt):
        text = colored(txt, 'magenta')
        print(text, end="")
        return " "

    def green(self, txt):
        text = colored(txt, 'green')
        print(text, end="")
        return " "

    def cyan(self, txt):
        text = colored(txt, 'cyan')
        print(text, end="")
        return " "

    def blue(self, txt):
        text = colored(txt, 'blue')
        print(text, end="")
        return " " 
    
    def orange(self, txt):
        orange = pycolor.fg(202)
        default = pycolor.fg('white')
        print(f'{orange}{txt}{default}')
        return " " 
        
    def red_function(self, txt):
        text = colored(txt, 'red')
        return text
        
    def yellow_function(self, txt, color = 'yellow'):
        text = colored(txt, color)
        return text

    def magenta_function(self, txt, color = 'magenta'):
        text = colored(txt, color)
        return text

    def green_function(self, txt, color = 'green'):
        text = colored(txt, color)
        return text

    def blue_function(self, txt, color='blue'):
        text = colored(txt, color)
        return text

    def cyan_function(self, txt, color='cyan'):
        text = colored(txt, color)
        return text

    def orange_function(self, txt):
        orange = pycolor.fg(202)
        default = pycolor.fg("white")
        text = f"{orange}{txt}{default}"
        return text

    def color_function(self, txt, color):
        text = colored(txt, color)
        return text