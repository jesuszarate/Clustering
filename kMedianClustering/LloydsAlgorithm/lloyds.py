import numpy as np
import random

def Init2DClusters(path):
    cluster_list = []
    center = None
    gotCenter = False
    with open(path, 'r') as f:
        for line in f:
            l = line.split()

            cluster_list.append((float(l[1]), float(l[2])))

    return cluster_list

path = "/Users/jesuszarate/SchoolSemesters/Spring2017/CS6140-DataMining/Clustering/Resources/C2.txt"

def init_board():
    N = 10
    X = np.array(Init2DClusters(path))
    return X

def cluster_points(X, mu):
    clusters  = {}
    for x in X:
        bestmukey = min([(i[0], np.linalg.norm(x-mu[i[0]])) \
                         for i in enumerate(mu)], key=lambda t:t[1])[0]
        try:
            clusters[bestmukey].append(x)
        except KeyError:
            clusters[bestmukey] = [x]
    return clusters

def reevaluate_centers(mu, clusters):
    newmu = []
    keys = sorted(clusters.keys())
    for k in keys:
        newmu.append(np.mean(clusters[k], axis = 0))
    return newmu

def has_converged(mu, oldmu):
    return (set([tuple(a) for a in mu]) == set([tuple(a) for a in oldmu]))

def find_centers(X, K, m):
    # Initialize to K random centers
    oldmu = random.sample(X, K)
    mu = np.array(m)#random.sample(X, K)
    while not has_converged(mu, oldmu):
        oldmu = mu
        # Assign all points in X to clusters
        clusters = cluster_points(X, mu)
        # Reevaluate centers
        mu = reevaluate_centers(oldmu, clusters)
    return(mu, clusters)

X = init_board()
#c = cluster_points(X, [1,2,3])
here = find_centers(X, 3, [X[0], X[1], X[2]])
print

