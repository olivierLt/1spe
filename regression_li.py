# origine du programme : https://gsalvatovallverdu.gitlab.io/python/moindres-carres/

def regLin(x, y):
    """
    Ajuste une droite d'équation a*x + b sur les points (x, y) par la méthode
    des moindres carrés.

    Args :
        * x (list): valeurs de x
        * y (list): valeurs de y

    Return:
        * a (float): pente de la droite
        * b (float): ordonnée à l'origine
        * r2 (float) : coefficient de corrélation
    """
    # initialisation des sommes
    x_sum = 0.
    x2_sum = 0.
    y_sum = 0.
    xy_sum = 0.
   # nombre de points
    npoints = len(x)
    # calcul des sommes
    for xi in x:
        x_sum = x_sum + xi
    for yi in y:
        y_sum = y_sum + yi
    for xi in x:
        x2_sum = x2_sum + xi**2
    for i in range(npoints):
        xy_sum=xy_sum +x[i]*y[i]  
    # calcul des paramètres
    a = (npoints * xy_sum - x_sum * y_sum) / (npoints * x2_sum - x_sum**2)
    b = (x2_sum * y_sum - x_sum * xy_sum) / (npoints * x2_sum - x_sum**2)
    #calcul du coefficient de régression
    ymoy=y_sum/len(y)
    r2num=0
    r2denom=0
    for i in range(npoints):
        r2num=r2num+(a*x[i]+b -ymoy)**2
        r2denom=r2denom + (y[i] - ymoy)**2
    r2=r2num/r2denom 
  
    # renvoie des paramètres
    return a, b,r2
