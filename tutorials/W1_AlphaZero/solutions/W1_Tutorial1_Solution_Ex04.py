class EpsilonGreedyAgent(ArtificialPlayer):
    def __init__(self, epsilon=0.05, name=None):
        super(EpsilonGreedyAgent,
              self).__init__(name if name is not None else f"Epsilon={epsilon}")
        self.epsilon = epsilon

    def select_move(self, game:OthelloGame):
        # Evaluate all actions in all games.
        all_values, actions_tensor, actions_list = self.batch_evaluate(game,
                                                        game.current_player)
        # Initially select the best action in each game.
        chosen_action = torch.zeros(game.n_games, 2, dtype=torch.int32)
        for g in range(game.n_games):
            # If there are no moves available, pass
            if len(actions_list[g]) == 0:
                chosen_action[g, :] = -1
                continue
            if np.random.rand() < self.epsilon:
                acts = actions_list[g]
                random_choice = acts[np.random.randint(len(acts))]
                chosen_action[g, :] = torch.as_tensor(random_choice,
                                                      dtype=torch.int32)
            else:
                idx = torch.argmax(all_values[g])
                chosen_action[g, :] = actions_tensor[g, idx, :]

        return chosen_action

    def evaluate(self, game:OthelloGame, whoami:int):
        """
        Evaluation function used in "select_move" below.
        Subclasses may override evaluate() to create epsilon-greedy players
        with a different value function.
        """
        # Default to the hand-coded heuristic from above
        return my_board_value(game.boards, whoami)
    
    def batch_evaluate(self, game:OthelloGame, whoami:int):
        """Call evaluate() once per available action. Returns three things:
            - 'values' a [n_games, n_actions] tensor containing values estimated
              for each action per game.
            - 'actions_tensor' a [n_games, n_actions, 2] tensor containing the
              (row,col) coordinates of corresponding actions.
            - 'actions_list' the output of game.get_available_actions

        Handles the case of game.n_games>1 somewhat efficiently. If different
        games have different #s of actions, then n_actions is the maximum number
        of actions in any of the games. 'actions' is padded with -1 on games
        that have fewer actions (since -1 indicates "pass") and 'values' is set
        to -inf on all pass moves.
        """
        # actions_list is a list of lists of tuples. One list per game.
        actions_list = game.get_available_actions()
        num_actions_each_game = torch.as_tensor(
                                        [len(acts) for acts in actions_list])
        max_actions = num_actions_each_game.max()
        # Allocate values output
        values = float('-inf')*torch.ones(game.n_games, max_actions)
        # Create a tensor of [n_games, max_actions, 2] that contains
        # all available actions for all games, padded with -1s (pass move)
        # where games have fewer than max_actions possible actions.
        actions_tensor = -torch.ones(game.n_games, max_actions, 2,
                                     dtype=torch.int32)
        for g in range(game.n_games):
            if num_actions_each_game[g] == 0:
                continue
            actions_tensor[g, :num_actions_each_game[g], :] =\
                torch.as_tensor(actions_list[g], dtype=torch.int32)
        
        # Evaluate each action, simultaneously for all games
        for i in range(max_actions):
            state = game.copy_state()
            game.step(actions_tensor[:,i,:])
            values[:,i] = self.evaluate(game, whoami)
            values[num_actions_each_game < i+1] = float('-inf')
            game.paste_state(state)
        return values, actions_tensor, actions_list


game = OthelloGame()
agent = EpsilonGreedyAgent(epsilon=0.05)
act = agent.select_move(game)
game.step(act)
game.render()