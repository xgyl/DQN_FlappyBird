import game.wrapped_flappy_bird as game
import tensorflow as tf
import DQN_brain

game_state = game.GameState()
while True:
    game_state.run_game()
    if game_state.userPlay:
        game_state.user_play()
    else:
        sess = tf.InteractiveSession()
        s, readout, h_fc1 = DQN_brain.createNetwork()
        DQN_brain.trainNetwork(s, readout, h_fc1, sess)



