from GuessGame import guess_game
from CurrencyRouletteGame import currency_roulette_game
from MemoryGame import memory_game
from Common import common

class game_manager(common):
  def __init__(self):
      self.games = []
      self.text_menu = ''
      self.create_games_obj()
      self.create_menu()

  def create_games_obj(self):
    new_game = guess_game()
    self.games.append(new_game)
    new_game = memory_game()
    self.games.append(new_game)
    new_game = currency_roulette_game('Currency Roulette - try and guess the value of a random amount of USD in ILS')
    self.games.append(new_game)

  def create_menu(self):
    self.text_menu = "Please choose a game to play:\n"
    index = 0
    for games in self.games:
      index += 1
      new_line = index.__str__() + '. ' + games.get_menu() + '\n'
      self.text_menu += new_line

  def play_game(self, game_obj, difficulty):
    print(game_obj.play(difficulty= difficulty))

  def show_main_menu(self):
    self.clean_screen()
    game_number = self.start_validate_input(message=self.text_menu, val_from_value=1, val_to_value=3)
    difficulty_number = self.start_validate_input("Please choose game difficulty from 1 to 5: ", val_from_value=1, val_to_value=5)
    self.clean_screen()
    self.play_game(self.games[game_number-1], difficulty_number)

  def welcome(self, name):
    return "Hello " + name + " and welcome to the World of Games(WoG).\nHere you can find many cool games to play."