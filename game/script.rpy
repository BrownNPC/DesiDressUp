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
        zoom 2

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

    show good choice at middle
    if transport=="rickshaw":
        hide car
        "Let's use the Rickshaw!!!"
    elif transport == "cab":
        hide rickshaw
        "Right, a cab. Obviously."

default bangles_color="" # green or red

label ArriveAtMarket:
    scene market

    transform foreground:
        xalign 0.75
        yalign 1.2
        zoom 1.9
    
    transform item_slot:
        xalign 0.25
        yalign 0.5
        zoom 0.3
    
    show yay at foreground
    
    "We're here!!"

    hide yay
    show thinking at foreground
    "I've been hearing about some Kashmiri bangles recently.."
    hide thinking
    show yay at foreground
    "I wonder which ones would suit me the best!"
    show bangles pair at item_slot
    hide yay
    show thinking at foreground
    "Green or Red? Hmmm.."
    menu:
        "Green":
            $ bangles_color = "green"
        "Red":
            $ bangles_color = "red"
    hide thinking
    show good choice at foreground
    "I'll go with the [bangles_color] ones!"
return
