from cloudant.client import Cloudant

#authenticate using an IAM API key

client = Cloudant.iam('a89ef88f-e4c3-4d63-b816-bdc4cb267519-bluemix','p5Hd4TxZ4Ab22qD5ldcAllNTLx4Ons3nZZJj0U4YgBCi',connect=True)

#create  a database using an intitlized client

my_database = client.create_database('ibm-deeplearning')