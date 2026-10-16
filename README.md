# RPG Character Builder
A Python project completed as part of the freeCodeCamp curriculum. The goal was to build a function that generates an RPG character sheet with validated stats and structured visual output.

---

## What I Did
I implemented a function named `create_character` that:

- Accepts a character name, strength, intelligence, and charisma  
- Validates all inputs according to strict rules  
- Returns a four-line formatted character sheet  
- Uses full dots (●) and empty dots (○) to visually represent stat values out of ten  

This lab focused on Python fundamentals such as type checking, conditional logic, and string formatting.

---

## Tests That Had to Be Passed
The lab included **19 automated tests**, covering:

### Name Validation
- Must be a string  
- Cannot be empty  
- Cannot exceed 10 characters  
- Cannot contain spaces  

### Stat Validation
- All stats must be integers  
- Stats must be between **1 and 4**  
- Total stat points must equal **7**

### Output Requirements
- Four-line output format  
- Correct dot representation (● and ○)  

## ✅ My Solution (All Tests Passed)
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
