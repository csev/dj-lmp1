import json
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import jwt

def generate_key():
    # Generate an RSA private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    # Serialize the private key
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    # Convert the private key to string
    private_key_str = private_key_pem.decode('utf-8')

    # return private_key_str
    return private_key

def create_jwt_keyset():
    # Generate a key
    private_key = generate_key()

    # Get the public key for JWK set
    public_key = private_key.public_key()
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

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

    # Create a JWT using PyJWT
    token = jwt.encode({}, private_key, algorithm='RS256')

    return private_key, json.dumps(jwk_set), token

if __name__ == "__main__":
    private_key, jwk_set, jwt_token = create_jwt_keyset()

    print("Private Key:")
    print(private_key)

    print("\nJWT Keyset:")
    print(jwk_set)

    print("\nJWT Token:")
    print(jwt_token)


