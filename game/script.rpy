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
        e "Let's use the Rickshaw!!!"
    elif transport == "cab":
        hide rickshaw
        e "Right, a cab. Obviously."

default bangles_color="" # green or red
default clips_type="" # star or bow
default earrings_type = "" #heavy or minimal
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
    
    e "We're here!!"

    hide yay
    show thinking at foreground
    e "I've been hearing about some Kashmiri bangles recently.."
    hide thinking
    show yay at foreground
    e "I wonder which ones would suit me the best!"
    show bangles pair at item_slot
    hide yay
    show thinking at foreground
    e "Green or Pink? Hmmm.."
    menu:
        "Green":
            $ bangles_color = "green"
        "Pink":
            $ bangles_color = "pink"
    hide thinking
    show good choice at foreground
    e "I'll go with the [bangles_color] ones!"

    hide bangles pair
    show clips pair at item_slot
    e "And, I also want some hair clips"

    hide good choice
    show thinking at foreground
    e "Which ones?"
    menu:
        "Bow":
            $clips_type = "bow"
        "Star":
            $clips_type = "star"
    hide thinking
    show good choice at foreground
    e "I like [clips_type]s!"
    hide clips pair
    show earrings pair at item_slot
    hide good choice
    show thinking at foreground
    e "And which earrings?"
    menu:
        "Heavy":
            $earrings_type="heavy"
        "Minimal":
            $earrings_type="minimal"
    hide thinking
    show good choice at foreground
    e "You like the [earrings_type] ones? Okie dokie!!"

    hide good choice
    show yay at foreground
    e "Lets head home!"
    hide earrings pair
    hide yay
    jump ArriveAtHome
label ArriveAtHome:
    scene bedroom
    show yay at foreground
    e "I'll show the final look"
    hide yay
    jump FinalLook
return
label FinalLook:
    scene final
    if earrings_type == "heavy":
        show earrings heavy
    elif earrings_type == "minimal":        
        show earrings minimal
    if clips_type == "star":
        show clips star
    elif clips_type=="bow":
        show clips bow
    if bangles_color == "green":
        show bangles green
    elif bangles_color == "pink":
        show bangles pink
    e "What do you think?"
