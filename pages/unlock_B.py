from bearlibterminal import terminal as blt
from pygame import mixer
import time
import config as cfg

def erroo():
    global text, frequency
    blt.set('window.size=75x35')
    blt.color('yellow')

    # O texto piscante que será exibido 
    text = "password.txt"

    # Frequencia das piscadas em segundos
    frequency = 1

    # Verifica que o usuario viu essa página
    cfg.game_state['viu_99'] = 1

    logic()

def logic():
    while True:
        blt.clear()

        blt.color('green')

        # Ativa o efeito piscante no texto selecionado
        if time.time() % frequency < frequency / 2:
            blt.print(32, 3, text)

        blt.printf(6, 0, 'EGOTEXT   << 99 >>   SEGUNDA-FEIRA - 11 DE ABRIL, 1996  22:13h')
        blt.print(15, 6, "Pressione Enter para inserir a chave de acesso.")
        blt.printf(6, 0, '[color=yellow]EGOTEXT   << 99 >>   SEGUNDA-FEIRA - 11 DE ABRIL, 1996  22:13h[/color]')
        blt.print(15, 6, "[color=yellow]Pressione Enter para inserir a chave de acesso.[/color]")
        blt.refresh()

        # Verifica se o usuario apertou alguma tecla e a lê
        if blt.has_input():

            cfg.egotext_input()

            if cfg.key == blt.TK_ENTER:
                blt.color('yellow')
                blt.print(15, 10, "> ")
                rc, senha = blt.read_str(17, 10, "", 20)

                # Se acertou:
                #if (senha == "fenix" or senha == "FENIX"):
                if senha.lower() == "fenix" or senha.lower() == "phoenix":
                    blt.print(15, 13, "SENHA CORRETA.")
                    blt.refresh()
                    blt.delay(1000)
                    from pages.finaldemo import fim
                    blt.clear()
                    cfg.clear_input_queue()
                    fim()

                # Se errou:
                else:
                    blt.print(15, 13, "SENHA INCORRETA.")
                    blt.refresh()
                    blt.delay(1000)
                    blt.clear()
                    cfg.clear_input_queue()
                    erroo()
    
            elif cfg.key == blt.TK_LEFT:
                    cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                    blt.refresh()
                    from pages.gflex import gflex
                    blt.clear()
                    cfg.clear_input_queue()
                    gflex()

            elif cfg.key == blt.TK_RIGHT:
                cfg.play_sound('sfx/sound_menu_close.ogg', volume=0.5, loop = 0)
                from pages.welcome import saudacao
                blt.clear()
                cfg.clear_input_queue()
                saudacao()

            else:
                cfg.clear_input_queue()
                logic()  

if __name__ == "__main__": 
    erroo() 