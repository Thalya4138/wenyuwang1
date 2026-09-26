"""第 52—54 章：价值迭代、Q 学习、学习动力学后的滚动控制。仅标准库。"""
from itertools import product
import random


def transition(state, action):
    """五格链，位置 4 为终点。左/右动作，撞左边界留在原地。"""
    next_state = max(0, min(4, state + action))
    terminal = next_state == 4
    return next_state, (1.0 if terminal else -0.02), terminal


def value_iteration():
    values = [0.0] * 5
    gamma = 0.95
    for _ in range(1000):
        updated = values.copy()
        for state in range(4):
            choices = []
            for action in [-1, 1]:
                ns, reward, terminal = transition(state, action)
                choices.append(reward + (0 if terminal else gamma * values[ns]))
            updated[state] = max(choices)
        difference = max(abs(a - b) for a, b in zip(values, updated))
        values = updated
        if difference < 1e-10:
            break
    policy = []
    for state in range(4):
        def action_value(action):
            ns, r, done = transition(state, action)
            return r + (0 if done else gamma * values[ns])
        policy.append(max([-1, 1], key=action_value))
    assert policy == [1, 1, 1, 1]
    print('价值迭代：', [round(x, 5) for x in values], '动作：', policy)


def q_learning():
    rng = random.Random(9)
    q = [[0., 0.] for _ in range(5)]
    visits = [[0, 0] for _ in range(5)]
    for episode in range(5000):
        state = 0
        for step in range(100):
            if rng.random() < 0.2:
                index = rng.randrange(2)
            else:
                index = max(range(2), key=lambda i: q[state][i])
            ns, reward, done = transition(state, [-1, 1][index])
            visits[state][index] += 1
            alpha = 1.0 / visits[state][index] ** 0.6
            target = reward + (0 if done else 0.95 * max(q[ns]))
            q[state][index] += alpha * (target - q[state][index])
            state = ns
            if done:
                break
    policy = [[-1, 1][max(range(2), key=lambda i: q[s][i])] for s in range(4)]
    assert policy == [1, 1, 1, 1]
    print('Q 学习动作：', policy)


def model_predictive_control():
    rng = random.Random(10)
    # 真实动力学 x_next=x+gain*u。数据拟合增量与动作的一元回归。
    gain = 0.8
    observations = []
    for _ in range(100):
        u = rng.uniform(-1, 1)
        delta = gain * u + rng.gauss(0, 0.01)
        observations.append((u, delta))
    fitted = sum(u*d for u,d in observations) / sum(u*u for u,d in observations)
    actions = [-1., -0.5, 0., 0.5, 1.]
    x, trajectory = 3.0, [3.0]
    for _ in range(15):
        def cost(sequence):
            predicted, result = x, 0.
            for u in sequence:
                predicted += fitted * u
                result += predicted**2 + 0.1*u*u
            return result
        best = min(product(actions, repeat=4), key=cost)
        x += gain * best[0]  # 只执行第一步，下一轮用真实新观测重规划。
        trajectory.append(x)
    assert abs(x) <= 0.21
    print('真实/拟合动作增益：', gain, round(fitted, 5))
    print('滚动控制轨迹：', [round(v, 3) for v in trajectory])
    print('扩展：改变真实增益、加入时延，比较盲执行与每步重规划。')


if __name__ == '__main__':
    value_iteration()
    q_learning()
    model_predictive_control()
