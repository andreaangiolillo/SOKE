import igraph as ig
import plotly.plotly as py
from plotly.graph_objs import *
import Preprocessing
import Main 
import json
import random 
import urllib2
py.sign_in('walter123456', 'xmGKiFqUcLmC29v3zb5I')

article = 145
user = 17

def create_graph_with_networkx(article):
    
    data = Preprocessing.extract_association_score(article,True)
    graph = []
    labels_edge =[]
    node = []
    online_learning_top10 = Main.learning(article, user, 5, 2)[:10]
    
    print online_learning_top10, "ONLINE LEARNING"
    
    
    group = []
    name_ass_online_learning = []
   
    print data
    
    for row in data:
        
          
        if row[3] != "":
             
            #for color
            if int(row[0]) in online_learning_top10:
                name_ass_online_learning.append(row[1])
                name_ass_online_learning.append(row[3])
                name_ass_online_learning.append(row[5])
             
            node.append(row[1])    
            node.append(row[3])
            node.append(row[5])
            labels_edge.append(row[2])
            if "R:" in row[2]:
                graph.append((row[3], row[1]))
            elif "L:" in row[2]:
                graph.append((row[1], row[3]))
                 
            labels_edge.append(row[4])
             
            if "R:" in row[4]:
                graph.append((row[5], row[3]))
            elif "L:" in row[4]:
                graph.append((row[3], row[5]))
             
        else:
            #for color
            if int(row[0]) in online_learning_top10:
                name_ass_online_learning.append(row[1])
                name_ass_online_learning.append(row[5])
             
            node.append(row[1])
            node.append(row[5])
            labels_edge.append(row[2])
            
            if "R:" in row[2]:
                graph.append((row[5], row[1]))
            elif "L:" in row[2]:
                graph.append((row[1], row[5]))
            
             
 
    #print labels_edge,"labels_edge"
    node = set(node)
         
    for n in node:
         
        if n in name_ass_online_learning:
            group.append('rgb(255, 0, 0)')
        else:
            group.append('rgb(69, 169, 255)')
             
     
     
     
    #print node
    print graph, "G"
    print labels_edge, "L"
    print node, "N"
    print group, "GG" 
    return graph, labels_edge, node, group






if __name__ == '__main__':
    edge, edgename, node, group = create_graph_with_networkx(article)
    
    print "first check: ", len(edgename) == len(edge)
    
    N=len(node)
    dictionary_node = {}
   
    i = 0
    for n in node:
        dictionary_node[n] = i
        #print n, "node"
        i += 1
    
    
    print edge, "EDGE"
    print dictionary_node, "dictionary"
    edge_with_num = []   
    for ed in edge:
        edge_with_num.append((dictionary_node[ed[0]], dictionary_node[ed[1]]));
         
    #print "third check: ", len(edge_with_num) == len(edgename)
    
    print edge_with_num, "edge_with_num", len(edge_with_num) == len(edgename)
    print edgename
     
    #labels_edge
    name_sorted = sorted(dictionary_node.items(), key=lambda x: x[1], reverse=False)
    print name_sorted[0]
    labels = []#NAME NODE
    for item in name_sorted:
        #print item[0]
        labels.append(item[0])
      
    print name_sorted
    print labels    
       
    print edge_with_num
      
    G=ig.Graph(edge_with_num, directed=False)
     
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
                   name='actors',
                   marker=Marker(symbol='dot',
                                 size=6,
                                 color=group,
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
                                 size=2,
                                 #color=group,
                                 colorscale='Viridis',
                                 #line=Line(color='rgb(50,50,50)', width=0.2)
                                  
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
       
    py.iplot(fig, filename='prova')
     
