import igraph as ig
import plotly.plotly as py
from plotly.graph_objs import *
import Preprocessing
import json
import urllib2
py.sign_in('walter123456', 'xmGKiFqUcLmC29v3zb5I')




def create_graph_with_networkx(article):
    
    data = Preprocessing.extract_association_score(article,True)
    graph = []
    labels =[]
    node = []
#     for row in data:
#         print len(row)
#         print row
#     
#     
    
    for row in data:
        if row[2] != "":
            node.append(row[0])
            node.append(row[2])
            node.append(row[4])
            graph.append((row[0], row[2]))
            labels.append(row[1])
            graph.append((row[2], row[4]))
            labels.append(row[3])
        else:
            node.append(row[0])
            node.append(row[4])
            graph.append((row[0], row[4]))
            labels.append(row[1])
            
    #print graph, "graph"
#     
#     graph = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8), (1, 6), (3, 7), (5, 9),
#              (2, 4), (0, 4), (2, 5), (3, 6), (8, 9), (2,2), (3,3), (0,99),(99,98), ("aaa","ssss"), (111,111)]


    #print labels,"labels"
    node = set(node)
    #print node
    return graph, labels, node











if __name__ == '__main__':
    edge, edgename, node = create_graph_with_networkx(130)
    
    N=len(node)
    dictionary_node = {}
    i = 0
    for n in node:
        dictionary_node[n] = i
        print i
        i += 1
    
    #print len(dictionary_node),"lwn"
    #print edge
    edge_with_num = []   
    for ed in edge:
        edge_with_num.append((dictionary_node[ed[0]], dictionary_node[ed[1]]));
        
        
    #labels
    name_sorted = sorted(dictionary_node.items(), key=lambda x: x[1], reverse=False),"assasasasasa"
    labels = []
    for item in name_sorted[0]:
        #print item[0]
        labels.append(item[0])
    
#     print name_sorted
#     print labels    
#      
#     print edge_with_num
    
    G=ig.Graph(edge_with_num, directed=True)
    
    layt=G.layout('kk_3d', dim=3)
    Xn=[layt[k][0] for k in range(N)]# x-coordinates of nodes
    Yn=[layt[k][1] for k in range(N)]# y-coordinates
    Zn=[layt[k][2] for k in range(N)]# z-coordinates
    Xe=[]
    Ye=[]
    Ze=[]
    Xx = []
    Yy = []
    Zz = []
    for e in edge_with_num:
        Xe+=[layt[e[0]][0],layt[e[1]][0], None]# x-coordinates of edge ends
        #print Xe
        Xx.append((layt[e[0]][0] + layt[e[1]][0])/2)
        Ye+=[layt[e[0]][1],layt[e[1]][1], None]
        Yy.append((layt[e[0]][1] + layt[e[1]][1])/2)
        Ze+=[layt[e[0]][2],layt[e[1]][2], None]
        Zz.append((layt[e[0]][2] + layt[e[1]][2])/2)

          
    trace1=Scatter3d(x=Xe,
                   y=Ye,
                   z=Ze,
                   mode='lines',
                   line=Line(color='rgb(125,125,125)', width=2),
#                    text = "",
                    hoverinfo= 'none'
                   
                   )
    trace2=Scatter3d(x=Xn,
                   y=Yn,
                   z=Zn,
                   mode='markers',
                   name=labels,
                   marker=Marker(symbol='dot',
                                 size=6,
                                 color='rgb(69, 169, 255)',
                                 colorscale='Viridis',
                                 line=Line(color='rgb(69, 169, 255)', width=0.7)
                                
                                 ),
                   text=labels,
                   hoverinfo='text'
                   )
    trace3=Scatter3d(x=Xx,
                   y=Yy,
                   z=Zz,
                   mode='markers',
                   name=edgename,
                   marker=Marker(symbol='dot',
                                 size=1,
                                 #color=group,
                                 colorscale='Viridis',
                                 line=Line(color='rgb(50,50,50)', width=0.2)
                                
                                 ),
                   text=edgename,
                   hoverinfo='text'
                   )
     
     
     
     
    axis=dict(showbackground=False,
              showline=False,
              zeroline=False,
              showgrid=False,
              showticklabels=False,
              title=''
              )
     
     
    layout = Layout(
             title="",
#              paper_bgcolor='rgba(0,0,0,0)',
#              plot_bgcolor='rgba(0,0,0,0)',
             width=1000,
             height=1000,
             showlegend=False,
             scene=Scene(
             xaxis=XAxis(axis),
             yaxis=YAxis(axis),
             zaxis=ZAxis(axis),
            ),
         margin=Margin(
            t=100
        ),
        hovermode='closest',
        annotations=Annotations([
               Annotation(
               showarrow=False,
                text="",
                xref='paper',
                yref='paper',
                x=0,
                y=0.1,
                xanchor='left',
                yanchor='bottom',
                font=Font(
                size=14
                )
                )
            ]),    )
     
     
    data=Data([trace1, trace2,trace3])
    fig=Figure(data=data, layout=layout)
     
    py.iplot(fig, filename='Les-Miserables')
     
