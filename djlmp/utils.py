import json
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import jwt

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

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

# Serialize private key to PEM format
def get_private_key_pem(private_key) :

    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    private_key_str = private_key_pem.decode('utf-8')
    return private_key_str

    return private_key_pem

def create_jwt_keyset(private_key):

    # Get the public key for JWK set
    public_key = private_key.public_key()

    # Convert the public key to base64-encoded strings
    modulus = public_key.public_numbers().n.to_bytes(256, 'big').decode('utf-8')
    exponent = public_key.public_numbers().e

    # Create a JSON Web Key (JWK) set
    jwk_set = {
        "keys": [
            {
                "kty": "RSA",
                "use": "sig",
                "kid": "my-key-id",
                "n": modulus,
                "e": exponent
            }
        ]
    }

    return json.dumps(jwk_set)

if __name__ == "__main__":
    key_pair = generate_key_pair()
    private_key_pem = get_private_key_pem(key_pair);
    public_key_pem = get_public_key_pem(key_pair);

    print("Private Key:")
    print(private_key_pem)

    print("\nPublic Key:")
    print(public_key_pem)

    jwk_set = create_jwt_keyset(key_pair)
    print("\nJWT Keyset:")
    print(jwk_set)

    token = jwt.encode({}, key_pair, algorithm='RS256')
    print("\nJWT Token:")
    print(jwt_token)

