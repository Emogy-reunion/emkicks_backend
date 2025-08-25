'''
creates custom form validators to handle edge cases
'''
import re
from wtforms.validators import ValidationError


NO_EMOJI_PATTERN = re.compile(r'^[\u0020-\u007E\u00A0-\u00FF]+$')

def no_emoji(form, field):
    '''
    ensures users cannot input emojis
    Allows letters, numbers, and standard punctuation.
    '''
    if field.data and not NO_EMOJI_PATTERN.match(field.data):
            raise ValidationError("Emojis are not allowed")


