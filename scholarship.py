def check_scholarship_conditions(result):
    if result['average_grade'] < 0 or result['average_grade'] > 4.0:
        return 'Invalid average'
    if result['credit'] < 0 or result['credit'] > 25:
        return 'Invalid creadit'
    if result['training_point'] < 0 or result['training_point'] > 100:
        return 'Invalid training point'

    if result['average_grade'] < 3.2 or result['credit'] < 16 or result['training_point'] < 90:
        return "scholarship 0%"
    if result['average_grade'] >= 3.6:
        return "scholarship 100%"
    return "scholarship 50%"
