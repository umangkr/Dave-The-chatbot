import random
import os
from win_text_to_speech import talk

def joke():
    jk1 = """Doctor-I am sorry but you suffer from a terminal illness and have only 10 to live.
            Patient-What do you mean, 10? 10 what? Months? Weeks?!
            Doctor-Nine."""

    jk2 = '''Patient-Doctor, I think that I have been bitten by a vampire.
            Doctor- Drink this glass of water.
            Patient- Will it make me better?
            Doctor- No,but I will be able to see if your neck leaks. '''

    jk3 = '''Teacher- Did your father help your with your homework?
            Student- No, he did it all by himself. '''

    jk4 = '''Man said to God - Why did you make women so beautiful?
            God said to man - So that you will love them.
            Man said to God - But why did you make them so dumb?
            God said to man - So that they will love you.'''

    list1 = [jk1, jk2, jk3, jk4]
    rand = random.choice(list1)
    print('bot-->>'+rand)
    talk(rand)