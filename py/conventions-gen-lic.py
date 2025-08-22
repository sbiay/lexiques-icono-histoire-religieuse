"""
Ce script ouvre le fichier
/home/sbiay/depotsGit/lexiques-icono-histoire-religieuse/conventions-gen.md
et en sélectionne le contenu selon les balises,
pour écrire le résultat dans un nouveau fichier

<!--pas en licence DEBUT-->
<!--pas en licence FIN-->
<!--pas en licence-->


"""



# On ouvre les conventions générales
with open("/home/sbiay/depotsGit/lexiques-icono-histoire-religieuse/conventions-gen.md") as f:
	contenu = f.read()

contenu = contenu.split("\n")

nouveauContenu = []
interrompre = False
for ligne in contenu:
	if "<!--pas en licence DEBUT-->" in ligne:
		interrompre = True
		continue
	elif "<!--pas en licence FIN-->" in ligne:
		interrompre = False
		continue

	if not "<!--pas en licence-->" in ligne and not interrompre:
		nouveauContenu.append(ligne)

contenu = "\n".join(nouveauContenu)

with open("/home/sbiay/depotsGit/lexiques-icono-histoire-religieuse/conventions-gen-licence.md", mode="w") as f:
	f.write(contenu)