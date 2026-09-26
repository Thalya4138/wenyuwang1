"""第 40—49 章：最小二乘、手写反向传播、数值梯度、因果注意力。依赖 numpy。"""
import numpy as np


def sigmoid(x):
    # 本实验数据范围受控；此限制只避免 exp 溢出。
    return 1.0 / (1.0 + np.exp(-np.clip(x, -60, 60)))


def loss_and_grad(X, y, params):
    W1, b1, W2, b2 = params
    H = np.tanh(X @ W1 + b1)
    logits = H @ W2 + b2
    p = sigmoid(logits)
    loss = np.mean(np.logaddexp(0, logits) - y * logits)
    g2 = (p - y) / len(X)
    g1 = (g2 @ W2.T) * (1 - H * H)
    grads = [X.T @ g1, g1.sum(axis=0, keepdims=True),
             H.T @ g2, g2.sum(axis=0, keepdims=True)]
    return float(loss), grads, p


def gradient_check(X, y, params):
    _, grads, _ = loss_and_grad(X, y, params)
    h = 1e-5
    errors = []
    for param, analytical in zip(params, grads):
        for index in np.ndindex(param.shape):
            old = param[index]
            param[index] = old + h
            plus = loss_and_grad(X, y, params)[0]
            param[index] = old - h
            minus = loss_and_grad(X, y, params)[0]
            param[index] = old
            errors.append(abs((plus - minus) / (2 * h) - analytical[index]))
    error = max(errors)
    assert error < 1e-7, error
    return error


def linear_regression(rng):
    X = rng.normal(size=(100, 2))
    y = 2 * X[:, 0] - 3 * X[:, 1] + 1
    A = np.column_stack([X, np.ones(len(X))])
    w = np.zeros(3)
    for _ in range(1000):
        w -= 0.1 * A.T @ (A @ w - y) / len(y)
    exact = np.linalg.lstsq(A, y, rcond=None)[0]
    assert np.allclose(w, exact, atol=1e-7)
    print('回归 [w1,w2,b]：', np.round(w, 6))


def causal_attention(rng):
    X = rng.normal(size=(4, 3))
    def apply(x):
        scores = x @ x.T / np.sqrt(x.shape[1])
        forbidden = np.triu(np.ones((len(x), len(x)), dtype=bool), k=1)
        scores[forbidden] = -np.inf
        weights = np.exp(scores - scores.max(axis=1, keepdims=True))
        weights /= weights.sum(axis=1, keepdims=True)
        return weights @ x, weights
    result, weights = apply(X)
    changed = X.copy()
    changed[-1] += 100
    after, _ = apply(changed)
    assert np.allclose(result[:-1], after[:-1])
    assert np.allclose(weights.sum(axis=1), 1)
    print('因果注意力：修改未来位置未改变前三个位置的输出。')


def main():
    rng = np.random.default_rng(7)
    linear_regression(rng)
    X = np.array([[0., 0.], [0., 1.], [1., 0.], [1., 1.]])
    y = np.array([[0.], [1.], [1.], [0.]])
    params = [rng.normal(scale=0.5, size=(2, 8)), np.zeros((1, 8)),
              rng.normal(scale=0.5, size=(8, 1)), np.zeros((1, 1))]
    print('数值梯度最大绝对误差：', gradient_check(X, y, params))
    initial = loss_and_grad(X, y, params)[0]
    for _ in range(6000):
        _, grads, _ = loss_and_grad(X, y, params)
        for param, grad in zip(params, grads):
            param -= 0.1 * grad
    final, _, probabilities = loss_and_grad(X, y, params)
    assert np.array_equal(probabilities > 0.5, y.astype(bool))
    assert final < 0.03
    print(f'异或损失：{initial:.6f} -> {final:.6f}')
    print('异或概率：', probabilities.ravel().round(4))
    causal_attention(rng)
    print('实验通过。扩展：去掉 tanh，并解释为何无法正确分开异或。')


if __name__ == '__main__':
    main()
