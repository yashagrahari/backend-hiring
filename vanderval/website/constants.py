class CustomerVolume:
    LOW = 'Low Volume'
    MEDIUM = 'Medium Volume'
    HIGH = 'High Volume'
    
    CHOICES = (
        (LOW, 'Low Volume'),
        (MEDIUM, 'Medium Volume'),
        (HIGH, 'High Volume'),
    )


class JobExecutionSpeed:
    VERY_FAST = 'Very Fast'
    FAST = 'Fast'
    MEDIUM = 'Medium'
    SLOW = 'Slow'
    VERY_SLOW = 'Very Slow'

    CHOICES = (
        (VERY_FAST, 'Very Fast'),
        (FAST, 'Fast'),
        (MEDIUM, 'Medium'),
        (SLOW, 'Slow'),
        (VERY_SLOW, 'Very Slow'),
    )
