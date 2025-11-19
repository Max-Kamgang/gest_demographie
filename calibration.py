X = hist[["F","F1"]].values
y = hist["pop"].values.astype(float)

coef, *_ = np.linalg.lstsq(X, y, rcond=None)
a, b = coef
hist["pred_linear"] = X @ coef

print(f"Paramètres calibrés: a={a:.3f}, b={b:.3f}")
hist