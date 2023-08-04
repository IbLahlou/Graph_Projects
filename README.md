# Graph_Projects
Projet de Recherche Opérationnelle pour trouver le plus court chemin 

## 1 - Problème de plus court chemin
Soit $G=(S,A)$ un graphe, avec deux sommets distingués $s$ (la source ou l'origine) et $t$ (le but ou le puits);
On note $w(i,j)$ le coût de l'arc $(i,j)$.
On considère le programme linéaire en les variables $x_{ij}$ suivant :

Minimiser $\sum\limits_{ij \in A} w(i,j)x_{ij}$

Sous contrainte : 
$\forall i,j \in \mathbb{R} \quad x_{ij} \geq 0$

$$\sum_jx_{ij} - \sum_jx_{ji} =
\begin{cases}
  1 & \text{si } i = s \\
  0 & \text{si } i = t \\
  -2 & \text{sinon}
\end{cases}$$

![image](https://github.com/IbLahlou/Graph_Projects/assets/105231126/fdb71616-f4f1-4d4c-8bf5-707159817593)

![dijkstra](https://github.com/IbLahlou/Graph_Projects/assets/105231126/cafe0c66-740c-4e8d-bb14-4b78e972a3d7)

## 2 - Algorithme de ford-fulkerson
Le problème du flot maximal dans un graphe peut être résolu efficacement à l'aide de l'algorithme de Ford-Fulkerson. Cet algorithme utilise la recherche de chemin augmentant dans le graphe résiduel pour trouver le flot maximal entre un sommet source $s$ et un sommet puits $t$. L'idée principale est d'augmenter le flot le long d'un chemin améliorant tant que cela est possible.

L'algorithme de Ford-Fulkerson repose sur la mise à jour des capacités résiduelles des arêtes, et il peut être formulé par l'équation suivante :

$$C_f(u, v) = C(u, v) - f(u, v)$$

où $C_f(u, v)$ est la capacité résiduelle de l'arc $(u, v)$, $C(u, v)$ est la capacité originale de cet arc, et $f(u, v)$ est le flot actuel circulant sur l'arc.

L'algorithme itératif continue à trouver de nouveaux chemins augmentants jusqu'à ce qu'il n'y ait plus de chemin possible dans le graphe résiduel. Une fois qu'aucun chemin augmentant n'est trouvé, le flot maximal est atteint.

![FordFulkersonDemo](https://github.com/IbLahlou/Graph_Projects/assets/105231126/81bfd14e-8652-4b39-a385-ab3fed58d510)

## 3 - Algorithme Hangroise
L'algorithme Hangroise est une méthode itérative pour résoudre le problème du plus court chemin dans un graphe pondéré. Il peut être utilisé pour trouver le plus court chemin entre un sommet source $s$ et tous les autres sommets du graphe. L'algorithme commence par initialiser les distances des sommets à l'infini, puis il effectue des relaxations sur les arêtes jusqu'à ce que les distances convergent vers les valeurs correctes.

L'algorithme Hangroise utilise la notion de relaxation qui peut être exprimée par l'inégalité suivante pour une arête $(u, v)$ de poids $w(u, v)$ :

$$d[v] \leq d[u] + w(u, v)$$

où $d[u]$ et $d[v]$ représentent respectivement la distance actuelle du sommet $u$ et $v$ à partir de la source $s$. L'algorithme effectue cette relaxation sur toutes les arêtes itérativement jusqu'à ce que la distance la plus courte de $s$ à tous les autres sommets soit obtenue.

![image](https://github.com/IbLahlou/Graph_Projects/assets/105231126/8faf13c0-4ae9-4d9f-a8a0-fc263e523c02)


## 4 - Algorithme de Page Rank (Processus de Markov)
L'algorithme de Page Rank est utilisé pour attribuer des scores d'importance à chaque page web dans un réseau de pages liées. Il se base sur le principe du processus de Markov, où un utilisateur aléatoire sur le web clique de manière itérative sur des liens, simulant ainsi un surfeur aléatoire. Les pages avec un plus grand nombre de liens entrants et provenant de pages importantes auront un score de Page Rank plus élevé, ce qui reflète leur importance supposée dans le réseau.

Le Page Rank d'une page $P_i$ peut être défini par l'équation suivante :

$$PR(P_i) = (1 - d) + d \cdot \sum\limits_{P_j \in M(P_i)} \frac{PR(P_j)}{L(P_j)}$$


où $PR(P_i)$ est le Page Rank de la page $P_i$, $M(P_i)$ est l'ensemble des pages qui ont des liens sortants vers $P_i$, $L(P_j)$ est le nombre total de liens sortants de la page $P_j$, et $d$ est un facteur d'amortissement (généralement fixé à 0,85) qui représente la probabilité que le surfeur aléatoire continue de cliquer sur des liens plutôt que de sauter aléatoirement à une autre page.

![image](https://github.com/IbLahlou/Graph_Projects/assets/105231126/c73cbf57-ddec-4dee-b9fa-b598eadf74e8)
![pr1](https://github.com/IbLahlou/Graph_Projects/assets/105231126/74072317-cc7d-46ed-947b-53ebe5fdae2c)
