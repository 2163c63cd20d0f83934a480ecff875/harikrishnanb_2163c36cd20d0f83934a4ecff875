#define the base class player
class player:
  def play(self):
    print("the player is player cricket.")

# define the deived class batsman
class batsman(player):
  def play(self):
    print("the player is player batting.")

# define the deived class bowler
class bowler(player):
  def play(self):
    print("the bowler is bowling.")

#create objects of batsman and bowler classes
batsman= batsman()
bowler=bowler()
#call the play() method for each object
batsman.play()
bowler.play()

