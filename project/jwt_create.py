#!/usr/bin/env python3
import datetime
# pip3 install PyJWT
import jwt
import sys
import config 


#from jwt.contrib.algorithms.pycrypto import RSAAlgorithm
#jwt.register_algorithm('RS256', RSAAlgorithm(RSAAlgorithm.SHA256))
#jwt.encode(claim, private_key, algorithm='RS256')




if len(sys.argv) != 2:
    print("Usage: jwt_create.py <private_key_file>")
    sys.exit(1)

private_key_file = sys.argv[1]


project_id = config.google_cloud_config['project_id']
algorithm = "RS256"

token = {
    # The time that the token was issued at
    "iat": datetime.datetime.now(tz=datetime.timezone.utc),
    # The time the token expires.
    "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(minutes=120),
    # The audience field should always be set to the GCP project id.
    "aud": project_id,
}

# Read the private key file.
with open(private_key_file, "r") as f:
    private_key = f.read()

print(
    "Creating JWT using {} from private key file {}".format(
        algorithm, private_key_file
    )
)

print("jwt = '{}'".format(jwt.encode(token, private_key, algorithm=algorithm)))
