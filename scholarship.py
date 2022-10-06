def check_scholarship_conditions(summary):
    if summary['average_grade'] < 0 or summary['average_grade'] > 4.0:
        return 'Invalid average'
    if summary['credit'] <0:
        return 'Invalid creadit'
    if summary['trainning_point'] <0:
        return 'Invalid trainning point'

    if summary['average_grade'] < 3.2 or summary['credit'] < 14 or summary['trainning_point'] < 90:
        return "scholarship 0%"
    if summary['average_grade'] >= 3.6:
        return "scholarship 100%" 
    return "scholarship 50%"
