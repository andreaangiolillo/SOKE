var $ = require('jquery');
var fs = require('fs');



//ref: http://stackoverflow.com/a/1293163/2343
// This will parse a delimited string into an array of
// arrays. The default delimiter is the comma, but this
// can be overriden in the second argument.
function CSVToArray( strData){
    // Check to see if the delimiter is defined. If not,
    // then default to comma.
    strDelimiter = (",");

    // Create a regular expression to parse the CSV values.
    var objPattern = new RegExp(
        (
            // Delimiters.
            "(\\" + strDelimiter + "|\\r?\\n|\\r|^)" +

            // Quoted fields.
            "(?:\"([^\"]*(?:\"\"[^\"]*)*)\"|" +

            // Standard fields.
            "([^\"\\" + strDelimiter + "\\r\\n]*))"
        ),
        "gi"
        );


    // Create an array to hold our data. Give the array
    // a default empty first row.
    var arrData = [[]];

    // Create an array to hold our individual pattern
    // matching groups.
    var arrMatches = null;


    // Keep looping over the regular expression matches
    // until we can no longer find a match.
    while (arrMatches = objPattern.exec( strData )){

        // Get the delimiter that was found.
        var strMatchedDelimiter = arrMatches[ 1 ];

        // Check to see if the given delimiter has a length
        // (is not the start of string) and if it matches
        // field delimiter. If id does not, then we know
        // that this delimiter is a row delimiter.
        if (
            strMatchedDelimiter.length &&
            strMatchedDelimiter !== strDelimiter
            ){

            // Since we have reached a new row of data,
            // add an empty row to our data array.
            arrData.push( [] );

        }

        var strMatchedValue;

        // Now that we have our delimiter out of the way,
        // let's check to see which kind of value we
        // captured (quoted or unquoted).
        if (arrMatches[ 2 ]){

            // We found a quoted value. When we capture
            // this value, unescape any double quotes.
            strMatchedValue = arrMatches[ 2 ].replace(
                new RegExp( "\"\"", "g" ),
                "\""
                );

        } else {

            // We found a non-quoted value.
            strMatchedValue = arrMatches[ 3 ];

        }


        // Now that we have our value string, let's add
        // it to the data array.
        arrData[ arrData.length - 1 ].push( strMatchedValue );
    }

    // Return the parsed data.
    return( arrData );
}





function createJSON_for_graph(){
	
	$.ajax({
		url: 'data/association_score.csv',
		dataType: 'text',
		success: function (response) {
			
			associations = CSVToArray(response);
			console.log(associations);
			var article = "130";
			
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
							str ='\n{\n "id": "'+id_class+'",\n "type": "owl:Class"\n}'
							owl_class.push(str);
							
							str = '\n{\n"id" : "'+id_class+'",\n "label" : { \n "undefined" : "'+associations[i][2]+'"\n}\n}';
							owl_classAttribute.push(str);
							
							dict[associations[i][2]] = id_class;//add to dictionary
							id_class = id_class + 1; // id_class
						}
						
						
						
						
						if (dict[associations[i][7]] == undefined) {
							
							//class
							str ='\n{\n "id": "'+id_class+'",\n "type": "owl:Class"\n}'
							owl_class.push(str);
							
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
							str ='\n{\n "id": "'+id_class+'",\n "type": "owl:Class"\n}'
							owl_class.push(str);
							
							str = '\n{\n"id" : "'+id_class+'",\n "label" : { \n "undefined" : "'+associations[i][2]+'"\n}\n}';
							owl_classAttribute.push(str);
							
							dict[associations[i][2]] = id_class;//add to dictionary
							id_class = id_class + 1; // id_class
						}
						
						
						if (dict[associations[i][4]] == undefined) {
							
							//class
							str ='\n{\n "id": "'+id_class+'",\n "type": "owl:Class"\n}'
							owl_class.push(str);
							
							str = '\n{\n"id" : "'+id_class+'",\n "label" : { \n "undefined" : "'+associations[i][4]+'"\n}\n}';
							owl_classAttribute.push(str);
							
							dict[associations[i][4]] = id_class;//add to dictionary
							id_class = id_class + 1; // id_class
						}
						
						
				
						
						if (dict[associations[i][7]] == undefined) {
							
							//class
							str ='\n{\n "id": "'+id_class+'",\n "type": "owl:Class"\n}'
							owl_class.push(str);
							
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



