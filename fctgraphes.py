#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 13:51:38 2021

@author: jpphi
"""

import networkx as nx
import matplotlib.pyplot as plt

"""
graphe={
    'A':{'B':2, 'C':1},
    'B':{'A':2, 'C':2, 'D':1, 'E':3}, 
    'C':{'A':1, 'B':2, 'D':4, 'E':3, 'F':5}, 
    'D':{'B':1, 'C':4, 'E':3, 'F':6, 'G':5}, 
    'E':{'B':3, 'C':3, 'D':3, 'F':1}, 
    'F':{'C':5, 'D':6, 'E':1, 'G':2}, 
    'G':{'D':5, 'F':2} }

graphe2= {
    'A':{'B':2, 'C':1},
    'B':{'C':2, 'D':1, 'E':3}, 
    'C':{'D':4, 'E':3, 'F':5}, 
    'D':{'E':3, 'F':6, 'G':5}, 
    'E':{'F':1}, 
    'F':{'G':2}, 
    'G':{} }
"""


#-----------------------------------------------------------------------------
#                          Definition de classe
#-----------------------------------------------------------------------------
class GrapheJP:
    cheminement= []
    liste_sommets_explores= []

    def arc(self,graph):
        arc= {}

        for clefs,valeurs in graph.items():
            #print(clefs,valeurs)
            for clefs2,valeurs2 in valeurs.items():
                arc[clefs+clefs2]= valeurs2
                
        return arc
    
    
    def parcoursProfondeur(self,graph):
        self.liste_sommets_explores=[]
        for sommet in graph.keys():
            print("Fct parcoursProfondeur: sommet: {}".format(sommet))
            self.cheminement.append(sommet)
            if sommet not in self.liste_sommets_explores:
                self.liste_sommets_explores.append(sommet)
                self.explorer(graph,sommet)

        # Le parcours en profondeur d'un graphe G est alors :
        #   parcoursProfondeur(graphe G)
        #       pour tout sommet s du graphe G
        #       si s n'est pas marqué alors
        #              explorer(G, s)

    def explorer(self,graph, sommet):
        print("Fct explorer. sommet: {} sommet exploré: {}".format(sommet, 
            self.liste_sommets_explores))
        
        for noeud,poids in graph.items():
            print("noeud: {} poids: {}".format(noeud,poids))
            self.cheminement.append(noeud)
            if noeud not in self.liste_sommets_explores:
                self.liste_sommets_explores.append(noeud) 
                self.explorer(graph,noeud)
        return sommet
    
        # marquer le sommet s
        # afficher(s)
        # pour tout sommet t voisin du sommet s
        #       si t n'est pas marqué alors
        #              explorer(G, t);
        

    def parcoursLargeur(self,graph):
        self.ListeChemin={}
        
        for noeud, sgraph in graph.items():
            for enf, poids in sgraph.items():
                #print("Fct parcourslargeur: noeud: {} sous graph: {} enf: {} \
                #      poids: {}".format(noeud, sgraph, enf, poids))
                self.ListeChemin[noeud+enf]= poids
        # suprimer les chemins retours AB / BA
        return self.ListeChemin
    
    def Dijkstra(self, graph, start, end):
        self.chemin= {}
        
        return self.chemin
    
    def affiche(self,graph):
        for k,v in graph.items():
            print(k," : ",v)

    #--------------------------------------------------------------------------
    #                            Affichage du graphe
    #--------------------------------------------------------------------------
    def afficheGraphe(self,graph):
        g = nx.Graph()
        for i, j in graph.items():
            for k,v in j.items():
                #print("for niv2: ",i,j,k,v)
                #print("chemin: ",i, k, v)
                g.add_edge(i,k,weight= v)
        f, ax = plt.subplots(figsize=(10,5))
        nx.draw(g, ax = ax, with_labels=True, font_weight='bold')
  





class titi:
    def toto(self):
        print("tutu")






#--------------------------------------------------------------------------
#                            Djistra
#--------------------------------------------------------------------------



def dij_rec(graphe, debut, fin):
    return plus_court(graphe, debut, fin, [], {}, {}, debut)

 
def affiche_peres(pere, depart, extremite, trajet):
    """
    À partir du dictionnaire des pères de chaque sommet on renvoie
    la liste des sommets du plus court chemin trouvé. Calcul récursif.
    On part de la fin et on remonte vers le départ du chemin.
    
    """
    if extremite == depart:
        return [depart] + trajet
    else:
        return (affiche_peres(pere, depart, pere[extremite], [extremite] + trajet))


def plus_court(graphe, etape, fin, visites, dist, pere, depart):
    """
    Trouve récursivement la plus courte chaine entre debut et fin avec l'algo de Dijkstra
    visites est une liste et dist et pere des dictionnaires 
    graphe  : le graphe étudié                                                               (dictionnaire)
    étape   : le sommet en cours d'étude                                                     (sommet)
    fin     : but du trajet                                                                  (sommet)
    visites : liste des sommets déjà visités                                                 (liste de sommets)
    dist    : dictionnaire meilleure distance actuelle entre départ et les sommets du graphe (dict sommet : int)
    pere    : dictionnaire des pères actuels des sommets correspondant aux meilleurs chemins (dict sommet : sommet)
    depart  : sommet global de départ                                                        (sommet)
    Retourne le couple (longueur mini (int), trajet correspondant (liste sommets)) 
       
    """
    # si on arrive à la fin, on affiche la distance et les peres
    if etape == fin:
       return dist[fin], affiche_peres(pere, depart, fin, [])
    # si c'est la première visite, c'est que l'étape actuelle est le départ : on met dist[etape] à 0
    if len(visites) == 0:
        dist[etape] = 0
    # on commence à tester les voisins non visités
    for voisin in graphe[etape]:
        if voisin not in visites:
            # la distance est soit la distance calculée précédemment soit l'infini
            dist_voisin = dist.get(voisin, float('inf'))
            # on calcule la nouvelle distance calculée en passant par l'étape
            candidat_dist = dist[etape] + graphe[etape][voisin]
            # on effectue les changements si cela donne un chemin plus court
            if candidat_dist < dist_voisin:
                dist[voisin] = candidat_dist
                pere[voisin] = etape
    # on a regardé tous les voisins : le noeud entier est visité
    visites.append(etape)
    # on cherche le sommet *non visité* le plus proche du départ
    non_visites = dict((s, dist.get(s, float('inf')))
                       for s in graphe if s not in visites)
    noeud_plus_proche = min(non_visites, key=non_visites.get)
    #noeud_plus_proche = min(non_visites.values())
    # on applique récursivement en prenant comme nouvelle étape le sommet le plus proche
    return plus_court(graphe, noeud_plus_proche, fin, visites, dist, pere, depart)

