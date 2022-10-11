def check_scholarship_conditions(result):
    if result['average_grade'] < 0 or result['average_grade'] > 4.0 or type(result['average_grade']) != float:
        return 'Invalid average'
    if result['credit'] < 0 or result['credit'] >= 25 or type(result['credit']) != int:
        return 'Invalid credit'
    if result['training_point'] < 0 or result['training_point'] > 100 or type(result['training_point']) != int:
        return 'Invalid training point'

    if result['average_grade'] < 3.2 or result['credit'] < 16 or result['training_point'] < 90:
        return "no scholarship"
    if result['average_grade'] > 3.6:
        return "scholarship 100%"
    return "scholarship 50%"

