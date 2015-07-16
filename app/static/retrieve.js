require(['main'], function (jsonpickle) {

		/* given hash, gets error details using API*/ 
	

	/* sends http get request for errors overview*/
	function get_data(){
		var xhr = new XMLHttpRequest();
		xhr.open('GET', 'http://localhost:5001/list', true);
		xhr.send(null);

		xhr.onreadystatechange = function() {
			if (xhr.readyState == 4 && xhr.status == 200) {
				makeTable(xhr.responseText);
				$(".table > tbody > tr").attr("style", "cursor: pointer");
				$(".table > tbody > tr").click(function() {
					var hash = $(this).find('td:first').text();
					make_details_window(hash);
				});			
			}
			else if (xhr.status != 200)  {	
				document.write("GET request for JSON data failed!");
				document.close();
			}
		};
	}
	
	/* takes json data for all errors and uses it to generate html table elements without error details*/ 
	function makeTable(array_json){
		var array = jsonpickle.decode(array_json);	// convert array json back to array
		var div  = document.getElementById('block');
		var table = document.createElement("table");
		table.setAttribute("id", "table");
		table.setAttribute("class", "table table-hover");
		div.appendChild(table);
		table.innerHTML = "<thead><tr><th>Hash</th><th>Error Message</th><th>First Occurrence</th><th>Most Recent Occurrence</th><th>Count</th></tr></thead>";
		var tablebody = table.appendChild(document.createElement('tbody'));
		
		for(var i=0;i<array.length;i++){
			var tr = document.createElement('tr');   

			var td1 = document.createElement('td');
			var td2 = document.createElement('td');
			var td3 = document.createElement('td');
			var td4 = document.createElement('td');
			var td5 = document.createElement('td');
			
			error_obj_json = array[i]
			error_obj = jsonpickle.decode(error_obj_json)
			
			var text1 = document.createTextNode(error_obj.hash);
			var text2 = document.createTextNode(error_obj.message_string);
			var text3 = document.createTextNode(error_obj.first_occurrence);
			var text4 = document.createTextNode(error_obj.last_occurrence);
			var text5 = document.createTextNode(error_obj.count);

			td1.appendChild(text1);
			td2.appendChild(text2);
			td3.appendChild(text3);
			td4.appendChild(text4);
			td5.appendChild(text5);	
			
			tr.appendChild(td1);
			tr.appendChild(td2);
			tr.appendChild(td3);
			tr.appendChild(td4);
			tr.appendChild(td5);

			tablebody.appendChild(tr);
		}
		
		document.close();
	}
	
	
	function make_details_window(hash) {
		window.open("details.html?hash=" + hash); // or use window.location if errors		
	}

	// main begins
	get_data();
});