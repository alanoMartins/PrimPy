import PrimImp as PrimAlg
import networkx as nx
from networkx_viewer import Viewer

if __name__ == "__main__":
    mat = [
    [0, 1, 0, 0, 4, 8, 0, 0],
    [1, 0, 2, 0, 0, 6, 6, 0],
    [0, 2, 0, 3, 0, 0, 2, 0],
    [0, 0, 3, 0, 0, 0, 1, 4],
    [4, 0, 0, 9, 0, 5, 0, 0],
    [8, 6, 0, 0, 5, 0, 1, 0],
    [0, 6, 2, 1, 0, 1, 0, 1],
    [0, 0, 0, 4, 0, 0, 1, 0]
]
    prim = PrimAlg.Prim()
    par, pes = prim.execute(mat, 0)

    G = nx.MultiGraph()

    for idx in range(0, len(mat)):
        G.add_edge(idx, par[idx])
        G.node[idx]['color'] = 'blue'

    app = Viewer(G)
    app.mainloop()
