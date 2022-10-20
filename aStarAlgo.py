def astaralgo(startNode,endNode):
    openSet=set(startNode)
    closeSet=set()
    # distance from start nod
    g={}
    # contain adjacent map of all nodes
    parent={}
    # distance of start node is 0 
    g[startNode]=0
    # START NODE IS ROOT NODE SO IT HAS NO PRENT NODES
    # HENCE START NODE IS SET TO ITS OWN PARTENT NODE
    parent[startNode]=startNode

    while(len(openSet)>0):
        n=None
        # node with lowest f(n) is found
        for v in openSet:
            if (n==None) or  (g[v]+heuristic(v) < g[n]+heuristic(n)):
                n=v
        if (n==endNode) or (graphNodes[n]==None):
            pass
        else:
            for (m,weight) in getNeighbours(n):
                if (m not in openSet) and (m not in closeSet):
                    openSet.add(m)
                    parent[m]=n
                    g[m]=g[n]+weight
                else:
                    if g[m] > g[n]+weight:
                        g[m]=g[n]+weight
                        parent[m]=n
                    if m in closeSet:
                        closeSet.remove(m)
                        openSet.add(m)



def getNeighbours(v):
    if v in graphNodes:
        return graphNodes[v]
    else:
        return None

def heuristic(v):
    h_dict= {
                'a':11,
                'b':6,
                'c':99,
                'd':1,
                'e':7,
                'g':0
            }
    return h_dict[v]

graphNodes= {
                'a' :   [ ('b',2) , ('e',3) ] ,
                'b' :   [('c',1),('g',9)],
                'c' :   None,
                'e' :   [('d',6)],
                'd' :   [('g',1)]
            }

astaralgo('a','g')
