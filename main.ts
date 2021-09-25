let place = 0
let school: Image = null
input.onButtonPressed(Button.A, function () {
    basic.showString("A Minor Autumn")
    for (let index = 0; index < 2; index++) {
        music.playMelody("G B A G C5 B A B ", 120)
    }
    // ending
    music.playTone(440, music.beat(BeatFraction.Breve))
})
input.onGesture(Gesture.Shake, function () {
    for (let index = 0; index < 4; index++) {
        basic.showArrow(ArrowNames.North)
        basic.showArrow(ArrowNames.NorthEast)
        basic.showArrow(ArrowNames.East)
        basic.showArrow(ArrowNames.SouthEast)
        basic.showArrow(ArrowNames.South)
        basic.showArrow(ArrowNames.SouthWest)
        basic.showArrow(ArrowNames.West)
        basic.showArrow(ArrowNames.NorthWest)
    }
    basic.showArrow(ArrowNames.North)
    basic.pause(2000)
    for (let index = 0; index < 4; index++) {
        basic.showLeds(`
            . . # . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . # .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . #
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . #
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . # .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . # . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            # . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . . . . .
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        basic.showLeds(`
            . # . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
    }
    basic.clearScreen()
    place = randint(1, 3)
    if (place == 1) {
        basic.showLeds(`
            . . # . .
            . # # # .
            # # # # #
            # # # # #
            # # # # #
            `)
        music.playMelody("C D E F G A B C5 ", 120)
        music.playMelody("B A G F E D C - ", 120)
    } else if (place == 2) {
        school = images.createBigImage(`
            . # # # # # # # # .
            # # # # # # # # # #
            # # # # # # # # # #
            # # # # # # # # # #
            # # # # # # # # # #
            `)
        school.scrollImage(1, 200)
        for (let index = 0; index < 4; index++) {
            music.playMelody("C - C - C5 - C5 - ", 300)
        }
    } else {
        basic.showString("?")
        music.playMelody("E B C5 A B G A F ", 120)
    }
})
