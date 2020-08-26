# setup game
info.set_score(0)
info.set_life(3)

# setup player
spaceship = sprites.create(img("""
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
"""))
spaceship.set_position(10, scene.screen_height()/2)
spaceship.set_flag(SpriteFlag.StayInScreen, True)

# set player controls
controller.move_sprite(spaceship, 200, 200)

# setup enemies

# set projectiles for player
