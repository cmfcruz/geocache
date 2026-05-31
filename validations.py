def check_parameter_existence(request, key):
    if request.args.get(key) is None:
        code = 400
        response = {
            'status': 'fail',
            'data': {
                key: 'Parameter is required.'
            }
        }
        return False, code, response
    return True, None, None


def check_comma_delimited(request, key):
    if ',' not in request.args.get(key):
        code = 400
        response = {
            'status': 'fail',
            'data': {
                key: 'Parameter should be comma delimited.'
            }
        }
        return False, code, response
    return True, None, None


def check_non_zero(value, key):
    code = 400
    response = {
            'status': 'fail',
            'data': {
                key: 'Parameter should not be empty.'
            }
        }
    if value is None:
        return False, code, response
    if len(value) < 1:
        return False, code, response
    return True, None, None


def check_numeric(value, key):
    try:
        float(value)
    except ValueError:
        code = 400
        response = {
            'status': 'fail',
            'data': {
                key: 'Parameter should be numeric.'
            }
        }
        return False, code, response
