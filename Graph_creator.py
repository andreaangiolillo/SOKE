import networkx as nx
import matplotlib.pyplot as plt
import Preprocessing
import igraph





def create_graph_with_igraph(article):
    
    g = igraph.Graph([(0,1), (0,2), (2,3), (3,4), (4,2), (2,5), (5,0), (6,3), (5,6)])
    
    g.vs["name"] = ["Alice", "Bob", "Claire", "Dennis", "Esther", "Frank", "George"]
    g.vs["age"] = [25, 31, 18, 47, 22, 23, 50]
    g.vs["gender"] = ["f", "m", "f", "m", "f", "m", "m"]
    g.es["is_formal"] = [False, False, True, True, True, False, True, False, False]
    
    
    
    color_dict = {"m": "blue", "f": "pink"}
    layout = g.layout("kk")
    visual_style = {}
    visual_style["vertex_size"] = 20
    visual_style["vertex_color"] = [color_dict[gender] for gender in g.vs["gender"]]
    visual_style["vertex_label"] = g.vs["name"]
    visual_style["edge_width"] = [1 + 2 * int(is_formal) for is_formal in g.es["is_formal"]]
    visual_style["edge_label"] = g.vs["age"]
    visual_style["layout"] = layout
    visual_style["bbox"] = (600, 600)
    visual_style["margin"] = 20
    igraph.plot(g, **visual_style)
   
def create_graph_with_networkx(article):
    
    data = Preprocessing.extract_association_score(article,True)
    graph = []
    labels =[]
#     for row in data:
#         print len(row)
#         print row
#     
#     
    
    for row in data:
        if row[2] != "":
            graph.append((row[0], row[2]))
            labels.append(row[1])
            graph.append((row[2], row[4]))
            labels.append(row[3])
        else:
            graph.append((row[0], row[4]))
            labels.append(row[1])
            
    #print graph
#     
#     graph = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9),
#              (2, 4), (0, 4), (2, 5), (3, 6), (8, 9), (2,2), (3,3), (0,99),(99,98), ("aaa","ssss"), (111,111)]


    #print labels

    draw_graph(graph, labels)









def draw_graph(graph, labels=None, graph_layout='shell',
               node_size=500, node_color='blue', node_alpha=0.3,
               node_text_size=12,
               edge_color='blue', edge_alpha=0.3, edge_tickness=1,
               edge_text_pos=0.3,
               text_font='sans-serif'):

    # create networkx graph
    G=nx.Graph()

    # add edges
    for edge in graph:
        G.add_edge(edge[0], edge[1])

    # these are different layouts for the network you may try
    # shell seems to work best
    if graph_layout == 'spring':
        graph_pos=nx.spring_layout(G)
    elif graph_layout == 'spectral':
        graph_pos=nx.spectral_layout(G)
    elif graph_layout == 'random':
        graph_pos=nx.random_layout(G)
    else:
        graph_pos=nx.shell_layout(G)
    
    ax = plt.subplots(figsize=(10, 10))
    # draw graph
    nx.draw_networkx_nodes(G,graph_pos,node_size=node_size, 
                           alpha=node_alpha, node_color=node_color)
    nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                           alpha=edge_alpha,edge_color=edge_color)
    nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                            font_family=text_font)

    if labels is None:
        labels = range(len(graph))

    edge_labels = dict(zip(graph, labels))
    nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels, 
                                 label_pos=edge_text_pos)
    
    # show graph
  
    plt.show()


if __name__ == '__main__':
    
    #create_graph_with_networkx(130)
    
    create_graph_with_igraph(130)
    
    
    
#     data = Preprocessing.extract_association_score(130,True)
# 
#     graph = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9),
#              (2, 4), (0, 4), (2, 5), (3, 6), (8, 9), (2,2), (3,3), (0,99),(99,98), ("aaa","ssss"), (111,111)]
#     
#     # you may name your edge labels
#     labels = map(chr, range(65, 65+len(graph)))
#     draw_graph(graph, labels)
#     
    # if edge labels is not specified, numeric labels (0, 1, 2...) will be used
    #draw_graph(graph)