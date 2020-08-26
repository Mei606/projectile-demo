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


def on_update_interval():
    meteor = sprites.create(img("""
    . . . . . . . . . c c 8 . . . .
    . . . . . . 8 c c c f 8 c c . .
    . . . c c 8 8 f c a f f f c c .
    . . c c c f f f c a a f f c c c
    8 c c c f f f f c c a a c 8 c c
    c c c b f f f 8 a c c a a a c c
    c a a b b 8 a b c c c c c c c c
    a f c a a b b a c c c c c f f c
    a 8 f c a a c c a c a c f f f c
    c a 8 a a c c c c a a f f f 8 a
    . a c a a c f f a a b 8 f f c a
    . . c c b a f f f a b b c c 6 c
    . . . c b b a f f 6 6 a b 6 c .
    . . . c c b b b 6 6 a c c c c .
    . . . . c c a b b c c c . . . .
    . . . . . c c c c c c . . . . .
    """))
    meteor.set_position(scene.screen_width(), randint(0, scene.screen_height()))
    meteor.set_velocity(-50, 0)
game.on_update_interval(750, on_update_interval)

# set projectiles for player
