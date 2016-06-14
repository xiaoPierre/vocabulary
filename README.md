# Vocabulaire.com

---

Explications sur les dossiers:

* app
    * Article
        * analyseArticle.py : fonction pour analyser l'article
    * BDD
        * connectBDD.py : fonction pratique pour connecter la base de données
    * Crawler
        * crawlArticle.py : récupérer un article selon thème
        * crawlImage.py : récupérer un URL de l'image correspondant au mot
        * crawlWord.py : récupérer des informations (définitions, synonyme, antonyme ...) sur le mot
    * Dictionary
        * dictionary.py : méthodes pratiques pour chercher les informations des mots (trouver la lemme, les mots ayant le même préfixe)
        * dawgFile.dawg : structure de données DAWG stocke tous les mots français sous forme de l'arbre
    * Exercise
        * ExerciceGenerator.py : y se trouvent les générateurs d'exercice
        * LevelTest.py : méthode pour créer un test de niveau contenant 30 tests
    * Model
        * Article.py : définition du objet Article
        * Exercise.py : définition du objet Exercise
        * User.py : définition du objet User
        * Word.py ： définition du objet Word  (cet objet est créé par la BDD lexique3)
        * WordCrawled.py : définition du objet WordCrawled (cet objet est créé par crawler)
    * misc
        * etendu.py : tableau représentant les niveaux des mots (intervalles de fréquence)
        * generateDawg.py : générer le DAWG objet à partir du fichier wordList.txt
        * generateLexiqueBDD.py : générer la BDD de lexique à partir du fichier Lexique381.txt
        * Lexique381.txt : BDD de Lexique3 (http://www.lexique.org/)
        * wordList.txt : tous les mots français en string
    * static
        * css : y se trouvent les fichiers CSS
        * image : y se trouvent les images
        * js : y se trouvent les fichiers JavaScript
    * templates : y se trouvent les fichiers HTML
    * views.py : routage du site web

* test : tests unitaires pour les modules Article, Crawler, Dictionary et Exercise

* config.py : configuration du flask
* scriptRun.py : entrée du programme

