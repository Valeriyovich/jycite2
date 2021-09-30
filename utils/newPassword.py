import string
import random

import sentry_sdk
sentry_sdk.init(
    "https://4963b311c67b4e84812569fcc9224980@o518216.ingest.sentry.io/5627744",
    traces_sample_rate=1.0
)

def getRandomString(length):
    letters = string.ascii_lowercase
    resultStr = ''.join(random.choice(letters) for i in range(length))
    return (resultStr)