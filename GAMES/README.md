TP4 RENDU
IMAC1 S2
DUPUIS Maxence, DOUET Angèle

    INTRODUCTION

Lors du dernier TP d’Architecture Logicielle, nous avons créé un site recensant des jeux entrés par l’utilisateur.
Depuis la page d’accueil, nous pouvons ajouter un jeu ou simplement voir la liste des jeux déjà entrés. Sur la page d’affichage des jeux, nous pouvons supprimer un jeu, le modifier, en ajouter un autre ou retourner à la page d’accueil.

    DÉROULÉ

Voici comment nous nous sommes organisés pour réaliser ce TP.
Avec un peu de collaboration, les premières étapes de création de formulaire et d’affichage de jeux entrés se sont bien déroulées.
Les étapes de suppression ou de modification de jeux nous a demandé un peu plus de réflexion.
Dans nos recherches pour la suppression, nous nous sommes rendus compte que lorsque nous supprimions tous les jeux, nous étions mal redirigés. Nous avons alors découvert la fonction Flask redirect qui réglait ce soucis!
Et en découvrant ce problème de redirection, nous nous sommes aussi aperçu que nous ne pouvions voir la liste des jeux que si l’on en ajoutait un. La fonction redirect nous a donc permis de segmenter nos routes, afin d’en avoir une qui gère l’ajout de jeux et une autre qui gère l’affichage des jeux!
Pour ce qui est de la modification, la récupération de l’id du jeu à modifier était complexe à implémenter.

    RETOURS

Globalement, le point d’amélioration que nous avons est la logique de savoir quelle route renvoie à quel template ou quelle autre route, des problèmes d’organisation et de compréhension des chemins.
Maxence: J’ai découvert redirect permettant de ne pas abuser du render_template en faisant un POST. J’ai pu progresser en Python. Sinon, je suis plutôt à l’aise sur ce qu’on a fait.
Angèle: J’ai progressé exponentiellement par rapport au premier TP étant donné que je n’avais aucune base. J’ai toujours un peu de mal à comprendre quoi mettre dans le template html et quoi mettre dans la définition des routes en Python mais c’est un souci qui se règlera avec l’expérience. J’ai aussi encore un peu de mal avec la syntaxe pour chaque langage. Mais j’ai beaucoup appris, le rythme des TP m’a permis de ne pas trop me sentir à la ramasse et de bien progresser à mon rythme.

    MOT DE LA FIN

Vive les tartiflettes et Timothée Chalamet.
