from enum import Enum

class CustomerVolume(Enum):
    LOW = 'Low_Volume'
    MEDIUM = 'Medium_Volume'
    HIGH = 'High_Volume'
    
    # CHOICES = (
    #     (LOW, 'Low Volume'),
    #     (MEDIUM, 'Medium Volume'),
    #     (HIGH, 'High Volume'),
    # )


class JobExecutionSpeed(Enum):
    VERY_FAST = 'Very_Fast'
    FAST = 'Fast'
    MEDIUM = 'Medium'
    SLOW = 'Slow'
    VERY_SLOW = 'Very_Slow'

    # CHOICES = (
    #     (VERY_FAST, 'Very Fast'),
    #     (FAST, 'Fast'),
    #     (MEDIUM, 'Medium'),
    #     (SLOW, 'Slow'),
    #     (VERY_SLOW, 'Very Slow'),
    # )
