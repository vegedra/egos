from bearlibterminal import terminal as blt
from pygame import mixer
from itertools import cycle
import config as cfg
import language

def erro():
    #blt.open()
    blt.set('window.size=75x20')
    blt.color('black')
    language.get_localized_text('welcome5', section='egotext', color="yellow") 
    blt.printf(20, 0, '[color=yellow]0[/color]')

    blt.printf(12, 4, '[color=#ff71ce]       ___   ___   ________  ____   ___        [/color]')
    blt.printf(12, 5, '[color=#01cdfe]      |\  \ |\  \ /\   __  \|\   \ |\  \       [/color]')
    blt.printf(12, 6, '[color=#05ffa1]      \ \  \|_\  \  \  \/\  \ \   \__\  \      [/color]')
    blt.printf(12, 7, '[color=#b967ff]       \ \_____   \  \  \ \  \ \______   \     [/color]')
    blt.printf(12, 8, '[color=#fffb96]        \|____|\   \  \  \_\  \|_____|\   \    [/color]')
    blt.printf(12, 9, '[color=#ff3f3f]              \ \___\  \_______\     \ \___\   [/color]')
    blt.printf(12, 10, '[color=#001eff]               \|___|\_|_______|      \|___|  [/color]')  

    language.get_localized_text('error', section='egotext', color="674ea7") 
    blt.refresh()

    logic()

def logic():
    # Define os frames da animação de loading
    loading_animation = cycle(['|', '/', '-', '\\'])
    blt.color('#674ea7')
      
    # Loop da animação, que roda 30 vezes  
    for i in range(15):
        blt.delay(100)
        blt.print(48, 13, next(loading_animation))
        blt.refresh()

    from pages.welcome import saudacao
    blt.clear()
    cfg.clear_input_queue()
    saudacao()

if __name__ == "__main__": 
    erro() 