# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from enum import Enum


class TranslationSettings(str, Enum):
    #The language code here should be in smaller case to match the user code. 
    default_language = "en"
    english_english = "en"
    english_spanish = "es"
    spanish_english = "in"
    spanish_spanish = "it"
    chinese_t = "zh-hant"
    nihongko_japanese = "ja" 
