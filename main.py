# ESQUIVE - jeu pour micro:bit (MakeCode Python)
# A = aller à gauche, B = aller à droite
# Évitez le bloc qui tombe. Plus vous avancez, plus ça va vite !

delai = 500
joueur: game.LedSprite = None
bloc: game.LedSprite = None

def on_button_pressed_a():
    if joueur:
        joueur.change(LedSpriteProperty.X, -1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    if joueur:
        joueur.change(LedSpriteProperty.X, 1)
input.on_button_pressed(Button.B, on_button_pressed_b)

# Écran de démarrage
basic.show_string("GO!")
basic.pause(300)

joueur = game.create_sprite(2, 4)
bloc = game.create_sprite(randint(0, 4), 0)
game.set_score(0)

def on_forever():
    global delai
    basic.pause(delai)
    if bloc.get(LedSpriteProperty.Y) == 4:
        # Le bloc est en bas : collision ou esquive réussie ?
        if bloc.is_touching(joueur):
            game.game_over()
        else:
            game.add_score(1)
            music.play_tone(523, 50)
            # Accélère le jeu (vitesse max : 150 ms)
            delai = max(150, delai - 20)
            # Nouveau bloc en haut
            bloc.set(LedSpriteProperty.Y, 0)
            bloc.set(LedSpriteProperty.X, randint(0, 4))
    else:
        bloc.change(LedSpriteProperty.Y, 1)
basic.forever(on_forever)
