def fib_recursive(n:int)->int:
    """Récursif naïf — ~O(phi^n). À éviter pour n>35."""
    if n <= 1: return n
    return fib_recursive(n-1) + fib_recursive(n-2)

@lru_cache(maxsize=None)
def fib_memo(n:int)->int:
    """Récursif mémoïsé — O(n), mémoire O(n)."""
    if n <= 1: return n
    return fib_memo(n-1) + fib_memo(n-2)

def fib_iter(n:int)->int:
    """Itératif — O(n), mémoire O(1)."""
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
    return a

def fib_fast_doubling(n:int)->int:
    """Fast-doubling — O(log n)."""
    def _fd(k):
        if k == 0: return (0,1)
        a,b = _fd(k>>1)
        c = a*((b<<1) - a)
        d = a*a + b*b
        return (d, c+d) if (k & 1) else (c, d)
    return _fd(n)[0]

# Vérif rapide
for k in range(12):
    assert fib_iter(k)==fib_memo(k)==fib_fast_doubling(k)
print("Fibonacci OK (iter/memo/fast-doubling). Récursif naïf valide mais lent.")