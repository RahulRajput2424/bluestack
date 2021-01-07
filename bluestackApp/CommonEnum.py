class UserType:
    ADMIN = 'AD'
    ENGG_MANAGER = 'EM'
    OFFICE_MANAGER = "OM"
    EMPLOYEE = "EP"

    MAX_LENGTH = 2
    CHOICES = (
        (ADMIN, 'Admin'),
        (ENGG_MANAGER, 'Engg Manager'),
        (OFFICE_MANAGER, 'Office Manager'),
        (EMPLOYEE, 'Employee'),
    )
    REPR = dict(CHOICES)
