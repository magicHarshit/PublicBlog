from django.utils.translation import ugettext_lazy as _
import re

#todo: customize words
CLOSE_REASONS = (
    (1, _('Duplicate Article')),
    (2, _('Article is off-topic or not relevant')),
    (3, _('too subjective and argumentative')),
    (4, _('not a real Article')),
    (5, _('Duplicate Article')),
    (6, _('Article is not relevant or outdated')),
    (7, _('Article contains offensive or malicious remarks')),
    (8, _('spam or advertising')),
    (9, _('too localized')),
)
VOTE_TYPE = (
    (+1,'VOTE_UP'),
    (0,'NEUTRAL'),
    (-1,'VOTE_DOWN')
)