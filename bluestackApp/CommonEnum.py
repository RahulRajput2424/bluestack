class UserType:
    ENGG_MANAGER = 'EM'
    OFFICE_MANAGER = "OM"
    EMPLOYEE = "EP"

    MAX_LENGTH = 2
    CHOICES = (
        (ENGG_MANAGER, 'Engg Manager'),
        (OFFICE_MANAGER, 'Office Manager'),
        (EMPLOYEE, 'Employee'),
    )
    REPR = dict(CHOICES)

class RoomStatus:
    AVAILABLE = 'AV'
    BOOKED = "BO"

    MAX_LENGTH = 2
    CHOICES = (
        (AVAILABLE, 'Engg Manager'),
        (BOOKED, 'Office Manager'),
    )
    REPR = dict(CHOICES)

