# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eera")

default transport="" # "rickshaw" or "cab"

# The game starts here.
label start:
    scene bedroom
    
    transform middle:
        xalign 0.45
        yalign 0.5
        zoom 1.2

    show wave at middle
    e "Hewooo!!! Wanna go shopping together?"
    hide wave
    show thinking at middle
    e "Should we get a cab, or use a Rickshaw?"
    hide thinking
 
    show rickshaw:
        xalign 0.0
        yalign 0.5
        zoom 0.4
    show car:
        xalign 0.85
        yalign 0.5
        zoom 0.4

    menu:
        "Rickshaw":
            $ transport="rickshaw"
        "Cab":
            $ transport="cab"
    jump ChoseTransport
label ChoseTransport:

    hide cab
    hide rickshaw
    
    if transport=="rickshaw":
        show good choice at middle
        "Let's use the Rickshaw!!!"
    elif transport == "cab":
        show yay at middle
        "Right, a cab. Obviously."
return
