var $ = require('jquery');

var net = require('net');
var HOST = '127.0.0.1';
var PORT = 6000;


var client = new net.Socket();
client.connect(PORT, HOST, function() {
 
    console.log('CONNECTED TO: ' + HOST + ':' + PORT);
    // Inviamo un messaggio al server non appena il client si è connesso, il server riceverà questo messaggio dal client.
    client.write("1");
    client.write("130");
    
    
    client.on('data', function(data) {
    	 
        console.log('DATA: ' + data);
        
        // chiude il client socket 
        client.destroy();
     
    });
 
});


