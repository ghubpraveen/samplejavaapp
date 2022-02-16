from util import get_message

def lambda_handler(event, context):
    print("Hi")
    return get_message()

# import json
#
#
# def lambda_handler(event, context):
#     print("Hello")
#     return {
#         "statusCode": 200,
#         "body": json.dumps({
#             "message": "Welcome to K9",
#         }),
#     }
