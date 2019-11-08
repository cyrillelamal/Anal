from l1_measurement_errors.errors import count_errors


VALUES = [14.85, 14.80, 14.79, 14.84, 14.81]
PRECISION = 5

X0 = 14.80
TA = 2.570


# All is done here
count_errors(VALUES, PRECISION, X0, TA)
