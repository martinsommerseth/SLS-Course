Installations:
1. Install node js https://nodejs.org/en/download/
2. npm install -g serverless

Deployment:
1. Make sure you have an aws account with a user that has Admin roles and add the credentials for this user
 to .aws/credentials with the name serverless-user
2. Run bash script sh deploy.sh

Test:
Run a POST request against the deployed API with the api key that is provided
Data contract for the body:
{
    "weights": [
        48,
        30,
        19
    ],
    "items": [
        0,
        1,
        2
    ],
    "bins": [
        0,
        1,
        2
    ],
    "bin_capacity": 100
}