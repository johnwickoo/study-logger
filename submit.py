import time
import hmac
import hashlib
import struct
import json
import base64
import urllib.request


EMAIL = "bukolafaduagba@gmail.com"
GIST_URL = "https://gist.github.com/johnwickoo/1f19d9a2fe705266ec78e2ae3ed8ac36"
SUBMIT_URL = "https://api.challenge.hennge.com/challenges/backend-recursion/004"


def generate_totp(secret: str, digits: int = 10, timestep: int = 30, t0: int = 0) -> str:
    counter = int((time.time() - t0) // timestep)
    counter_bytes = struct.pack(">Q", counter)
    secret_bytes = secret.encode("ascii")

    digest = hmac.new(secret_bytes, counter_bytes, hashlib.sha512).digest()
    offset = digest[-1] & 0x0F
    binary = struct.unpack(">I", digest[offset:offset + 4])[0] & 0x7FFFFFFF
    otp = binary % (10 ** digits)

    return str(otp).zfill(digits)


def main():
    payload = {
        "github_url": GIST_URL,
        "contact_email": EMAIL,
        "solution_language": "python",
    }

    secret = EMAIL + "HENNGECHALLENGE004"
    totp = generate_totp(secret)

    credentials = f"{EMAIL}:{totp}".encode("utf-8")
    auth_header = "Basic " + base64.b64encode(credentials).decode("ascii")

    data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        SUBMIT_URL,
        data=data,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Authorization": auth_header,
        },
    )

    with urllib.request.urlopen(request) as response:
        print("Status:", response.status)
        print(response.read().decode("utf-8"))


if __name__ == "__main__":
    main()