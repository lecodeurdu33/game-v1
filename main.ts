input.onButtonPressed(Button.A, function () {
    if (joueur) {
        joueur.change(LedSpriteProperty.X, -1)
    }
})
input.onButtonPressed(Button.B, function () {
    if (joueur) {
        joueur.change(LedSpriteProperty.X, 1)
    }
})
let joueur: game.LedSprite = null
// ESQUIVE - jeu pour micro:bit (MakeCode Python)
// A = aller à gauche, B = aller à droite
// Évitez le bloc qui tombe. Plus vous avancez, plus ça va vite !
let delai = 500
// Écran de démarrage
basic.showString("GO!")
basic.pause(300)
joueur = game.createSprite(2, 4)
let bloc = game.createSprite(randint(0, 4), 0)
game.setScore(0)
basic.forever(function () {
    basic.pause(delai)
    if (bloc.get(LedSpriteProperty.Y) == 4) {
        // Le bloc est en bas : collision ou esquive réussie ?
        if (bloc.isTouching(joueur)) {
            game.gameOver()
        } else {
            game.addScore(1)
            music.playTone(523, 50)
            // Accélère le jeu (vitesse max : 150 ms)
            delai = Math.max(150, delai - 20)
            // Nouveau bloc en haut
            bloc.set(LedSpriteProperty.Y, 0)
            bloc.set(LedSpriteProperty.X, randint(0, 4))
        }
    } else {
        bloc.change(LedSpriteProperty.Y, 1)
    }
})
