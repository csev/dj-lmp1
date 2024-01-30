
import json

from jwcrypto.jwk import JWK  # type: ignore
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


# Adapted from:
# https://github.com/dmitry-viskov/pylti1.3/blob/master/pylti1p3/registration.py

# Generate an RSA key pair
def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    return private_key;

# Serialize public key to PEM format
def get_public_key_pem(private_key) :

    public_key = private_key.public_key()

    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    public_key_str = public_key_pem.decode('utf-8')
    return public_key_str

key_pair = generate_key_pair()
public_key_pem = get_public_key_pem(key_pair);

print("\nPublic Key:")
print(public_key_pem)

jwk_obj = JWK.from_pem(public_key_pem.encode("utf-8"))
public_jwk = json.loads(jwk_obj.export_public())
public_jwk["alg"] = "RS256"
public_jwk["use"] = "sig"
print(public_jwk);

