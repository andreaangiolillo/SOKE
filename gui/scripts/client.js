var $ = require('jquery');

var net = require('net');
var HOST = '127.0.0.1';
var PORT = 6000;


//insert a scroll bar for the table 
$(window).resize(function(){
	var windows_width = $(window).width(); 
	console.log(windows_width);
	if (windows_width < 884){
		$("body").css("overflow", "auto");
	}else{
		$("body").css("overflow", "");
	}
		
});







function writeToTable(associations){
	
	//removing useless information
	associations = associations.replace("S',", "");
	associations = associations.replace("'\np0\n.", "");
	//split the string
    console.log(associations.split(".,"));
    associations = associations.split(".,");
	console.log(associations.length);
	
	console.log(associations[0]);
	
	var counter = 7;
	for (var i = 0; i < associations.length; i++){
		assoc  = associations[i].split(",");
		console.log(assoc);
		
		for (var j = 1; j < assoc.length; j++){
			console.log(assoc[j]);
			$("#tg-" + counter).append(assoc[j]);		
			
			//valuation column 
			if ( (counter + 1) % 6 == 0){
				counter = counter + 1;
			}
			
			counter = counter + 1;
			
		}
		
	}
	
	//deleting the useless row into the table
	if (associations.length < 10){
		var associations_lenght = associations.length + 2 ;
		console.log(associations_lenght);
		for(var i = associations_lenght; i < 12; i++){
			$("#row" + i ).remove();
		}
		
		
	}
	
}







var client = new net.Socket();
client.connect(PORT, HOST, function() {
 
    console.log('CONNECTED TO: ' + HOST + ':' + PORT);
    
    client.write("1");
    client.write("130");
    
    
    client.on('data', function(data) {
    	   
    	centroids = data.toString();
    	writeToTable(centroids);
    	
        
        
        // chiude il client socket 
        client.destroy();
     
    });
 
});







function sendToServer(){
	
	var valutations = [];
	var name_html = 12;
	for (var i = 0; i < 6; i++){
		//console.log($("#tg-" + (name_html - 1).toString()).html());

		if(($("#tg-" + (name_html - 1).toString()).html()) != undefined){
			valutations.push($("#s" + name_html).val());
		}
		
		name_html = name_html + 6;
		
	}
	
	//console.log(valutations)
	client.write(valutations);
}

