H = 25                            # horizon (années à partir de t0),
t = np.arange(0, H+1)

# 1) Linear-Fib calibré
Y_lin = model_linear_fib(t, a=a, b=b)

# 2) Scaled-Fib (paramètres ajustables)
Y0    = float(hist["pop"].iloc[0])
alpha = 0.8
Tref  = max(1, int(hist["t"].max()))
Y_scaled = model_scaled_fib(t, Y0=Y0, alpha=alpha, Tref=Tref)

# 3) Dynamique-cap (logistique simplifiée)
beta = 5_000.0
K    = 1_200_000.0
Y_dyn = model_dynamic_cap(t, Y0=Y0, beta=beta, K=K)

df_fore = pd.DataFrame({
    "t": t,
    "year": t0 + t,
    "Y_linear_calibrated": Y_lin,
    "Y_scaled": Y_scaled,
    "Y_dynamic_cap": Y_dyn
})
df_fore.head(10)