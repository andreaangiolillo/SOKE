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







function createJSON_for_graph(top_assoc, article){
	
	$.ajax({
		url: 'data/association_score.csv',
		dataType: 'text',
		success: function (response) {
			
			associations = CSVToArray(response);
			console.log(associations);
			console.log("TOPPPPPP");
			console.log(top_assoc);
			
			var owl_class = [];
			var owl_classAttribute = []
			var owl_prop = [];
			var owl_propertyAttribute = []
			var str = '';
			var id_class = 0;
		
			var dict = {};//Entities' dictionary
			var edge_dict = {};
			var edge_key = "";
			
			for (var i = 1; i < associations.length; i++){
				
				if (article == associations[i][1]){
					//json Class
					if(associations[i][4] == ""){
						//there are only 2 entities 
						
						
						if (dict[associations[i][2]] == undefined) {
							
							//class
							if (top_assoc.search(associations[i][0]) != -1){
								str ='\n{\n "id": "'+id_class+'",\n "type": "owl:Thing"\n}'
								owl_class.push(str);
							}else{
								str ='\n{\n "id": "'+id_class+'",\n "type": "owl:Class"\n}'
								owl_class.push(str);
							}
							
							str = '\n{\n"id" : "'+id_class+'",\n "label" : { \n "undefined" : "'+associations[i][2]+'"\n}\n}';
							owl_classAttribute.push(str);
							
							dict[associations[i][2]] = id_class;//add to dictionary
							id_class = id_class + 1; // id_class
						}
						
						
						
						
						if (dict[associations[i][7]] == undefined) {
							
							//class
							if (top_assoc.search(associations[i][0]) == -1){
								str ='\n{\n "id": "'+id_class+'",\n "type": "owl:Thing"\n}'
								owl_class.push(str);
							}else{
								str ='\n{\n "id": "'+id_class+'",\n "type": "owl:Class"\n}'
								owl_class.push(str);
							}
							
							str = '\n{\n"id" : "'+id_class+'",\n "label" : { \n "undefined" : "'+associations[i][7]+'"\n}\n}';
							owl_classAttribute.push(str);
							
							dict[associations[i][7]] = id_class;//add to dictionary
							id_class = id_class + 1; // id_class
						}
							
							
					
						//edge's attributes
						if(associations[i][3].search("L:") !=  -1){
							edge_key = associations[i][2] + (associations[i][3]).substring(2) + associations[i][7];//creating the key for the dictionary
							if(edge_dict[edge_key] == undefined){
								str = '\n{\n"id" : "'+id_class+'",\n"domain" : "'+ dict[associations[i][2]] +'",\n"range" : "'+ dict[associations[i][7]] +'",\n"label" : { \n "en" : "'+(associations[i][3]).substring(2)+'"\n}\n}\n';
								owl_propertyAttribute.push(str);
								edge_dict[edge_key] = str;
								
								//property (edge)
								str ='\n{\n "id": "'+id_class+'",\n "type": "owl:objectProperty"\n}\n'//edge
								owl_prop.push(str);
								
							}
						}else if (associations[i][3].search("R:") !=  -1){
							edge_key = associations[i][7] + (associations[i][3]).substring(2) + associations[i][2];//creating the key for the dictionary
							if(edge_dict[edge_key] == undefined){
								str = '\n{\n"id" : "'+id_class+'",\n"domain" : "'+ dict[associations[i][7]] +'",\n"range" : "'+ dict[associations[i][2]] +'",\n"label" : { \n "en" : "'+(associations[i][3]).substring(2)+'"\n}\n}\n';
								owl_propertyAttribute.push(str);
								edge_dict[edge_key] = str;
								
								//property (edge)
								str ='\n{\n "id": "'+id_class+'",\n "type": "owl:objectProperty"\n}\n'//edge
								owl_prop.push(str);
								
							}
							
						}else{
							console.log("!!!!!!!!!ERROR!!!!!!!");
						}
							
						
							
						
						id_class = id_class + 1; // id_prop
						
						
					
						
						
					}else{
						// there are 3 entities
						
						
						
						if (dict[associations[i][2]] == undefined) {
							
							//class
						
							if (top_assoc.search(associations[i][0]) == -1){
								str ='\n{\n "id": "'+id_class+'",\n "type": "owl:Thing"\n}'
								owl_class.push(str);
								
								
							}else{
								str ='\n{\n "id": "'+id_class+'",\n "type": "owl:Class"\n}'
								owl_class.push(str);
								
							}
							
							str = '\n{\n"id" : "'+id_class+'",\n "label" : { \n "undefined" : "'+associations[i][2]+'"\n}\n}';
							owl_classAttribute.push(str);
							
							dict[associations[i][2]] = id_class;//add to dictionary
							id_class = id_class + 1; // id_class
						}
						
						
						if (dict[associations[i][4]] == undefined) {
							
							//class
							if (top_assoc.search(associations[i][0]) == -1){
								str ='\n{\n "id": "'+id_class+'",\n "type": "owl:Thing"\n}'
								owl_class.push(str);
							}else{
								str ='\n{\n "id": "'+id_class+'",\n "type": "owl:Class"\n}'
								owl_class.push(str);
							}
							
							str = '\n{\n"id" : "'+id_class+'",\n "label" : { \n "undefined" : "'+associations[i][4]+'"\n}\n}';
							owl_classAttribute.push(str);
							
							dict[associations[i][4]] = id_class;//add to dictionary
							id_class = id_class + 1; // id_class
						}
						
						
				
						
						if (dict[associations[i][7]] == undefined) {
							
							//class
							if (top_assoc.search(associations[i][0]) == -1){
								str ='\n{\n "id": "'+id_class+'",\n "type": "owl:Thing"\n}'
								owl_class.push(str);
							}else{
								str ='\n{\n "id": "'+id_class+'",\n "type": "owl:Class"\n}'
								owl_class.push(str);
							}
							
							str = '\n{\n"id" : "'+id_class+'",\n "label" : { \n "undefined" : "'+associations[i][7]+'"\n}\n}';
							owl_classAttribute.push(str);
							
							dict[associations[i][7]] = id_class;//add to dictionary
							id_class = id_class + 1; // id_class
						}

						
					
							
					
						
						
						if((associations[i][3].search("L:") !=  -1)){
							edge_key = associations[i][2] + (associations[i][3]).substring(2) + associations[i][4];//creating the key for the dictionary
							if((edge_dict[edge_key] == undefined)){
								str = '\n{\n"id" : "'+id_class+'",\n"domain" : "'+ dict[associations[i][2]] +'",\n"range" : "'+ dict[associations[i][4]] +'",\n"label" : { \n "en" : "'+(associations[i][3]).substring(2)+'"\n}\n}';
								owl_propertyAttribute.push(str);
								edge_dict[edge_key] = str;
								
								//property
								str ='\n{\n "id": "'+id_class+'",\n "type": "owl:objectProperty"\n}'
								owl_prop.push(str);
							}
							
						}else if (associations[i][3].search("R:") !=  -1){
							edge_key = associations[i][4] + (associations[i][3]).substring(2) + associations[i][2];//creating the key for the dictionary
							if((edge_dict[edge_key] == undefined)){
								str = '\n{\n"id" : "'+id_class+'",\n"domain" : "'+ dict[associations[i][4]] +'",\n"range" : "'+ dict[associations[i][2]] +'",\n"label" : { \n "en" : "'+(associations[i][3]).substring(2)+'"\n}\n}';
								owl_propertyAttribute.push(str);
								edge_dict[edge_key] = str;
								
								//property
								str ='\n{\n "id": "'+id_class+'",\n "type": "owl:objectProperty"\n}'
								owl_prop.push(str);
							}
							
						}else{
							console.log("!!!!!!!!!ERROR!!!!!!!");
						}
						
						
						
						
						
						id_class = id_class + 1; // id_prop
						
						
					

						
						if(associations[i][6].search("L:") !=  -1){
							edge_key = associations[i][4] + (associations[i][6]).substring(2) + associations[i][7];//creating the key for the dictionary
							if((edge_dict[edge_key] == undefined)){
								str = '\n{\n"id" : "'+id_class+'",\n"domain" : "'+ dict[associations[i][4]] +'",\n"range" : "'+ dict[associations[i][7]] +'",\n"label" : { \n "en" : "'+(associations[i][6]).substring(2)+'"\n}\n}';
								owl_propertyAttribute.push(str);
								edge_dict[edge_key] = str;
								
								//property
								str ='\n{\n "id": "'+id_class+'",\n "type": "owl:objectProperty"\n}'
								owl_prop.push(str);
							}
						}else if (associations[i][6].search("R:") !=  -1){
							edge_key =  associations[i][7] + (associations[i][6]).substring(2) + associations[i][4];//creating the key for the dictionary
							if((edge_dict[edge_key] == undefined)){
								str = '\n{\n"id" : "'+id_class+'",\n"domain" : "'+ dict[associations[i][7]] +'",\n"range" : "'+ dict[associations[i][4]] +'",\n"label" : { \n "en" : "'+(associations[i][6]).substring(2)+'"\n}\n}';
								owl_propertyAttribute.push(str);
								edge_dict[edge_key] = str;
								
								//property
								str ='\n{\n "id": "'+id_class+'",\n "type": "owl:objectProperty"\n}'
								owl_prop.push(str);
							}
							
						}else{
							console.log("!!!!!!!!!ERROR!!!!!!!");
						}
						
						
						id_class = id_class + 1; // id_prop
					
						
						
						
					}
					
				}
				
					
			}
			console.log(owl_class);
			console.log(owl_classAttribute);
			console.log(owl_prop);
			console.log(owl_propertyAttribute);
			console.log(dict);
			
			
			console.log(edge_dict);
			
			
			var start = '{\n"metrics" : {\n"classCount" : 3,\n"datatypeCount" : 0,\n"objectPropertyCount" : 0,\n"datatypePropertyCount" : 0,\n"propertyCount" : 1,\n"nodeCount" : 53,\n"axiomCount" : 216,\n"individualCount" : 8\n},';
			fs.writeFile("data/json/"+article+".json", start + '"class":[' + owl_class+"\n]," + '"classAttribute": [' + owl_classAttribute +"\],"+ '"property": [' + owl_prop + "\]," + '"propertyAttribute": [' +owl_propertyAttribute +"]}") ;
		  }
});
}

























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


function main (article){



	client.connect(PORT, HOST, function() {
		
	    console.log('CONNECTED TO: ' + HOST + ':' + PORT);
	    
	    var first_step = sessionStorage.getItem('first_step' + article);
	    client.write(first_step);
	    client.write("1");
	    client.write($("#flag").val());
	    
	    var i = 0;
	    client.on('data', function(data) {
	    	console.log(first_step);
	    	if (first_step == "true"){
	    		
	    		if ( i == 0){
	        		centroids = data.toString();
	            	writeToTable(centroids);
	            	i = 1;
	            	
	        	}else if (i == 1){
	        		createJSON_for_graph(data.toString(), article );
	        		
	        		sessionStorage.setItem('first_step' + article, 'false');
	        		location.reload();//loading the new KG
	        	
	        		
	        	}
	    		
	    	}else{
	    		
	    		if (i == 0){
	    			console.log(data.toString());
	        		writeToTable(data.toString());
	        		i = 1;
	    		}else if ( i == 1){
	    			createJSON_for_graph(data.toString(), article );
	    			location.reload();//loading the new KG
	    			
	    		}
	    		
	    		
	    	}
	    
	    	
	 
	    
	    });
	 
	});


}




function sendToServer(article){
	
	var valutations = "";
	var name_html = 12;
	var n = 0;
	
	if (sessionStorage.getItem('first_step' + article) == true){
		n = 6;
	}else{
		n = 2;
	}
	
	
	for (var i = 0; i < n; i++){
		

		if(($("#tg-" + (name_html - 1).toString()).html()) != undefined){
			valutations = valutations + ($("#s" + name_html).val()) + ",";
		}
		
		name_html = name_html + 6;
		
	}
	
	console.log(valutations)
	client.write(valutations);
	
	 
 
}

