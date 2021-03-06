
FEATURE_ADDED = 0
FEATURE_IN_PROGRESS = 1
FEATURE_DELIVERED = 2
FEATURE_CLOSED = 3

FEATURE_STATUS = (
    (FEATURE_ADDED, 'Added'),
    (FEATURE_IN_PROGRESS, 'InProgress'),
    (FEATURE_DELIVERED, 'Delivered'),
    (FEATURE_CLOSED, 'CLOSED'),
)


POLICIES = 1
BILLING = 2
CLAIMS = 3
REPORTS = 4

PRODUCT_CHOICES = (
    (POLICIES, 'Policies'),
    (BILLING, 'Billing'),
    (CLAIMS, 'Claims'),
    (REPORTS, 'Reports')
)
