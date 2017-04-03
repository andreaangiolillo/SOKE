import socket
import pickle
import numpy as np
def main():
    host = "127.0.0.1"
    port = 5000
    
    s = socket.socket()
    s.connect((host,port))
    user = "1"
    article = "130"
    s.send(user)
   
    data = s.recv(1024)
    print "Received from server:" + str(data)
    s.send(article)
    
    #receiving the associations to evaluate 
    data = s.recv(1024)
    data_arr = pickle.loads(data)#deserialization
    
    c = 0
    eval = []
    print "Received from server:" 
    for i in data_arr:
        print i
        c = c + 1  
        eval.append(c)
    
    #sending the valuation
    s.send(pickle.dumps(eval))
    
    
    
    data = s.recv(10960)
    prediction_result = pickle.loads(data) 
    
    data = s.recv(40960)
    assoc_properties = pickle.loads(data)
    
    print prediction_result, "\n", assoc_properties, "client" 
    
    
        
if __name__ == '__main__':
    main()
