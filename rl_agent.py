import numpy as np

class QLearningAgent:
    def __init__(self, actions, alpha=0.1, gamma=0.99, epsilon=0.1):
        self.q_table = {}
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def get_q_value(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def update_q_value(self, state, action, reward, next_state):
        best_next_action = max(self.actions, key=lambda a: self.get_q_value(next_state, a))
        best_next_q = self.get_q_value(next_state, best_next_action)
        old_q = self.get_q_value(state, action)
        new_q = old_q + self.alpha * (reward + self.gamma * best_next_q - old_q)
        self.q_table[(state, action)] = new_q

    def choose_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.choice(self.actions)
        else:
            return max(self.actions, key=lambda a: self.get_q_value(state, a))
