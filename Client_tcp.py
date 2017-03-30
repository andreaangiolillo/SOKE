import socket
import pickle

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
    
    print "Received from server:" 
    for i in data_arr:
        print i 

if __name__ == '__main__':
    main()
