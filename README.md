# Graph_Projects
Projet de Recherche Opérationnel pour trouver le plus cours chemin 

## 1 - Problème de plus court chemin
   Soit $G=(S,A)$ un graphe , avec deux sommets distingués $s$ (la source ou l'origine) et $t$ (le but ou le puits) ;
   On note $w(i,j)$ le cout de l'arc $(i,j)$
   On considère le programme linéaire en les variables $x_{ij}$ suivant :
   
   minimiser $\sum\limits_{ij \in A} w(i,j)x_{ij}$
   
   sous contrainte : 
      $\forall i,j \in \mathbb{R} \ \ x_{ij} >= 0$
      
$\sum_jx_{ij} - \sum_jx_{ji}=
\left\{
  \begin{array}\\
      1 & \mbox{if } \ i = s;
      0 & \mbox{if } \ i = t;
      -2 & \mbox{else.}
  \end{array}
\right.$
   
## 2 - Algortihm de ford-fulkerson
## 3 - Algorithme Hangroise
