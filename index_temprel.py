hist = pd.read_csv("historique_bafoussam.csv").sort_values("year").reset_index(drop=True)
t0 = int(hist["year"].iloc[0])        # origine temporelle
hist["t"]  = hist["year"] - t0        # t=0..H
hist["F"]  = hist["t"].apply(lambda k: fib_iter(int(k)))
hist["F1"] = hist["t"].apply(lambda k: fib_iter(int(k+1)))
hist