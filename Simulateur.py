# Saisie des informations

prix_achat = float(input("Entrez le prix d'achat : "))
prix_vente = float(input("Entrez le prix de vente : "))
quantite = int(input("Entrez la quantité : "))

# Calculs

cout_total = prix_achat * quantite
montant_vente = prix_vente * quantite
resultat = montant_vente - cout_total

# Affichage

print("\n===== RÉSULTAT =====")
print("Coût total :", cout_total)
print("Montant de la vente :", montant_vente)

# Vérification

if resultat > 0:
    print("Bénéfice :", resultat)
    print("Bravo ! Votre opération est rentable.")

elif resultat < 0:
    print("Perte :", abs(resultat))
    print("Attention ! Vous êtes en perte.")

else:
    print("Ni bénéfice ni perte.")
