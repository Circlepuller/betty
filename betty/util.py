def is_na(result, result_type=str, default_result='N/A'):
    return result if isinstance(result, result_type) else default_result
