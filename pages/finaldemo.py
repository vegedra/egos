from bearlibterminal import terminal as blt
from pygame import mixer
import config as cfg
import language

def fim():
    blt.set('window.size=75x35')
    
    # OST
    cfg.play_music('bgm/credits.ogg', volume=0.7, loop=-1, crossfade_duration=100)

    cfg.game_state['finaldemo'] = 1

    logic()
    
def logic():
    while True:
        blt.color('black')
        language.get_localized_text('welcome5', section='egotext', color="#yellow") 
        blt.printf(20, 0, '0')
    
        blt.printf(11, 4, '[color=#ff71ce]       ___   ___   ________  ____   ___        [/color]')
        blt.printf(11, 5, '[color=#01cdfe]      |\  \ |\  \ /\   __  \|\   \ |\  \       [/color]')
        blt.printf(11, 6, '[color=#05ffa1]      \ \  \|_\  \  \  \/\  \ \   \__\  \      [/color]')
        blt.printf(11, 7, '[color=#b967ff]       \ \_____   \  \  \ \  \ \______   \     [/color]')
        blt.printf(11, 8, '[color=#fffb96]        \|____|\   \  \  \_\  \|_____|\   \    [/color]')
        blt.printf(11, 9, '[color=#ff3f3f]              \ \___\  \_______\     \ \___\   [/color]')
        blt.printf(11, 10, '[color=#001eff]               \|___|\_|_______|      \|___|  [/color]')  

        language.get_localized_text('finaldemo1', section='egotext', color="#674ea7") 
        language.get_localized_text('finaldemo2', section='egotext', color="#674ea7") 
        language.get_localized_text('finaldemo3', section='egotext', color="#674ea7") 
        language.get_localized_text('finaldemo4', section='egotext', color="#674ea7") 
        language.get_localized_text('finaldemo5', section='egotext', color="#674ea7") 
        language.get_localized_text('finaldemo6', section='egotext', color="#674ea7") 
        language.get_localized_text('finaldemo7', section='egotext', color="#674ea7") 
        language.get_localized_text('finaldemo8', section='egotext', color="#674ea7") 
        blt.refresh()

        if blt.has_input():
            key = blt.read()
            
            if key != -1:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                blt.refresh()
                from desktop.desktop import terminal
                blt.clear()
                terminal() 

if __name__ == "__main__": 
    fim() 