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
    play sound "show.ogg"
    hide wave
    show thinking at middle
    e "Should we get a cab, or use a Rickshaw?"
    play sound "show.ogg"
    
    hide thinking
    show rickshaw:
        xalign 0.3
        yalign 0.5
        anchor (0.5, 0.5)
        rotate -15
        zoom 0.35
        linear 1.5 rotate 15
        linear 1 rotate -15
        repeat
    show car:
        xalign 0.7
        yalign 0.5
        xanchor 0.5
        yanchor 0.5
        zoom 0.4
        linear 1.2 rotate 15
        linear 1.5 rotate -15
        repeat

    menu:
        "Rickshaw":
            $ transport="rickshaw"
        "Cab":
            $ transport="cab"
    play sound "select.ogg"
    jump ChoseTransport
label ChoseTransport:

    show good choice at middle
    if transport=="rickshaw":
        hide car
        e "Let's use the Rickshaw!!!"
        play sound "show.ogg"
        play sound "rickshaw.ogg" volume 4.0
    elif transport == "cab":
        hide rickshaw
        e "Right, a cab. Obviously."
        play sound "car.ogg" volume 4.0
        play sound "show.ogg"

default bangles_color="" # green or red
default clips_type="" # star or bow
default earrings_type = "" #desi or heavy
label ArriveAtMarket:
    scene market

    transform foreground:
        xalign 0.75
        yalign 1.2
        zoom 1.9
    
    transform item_slot:
        xalign 0.25
        yalign 0.5
        zoom 0.2
        linear 1.2 rotate 15
        linear 1.5 rotate -15
        repeat
    
    show yay at foreground
    e "We're here!!"
    play sound "show.ogg"

    hide yay
    show thinking at foreground
    e "I've been hearing about some Kashmiri bangles recently.."
    play sound "show.ogg"
    hide thinking
    show yay at foreground
    play sound "show.ogg"
    e "I wonder which ones would suit me the best!"
    show bangles pair at item_slot
    hide yay
    show thinking at foreground
    e "Green or Pink? Hmmm.."
    play sound "show.ogg"
    menu:
        "Green":
            $ bangles_color = "green"
        "Pink":
            $ bangles_color = "pink"
    hide thinking
    play sound "select.ogg"
    show good choice at foreground
    e "I'll go with the [bangles_color] ones!"
    play sound "show.ogg"

    hide bangles pair
    e "And, I also want some hair clips"
    play sound "show.ogg"

    hide good choice
    show thinking at foreground
    show clips pair at item_slot
    e "Which ones?"
    play sound "show.ogg"
    menu:
        "Bow":
            $clips_type = "bow"
        "Star":
            $clips_type = "star"
    hide thinking
    show good choice at foreground
    e "I like [clips_type]s!"
    play sound "show.ogg"
    hide clips pair
    show earrings pair at item_slot
    hide good choice
    show thinking at foreground
    e "And which earrings?"
    play sound "show.ogg"
    menu:
        "Desi":
            $earrings_type="desi"
        "Heavy":
            $earrings_type="heavy"
    hide thinking
    show good choice at foreground
    e "You like the [earrings_type] ones? Okie dokie!!"
    play sound "show.ogg"
    hide good choice
    show yay at foreground
    e "Lets head home!"
    play sound "show.ogg"
    hide earrings pair
    hide yay
    jump ArriveAtHome
label ArriveAtHome:
    scene bedroom
    show yay at foreground
    e "I'll show the final look"
    play sound "show.ogg"
    hide yay
    jump FinalLook
return
label FinalLook:
    scene final
    if earrings_type == "desi":
        show earrings desi
    elif earrings_type == "heavy":        
        show earrings heavy
    if clips_type == "star":
        show clips star
    elif clips_type=="bow":
        show clips bow
    if bangles_color == "green":
        show bangles green
    elif bangles_color == "pink":
        show bangles pink
    e "What do you think?"
    play sound "show.ogg"
