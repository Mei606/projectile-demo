//  setup game
info.setScore(0)
info.setLife(3)
//  setup player
let spaceship = sprites.create(img`
    . . b c c c c c c c c c b . . .
    . b 1 1 1 1 1 1 1 1 1 1 1 b . .
    . b d b c c c c c c c b d b . .
    . b d c 6 6 6 6 6 6 6 c d b . .
    . b d c 6 d 6 6 6 6 6 c d b . .
    . b d c 6 6 6 6 6 6 6 c d b . .
    . b d c 6 6 6 6 6 6 6 c d b . .
    . b d c 6 6 6 6 6 6 6 c d b . .
    . b d c c c c c c c c c d b . .
    . c b b b b b b b b b b b c . .
    . . c c c c c c c c c c c . . .
    . c d c . . c d c . . c d c . .
    . c c c . . c c c . . c c c . .
    . 4 2 4 . . 4 2 4 . . 4 2 4 . .
    . 5 4 5 . . 5 4 5 . . 5 4 5 . .
    . . 5 . . . . 5 . . . . 5 . . .
`)
spaceship.setPosition(10, scene.screenHeight() / 2)
spaceship.setFlag(SpriteFlag.StayInScreen, true)
//  set player controls
controller.moveSprite(spaceship, 200, 200)
