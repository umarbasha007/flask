from services.post_logic import process_post_request

def process_post_controller(request_data):
    # Call the business logic to process the request
    result = process_post_request(request_data)
    return result
