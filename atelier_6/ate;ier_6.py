import maya.cmds as cmds
import math


def creer_cloture(
    debut=(0, 0, 0),
    fin=(10, 0, 0),
    hauteur=2.0,
    espacement=2.0
):
    # Calcul de la longueur de la clôture
    dx = fin[0] - debut[0]
    dy = fin[1] - debut[1]

    longueur = math.sqrt(dx**2 + dy**2)

    if longueur == 0:
        cmds.warning("La longueur de la clôture doit être supérieure à zéro.")
        return None

    nombre_intervalles = max(1, math.ceil(longueur / espacement))
    nombre_poteaux = nombre_intervalles + 1

    angle = math.degrees(math.atan2(dy, dx))

    # Groupe principal
    groupe = cmds.group(empty=True, name="Cloture_Groupe")

    # Décalage des barreaux vers l'extérieur
    decalage_exterieur = 0.15

    # Création des poteaux
    for i in range(nombre_poteaux):
        t = i / nombre_intervalles

        x = debut[0] + dx * t
        y = debut[1] + dy * t

        poteau = cmds.polyCube(
            name=f"Poteau_{i + 1}",
            width=0.15,
            height=hauteur,
            depth=0.15
        )[0]

        cmds.move(
            x,
            y - decalage_exterieur,
            debut[2] + hauteur / 2,
            poteau
        )

        cmds.parent(poteau, groupe)

    # Création des traverses horizontales
    for i in range(nombre_intervalles):
        t1 = i / nombre_intervalles
        t2 = (i + 1) / nombre_intervalles

        x1 = debut[0] + dx * t1
        y1 = debut[1] + dy * t1

        x2 = debut[0] + dx * t2
        y2 = debut[1] + dy * t2

        longueur_segment = math.sqrt(
            (x2 - x1)**2 + (y2 - y1)**2
        )

        milieu_x = (x1 + x2) / 2
        milieu_y = (y1 + y2) / 2 - decalage_exterieur

        # Deux traverses par segment
        for j, niveau in enumerate([0.35, hauteur - 0.45]):
            traverse = cmds.polyCube(
                name=f"Traverse_{i + 1}_{j + 1}",
                width=longueur_segment,
                height=0.12,
                depth=0.08
            )[0]

            cmds.move(
                milieu_x,
                milieu_y,
                debut[2] + niveau,
                traverse
            )

            cmds.rotate(
                0, -angle, 0,
                traverse,
                relative=True
            )

            cmds.parent(traverse, groupe)

    print("Clôture créée avec succès !")
    return groupe


# Exemple d'utilisation
creer_cloture(
    debut=(0, 0, 0),
    fin=(10, 0, 0),
    hauteur=2.0,
    espacement=2.0
)