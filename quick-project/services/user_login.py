def user_login_check(request_data):
    # Process the request data
    # ...
    # Return the processed result
    respData = {}
    if(request_data['password'] == "rock"):
        respData = {
            'message': 'Data processed successfully',
            "username" : request_data["username"],
            "stats_code" : 200
        }
    else :
        respData = {
            'message': 'Data not found',
            "username" : request_data["username"],
            "stats_code" : 404
        }

    return respData