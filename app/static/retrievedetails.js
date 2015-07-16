require(['main'], function (jsonpickle) {

	function get_details(hash){
		var xhr = new XMLHttpRequest();

		xhr.open('GET', 'http://localhost:5001/list/' + hash, true);
		xhr.send(null);

		xhr.onreadystatechange = function() {
			if (xhr.readyState == 4 && xhr.status == 200) {
				make_details_window(xhr.responseText);
			}
			else if (xhr.status != 200) {
				document.write("GET request for JSON data failed!");
				document.close();
			}		
		};
	}

	/* makes new page with table containing error details */
	function make_details_window(detailed_error_json) {
		var detailed_error = jsonpickle.decode(detailed_error_json);
		var div = document.getElementById('block');
		var table = document.createElement("table");
		table.setAttribute("id", "table");
		table.setAttribute("class", "table table-hover");
		div.appendChild(table);
		table.innerHTML = "<thead><tr><th>Hash</th><th>Error Message</th><th>First Occurrence</th><th>Most Recent Occurrence</th><th>Count</th><th>URL</th><th>Method</th><th>Stack Trace</th></tr></thead>";
		var tablebody = table.appendChild(document.createElement('tbody'));

		var tr = document.createElement('tr');   

		var td1 = document.createElement('td');
		var td2 = document.createElement('td');
		var td3 = document.createElement('td');
		var td4 = document.createElement('td');
		var td5 = document.createElement('td');
		var td6 = document.createElement('td');
		var td7 = document.createElement('td');
		var td8 = document.createElement('td');
		

		var text1 = document.createTextNode(detailed_error.hash);
		var text2 = document.createTextNode(detailed_error.message_string);
		var text3 = document.createTextNode(detailed_error.first_occurrence);
		var text4 = document.createTextNode(detailed_error.last_occurrence);
		var text5 = document.createTextNode(detailed_error.count);
		var text6 = document.createTextNode(detailed_error.context.url);
		var text7 = document.createTextNode(detailed_error.context.method);
		var text8 = document.createTextNode(detailed_error.stack_trace);

		td1.appendChild(text1);
		td2.appendChild(text2);
		td3.appendChild(text3);
		td4.appendChild(text4);
		td5.appendChild(text5);	
		td6.appendChild(text6);	
		td7.appendChild(text7);	
		td8.appendChild(text8);	
		
		tr.appendChild(td1);
		tr.appendChild(td2);
		tr.appendChild(td3);
		tr.appendChild(td4);
		tr.appendChild(td5);
		tr.appendChild(td6);
		tr.appendChild(td7);
		tr.appendChild(td8);

		tablebody.appendChild(tr);
		
		document.close();
	}

	// this main here
	var hash_from_url = location.search.split('hash=')[1]
	document.title = hash_from_url;
	get_details(hash_from_url);


});