# open_source_esm
##Github repository for the lecture VU Open Source Energy System Modeling SS26.

The file main.py contains a short program, that analyses a password entered by the user and rates it according to several conditions. These conditions include: 

- length > 8 characters
use of
- uppercase letters
- lowecase letters
- digits
- symbols

Each fulfilled condition adds 1 to the total score and the password is rated according to the points:
- 'weak' score <= 2
- 'medium' score <=4
- 'strong' score = 5

Function descriptions:
- check_length()
    checks if length of string >= 8
    returns bool

- check_character_types()
    checks if string contains
    - uppercase letter
    - lowercase letter
    - digit
    - symbol
    returns list of 4 bools

- calculate_strength()
    adds +1 to the password score for every condition fulfilled
    returns score from 0-5

- generate_feedback()
    categorizes password in one of the 3 categories
    suggests to add missing conditions
    returns categorization + condition (if any are not met)



Declaration of AI usage:
ChatGPT was used to generate the contents of main.py, utils.py and test_utils.py. It was also used to understand linting error messages and identifying the issues with the code.

The link to the full chat is provided here: https://chatgpt.com/share/69b6fc20-3bc0-8010-a35e-9694f92831f6