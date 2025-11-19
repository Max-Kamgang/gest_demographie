def model_linear_fib(t:np.ndarray, a:float, b:float)->np.ndarray:
    F  = np.array([fib_iter(int(k))   for k in t], dtype=float)
    F1 = np.array([fib_iter(int(k+1)) for k in t], dtype=float)
    return a*F + b*F1

def model_scaled_fib(t:np.ndarray, Y0:float, alpha:float, Tref:int)->np.ndarray:
    denom = max(1, fib_iter(int(Tref)))
    F = np.array([fib_iter(int(k)) for k in t], dtype=float)
    return Y0 * (1.0 + alpha * (F/denom))

def model_dynamic_cap(t:np.ndarray, Y0:float, beta:float, K:float)->np.ndarray:
    Y = np.zeros_like(t, dtype=float)
    Y[0] = Y0
    for i in range(len(t)-1):
        grow = beta * fib_iter(int(t[i]))
        Y[i+1] = Y[i] + grow * (1 - Y[i]/K)
        Y[i+1] = max(0.0, Y[i+1])
    return Y
print("Modèles définis : Linear-Fib, Scaled-Fib, Dynamique-cap.")