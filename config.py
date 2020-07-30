#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    SUBSCRIPTION_KEY = os.environ.get("SubscriptionKey", "8a09b1b978db4e8c85dcb4a2b218985d")
    # SUBSCRIPTION_REGION = os.environ.get("SubscriptionRegion", "eastasia")
