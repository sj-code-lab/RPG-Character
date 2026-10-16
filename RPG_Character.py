full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    # Validate name type
    if not isinstance(name, str):
        return 'The character name should be a string'
    
    # Validate name content
    if name == "":
        return 'The character should have a name'
    if len(name) > 10:
        return 'The character name is too long'
    if ' ' in name:
        return 'The character name should not contain spaces'
    
    # Validate stat types
    if not isinstance(strength, int):
        return 'All stats should be integers'
    elif not isinstance(intelligence, int):
        return 'All stats should be integers'
    elif not isinstance(charisma, int):
        return 'All stats should be integers'

    # Validate minimum stat values
    if strength < 1:
        return 'All stats should be no less than 1'
    elif intelligence < 1:
        return 'All stats should be no less than 1'
    elif charisma < 1:
        return 'All stats should be no less than 1'

    # Validate maximum stat values
    if strength > 4:
        return 'All stats should be no more than 4'
    elif intelligence > 4:
        return 'All stats should be no more than 4'
    elif charisma > 4:
        return 'All stats should be no more than 4'

    # Validate total stat points
    if not strength + intelligence + charisma == 7:
        return 'The character should start with 7 points'

    # Build character sheet lines
    line_1 = name
    line_2 = 'STR ' + (full_dot * strength) + (empty_dot * (10 - strength))
    line_3 = 'INT ' + (full_dot * intelligence) + (empty_dot * (10 - intelligence))
    line_4 = 'CHA ' + (full_dot * charisma) + (empty_dot * (10 - charisma))

    # Return formatted character sheet
    return line_1 + '\n' + line_2 + '\n' + line_3 + '\n' + line_4

create_character('ren', 4, 2, 1)
