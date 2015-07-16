/* constructor needed by jsonpickle to convert json to javascript objs */
function Error_Object(__hash, __message_string, __stack_trace, __first_occurrence, __last_occurrence, __url, __method, __count){
	this.hash = __hash;
	this.message_string = __message_string;
	this.stack_trace = __stack_trace;
	this.first_occurrence = __first_occurrence;
	this.last_occurrence = __last_occurrence;
	this.context = new Error_Object.Context(__url, __method);
}

/* also a constructor for jsonpickle */
Error_Object.Context = function(__url, __method){
	this.url = __url;
	this.method = __method;
}