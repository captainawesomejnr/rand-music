place = 0

def on_button_pressed_a():
    basic.show_string("A Minor Fall")
    for index in range(2):
        music.play_melody("G B A G C5 B A B ", 120)
    music.play_tone(440, music.beat(BeatFraction.BREVE))
    basic.pause(2000)
    basic.show_string("Harvest Dance")
    for index2 in range(2):
        music.play_melody("E - E - E - E - ", 120)
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        music.play_tone(349, music.beat(BeatFraction.WHOLE))
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(247, music.beat(BeatFraction.WHOLE))
        music.play_tone(220, music.beat(BeatFraction.WHOLE))
    for index3 in range(2):
        music.play_tone(247, music.beat(BeatFraction.WHOLE))
        music.play_tone(247, music.beat(BeatFraction.HALF))
        music.play_tone(262, music.beat(BeatFraction.HALF))
        music.play_tone(247, music.beat(BeatFraction.WHOLE))
        music.play_tone(247, music.beat(BeatFraction.WHOLE))
        music.play_tone(247, music.beat(BeatFraction.HALF))
        music.play_tone(262, music.beat(BeatFraction.HALF))
        music.play_tone(247, music.beat(BeatFraction.WHOLE))
        music.play_tone(349, music.beat(BeatFraction.WHOLE))
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(247, music.beat(BeatFraction.WHOLE))
        music.play_tone(247, music.beat(BeatFraction.WHOLE))
    for index4 in range(2):
        music.play_melody("E - E - E - E - ", 120)
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        music.play_tone(349, music.beat(BeatFraction.WHOLE))
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(247, music.beat(BeatFraction.WHOLE))
        music.play_tone(220, music.beat(BeatFraction.WHOLE))
    for index5 in range(2):
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(247, music.beat(BeatFraction.WHOLE))
        music.play_tone(220, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global place
    for index6 in range(4):
        basic.show_arrow(ArrowNames.NORTH)
        basic.show_arrow(ArrowNames.NORTH_EAST)
        basic.show_arrow(ArrowNames.EAST)
        basic.show_arrow(ArrowNames.SOUTH_EAST)
        basic.show_arrow(ArrowNames.SOUTH)
        basic.show_arrow(ArrowNames.SOUTH_WEST)
        basic.show_arrow(ArrowNames.WEST)
        basic.show_arrow(ArrowNames.NORTH_WEST)
    basic.show_arrow(ArrowNames.NORTH)
    basic.pause(2000)
    for index7 in range(4):
        basic.show_leds("""
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . # .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . #
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . #
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . # .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . # . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . . . . .
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        basic.show_leds("""
            . # . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
    basic.clear_screen()
    place = 1
    if place == 1:
        basic.show_leds("""
            . . # . .
            . # # # .
            # # # # #
            # # # # #
            # # # # #
            """)
        music.play_melody("C D E F G A B C5 ", 120)
        music.play_melody("B A G F E D C - ", 120)
    elif place == 2:
        basic.show_string("school")
        music.play_melody("C C C5 C5 C C C5 C5 ", 120)
    else:
        pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
