class ValidationError(Exception):
    pass

# define metrics to be validate
def get_expected_metrics():
    return {
        "accuracy": 0.90,
        "f1_macro": 0.90,
        "f1_micro": 0.90,
        "precision": 0.90,
        "recall": 0.90
    }


# define custom validations
def custom_validate_performance(performance):

    for metric, expected in get_expected_metrics().items():
        if performance[metric] < expected:
            raise ValidationError("[{}] expected {} < {}"
                .format(metric, expected, performance[metric]))
