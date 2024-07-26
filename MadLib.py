"""
Allows you to fill in blanks of madlibs
"""

CLEAR = "\033[2J"
RETURN = "\033[H"

with open("story.txt","r") as f:
    story = f.read()

while "<" in story:
    print(CLEAR)
    print(RETURN)
    print (f"{story}\n")
    ind1 = story.find("<")
    ind2 = story.find(">")
    new_word = input(f"Enter your {story[ind1+1:ind2]}: ")
    story = story.replace(story[ind1:ind2 + 1], new_word)

print(f"{CLEAR}{RETURN}{story}")