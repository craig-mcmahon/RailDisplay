import threading
import time
import dot3k.lcd as lcd
import dot3k.backlight as bl
import dot3k.joystick as j

# Raspberry Pi - Displayotron 3000
class Displayotron:

    rail = None

    def __init__(self, rail, config=None):
        lcd.clear()
        bl.off()
        Displayotron.rail = rail
        self.config = config
        if config['use_rbg']:
            bl.use_rbg()

    # What to do on joystick up? - Show previous Journey
    @j.on(j.UP)
    def handle_up(pin):
        Displayotron.rail.journey_count -= 1
        if Displayotron.rail.journey_count < 0:
            Displayotron.rail.journey_count = 0
            threading.Thread(target=Displayotron.led_blink, args=(0, 0, 0, 255)).start()
        Displayotron.rail.update_board()
        Displayotron.rail.service_count = 0
        Displayotron.rail.display_train(Displayotron.rail.service_count)

    # What to do on joystick down? - Show next Journey
    @j.on(j.DOWN)
    def handle_down(pin):
        Displayotron.rail.journey_count += 1
        if Displayotron.rail.journey_count >= len(Displayotron.rail.config["journey"]):
            Displayotron.rail.journey_count = len(Displayotron.rail.config["journey"]) - 1
            threading.Thread(target=Displayotron.led_blink, args=(2, 0, 0, 255)).start()
        Displayotron.rail.update_board()
        Displayotron.rail.service_count = 0
        Displayotron.rail.display_train(Displayotron.rail.service_count)

    # What to do on joystick left? - Show previous Train
    @j.on(j.LEFT)
    def handle_left(pin):
        Displayotron.rail.service_count -= 1
        if Displayotron.rail.service_count < 0:
            Displayotron.rail.service_count = 0
            threading.Thread(target=Displayotron.led_blink, args=(0, 0, 0, 255)).start()
        Displayotron.rail.display_train(Displayotron.rail.service_count)

    # What to do on joystick right? - Show next Train
    @j.on(j.RIGHT)
    def handle_right(pin):
        Displayotron.rail.service_count += 1
        if Displayotron.rail.service_count >= len(Displayotron.rail.board.train_services):
            Displayotron.rail.service_count = len(Displayotron.rail.board.train_services) - 1
            threading.Thread(target=Displayotron.led_blink, args=(2, 0, 0, 255)).start()
        Displayotron.rail.display_train(Displayotron.rail.service_count)

    # What to do on joystick button press? - refresh board
    @j.on(j.BUTTON)
    def handle_button(pin):
        Displayotron.rail.service_count = 0
        Displayotron.rail.update_board()
        Displayotron.rail.display_train(0)

    @staticmethod
    def led_blink(led_id, r, g, b, sleep_time=1):
        if led_id == 0:
            bl.left_rgb(r, g, b)
        elif led_id == 1:
            bl.mid_rgb(r, g, b)
        elif led_id == 2:
            bl.right_rgb(r, g, b)
        time.sleep(sleep_time)
        if led_id == 0:
            bl.left_rgb(0, 0, 0)
        elif led_id == 1:
            bl.mid_rgb(0, 0, 0)
        elif led_id == 2:
            bl.right_rgb(0, 0, 0)

    @staticmethod
    def display_message(message):
        lcd.clear()
        lcd.write(message)

    @staticmethod
    def alert_late():
        threading.Thread(target=Displayotron.led_blink, args=(1, 255, 0, 0, 5)).start()

