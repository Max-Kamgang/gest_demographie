Colaborateurs : @Max-Kamgang , @KamgaHonore , @Tiakoyann 
Ce projet avait pour objectif d’estimer la croissance urbaine de la ville de Bafoussam en utilisant des modèles inspirés de la suite de Fibonacci et de ses variantes dynamiques. Grâce à la calibration sur des données réelles (PopulationStat, 2005–2025), nous avons pu relier la logique de croissance récursive à un phénomène démographique concret.

Les résultats montrent que : • Le modèle Linear-Fib reproduit correctement la tendance générale de la population urbaine, tout en présentant quelques écarts ponctuels liés à la simplification du modèle. • L’ajout d’un intercept améliore nettement la précision de la régression et la cohérence des prévisions (hausse du R², réduction du MAE et du RMSE). • Le modèle Scaled-Fib accentue la croissance et simule des scénarios d’expansion rapide, tandis que le modèle Dynamique-Cap intègre une saturation plausible à long terme (effet de capacité maximale K).

Sur le plan algorithmique : • L’étude a permis de comparer plusieurs versions de Fibonacci (récursive, mémoïsée, itérative, fast-doubling) et de comprendre leurs complexités — de O(φⁿ) à O(log n) — démontrant l’importance de l’optimisation. • L’approche a mis en avant la puissance de la modélisation récursive pour représenter des phénomènes cumulatifs et évolutifs dans le temps.

Enfin, au-delà de la dimension mathématique, cette simulation constitue une base utile pour : • l’analyse prospective urbaine, • la planification des infrastructures, • et la gestion durable des ressources à Bafoussam.

Elle pourrait être enrichie à l’avenir par : • des données topographiques ou socio-économiques réelles (INS Cameroun, SIG), • et l’intégration d’un modèle logistique complet (Malthus/Verhulst) pour des prévisions encore plus robustes.

En résumé : la suite de Fibonacci, appliquée à la croissance urbaine, illustre parfaitement comment un concept mathématique simple peut devenir un outil de prévision et d’aide à la décision pour la planification d’une ville en pleine expansion.