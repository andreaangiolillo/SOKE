import socket
import pickle
import numpy as np
def main():
    host = "127.0.0.1"
    port = 6000
    
    s = socket.socket()
    s.connect((host,port))
    user = "6"
    article = "133"
    s.send(user)
   
    data = s.recv(1024)
    #print "Received from server:" + str(data)
    s.send(article)
    
    #The servers runs the clustering algorithm and
    #returns the first associations that the user will evaluate
    data = s.recv(1024)
    data_arr = pickle.loads(data)#deserialization

    c = 0
    eval = []
    #print "Received from server:" 
    for i in data_arr:
        print i
        c = c + 1  
        eval.append(c)
    
    #sending the valuation
    s.send(pickle.dumps(eval))
    
    
    
    data = s.recv(10960)
    prediction = pickle.loads(data) 
    
    data = s.recv(40960)
    assoc_properties = pickle.loads(data)
    
    print prediction, "\n", assoc_properties, "client" 
    
    
        
if __name__ == '__main__':
    main()
