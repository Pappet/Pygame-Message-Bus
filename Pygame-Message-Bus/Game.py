from Functions import *
from MessageBus import *
import pygame
import sys
import PyCon

# SETTINGS
# How big should the Window be???
ScreenWidth = 1024
ScreenHeight = 768
ScreenSize = (ScreenWidth, ScreenHeight)
# How fast should the Game run?
FPS = 60


class Game:
    # Initialise The Game
    def __init__(self):
        # Is the Game running
        self.running = True
        # Initialise Pygame and the Sound Mixer
        pygame.init()
        # Generate a Screen to Display stuff
        self.screen = pygame.display.set_mode((ScreenWidth, ScreenHeight), pygame.RESIZABLE)
        # get an infoObject about the Display
        self.infoObject = pygame.display.Info()
        # Initialise the Clock to limit the Gamespeed
        self.clock = pygame.time.Clock()
        # Initialise the Message Bus System
        self.message_bus = Message_Queue()
        # Initialise the CMD Console
        self.console = PyCon.PyCon(self.screen,
                                   (0, 0, ScreenWidth, ScreenHeight / 4),
                                   functions={"fps": self.get_fps,
                                              "size": self.get_screen_dimensions,
                                              "shutdown": self.shutdown,
                                              "add": add,
                                              "draw": draw,
                                              "pi": pi,
                                              "msg": self.message_bus.create_message},
                                   key_calls={},
                                   vari={"A": 100, "B": 200, "C": 300},
                                   syntax={re_function: console_func}
                                   )

    # The Whole Game
    # Does it need anything else?
    def run(self):
        # THE GAMELOOP
        while self.running:
            self.clock.tick(FPS)
            eventlist = pygame.event.get()
            self.message_bus.dispatch_messages()
            self.screen.fill((255, 255, 255))
            self.console.process_input(eventlist)
            self.events(eventlist)
            self.console.draw()
            pygame.display.flip()
        self.close()

    def on_message(self, msg):
        self.console.output(msg)
        if msg.type is "print":
            print("Game got a msg!!!!!!!")

    # The Events, like Key pressed and stuff
    def events(self, eventlist):
        for event in eventlist:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.console.set_active()
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key is pygame.K_m:
                    self.message_bus.create_message(self.console, self, "print", "WHATS UP")

    def close(self):
        # Close the Game
        self.console.write_history_to_file()
        pygame.quit()
        sys.exit()

    # Function for the communication with the console!
    # DEPENDED on the Game Class
    def get_fps(self):
        """ Shows the FPS! Use: fps"""
        return self.clock.get_fps()

    # Test Function for the communication with the console!
    # DEPENDED on the Game Class
    def get_screen_dimensions(self):
        """ Shows Window Resolution! Use: size"""
        return self.infoObject.current_w, self.infoObject.current_h

    # Test Function for the communication with the console!
    # DEPENDED on the Game Class
    def shutdown(self):
        """CAVE: Shuts the Game Down!!! Use: shutdown"""
        self.running = False

if __name__ == "__main__":
    game = Game()
    game.run()
