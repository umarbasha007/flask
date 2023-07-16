from services.user_login import user_login_check

def user_login_controller(request_data):
    # Call the business logic to process the request
    #request validation
    result = user_login_check(request_data)
    return result