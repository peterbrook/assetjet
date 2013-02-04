Components.utils.import("resource://foo/bar.js");
(function(root, $, _, Backbone, undefined){
	"use strict";
	
	// setup
	if(!_.isDefined(root.AJ)){
		return;
	}
	var AJ = root.AJ = {
		VERSION = "0.1",
		rootUrl = "127.0.0.1:80"
	};

	// String convenience functions
	String.format = function() {
		var s = arguments[0];
	  	for (var i = 0; i < arguments.length - 1; i++) {       
	    	var reg = new RegExp("\\{" + i + "\\}", "gm");             
	    	s = s.replace(reg, arguments[i + 1]);
	  	}
		return s;
	};
		
	AJ.getCSV = function(url){
		$.get(url, 
			function(data){
			    var dataStr = new String(data);
			    var lines = dataStr.split('\n');
			    return lines;
			},
			dataType='text'
			async = false
		);
	};
	AJ.curl = function(url) {
		if (window.XMLHttpRequest) {              
			AJAX=new XMLHttpRequest();              
		} else {                                  
			AJAX=new ActiveXObject("Microsoft.XMLHTTP");
		}
		if (AJAX) {
			AJAX.open("GET", url, false);                             
			AJAX.send(null);
			return AJAX.responseText;                                         
		} else {
			return false;
		}                                             
	};

	AJ.sendRequest = function(url,callback,postData) {
	    var req = createXMLHTTPObject();
	    if (!req) return;
	    var method = (postData) ? "POST" : "GET";
	    req.open(method,url,true);
	    req.setRequestHeader('User-Agent','XMLHTTP/1.0');
	    if (postData)
	        req.setRequestHeader('Content-type','application/x-www-form-urlencoded');
	    req.onreadystatechange = function () {
	        if (req.readyState != 4) return;
	        if (req.status != 200 && req.status != 304) {
	//          alert('HTTP error ' + req.status);
	            return;
	        }
	        callback(req);
	    }
	    if (req.readyState == 4) return;
	    req.send(postData);
	}

	AJ.XMLHttpFactories = [
	    function () {return new XMLHttpRequest()},
	    function () {return new ActiveXObject("Msxml2.XMLHTTP")},
	    function () {return new ActiveXObject("Msxml3.XMLHTTP")},
	    function () {return new ActiveXObject("Microsoft.XMLHTTP")}
	];

	AJ.createXMLHTTPObject = function() {
	    var xmlhttp = false;
	    for (var i=0;i<XMLHttpFactories.length;i++) {
	        try {
	            xmlhttp = XMLHttpFactories[i]();
	        }
	        catch (e) {
	            continue;
	        }
	        break;
	    }
	    return xmlhttp;
	};

	var yahooUrl = "http://query.yahooapis.com/v1/public/yql?[query_params]";

	AJ.getYahooData = function(symbol, startDate, endDate, period, callback){
		if(!startDate){
			startDate = new Date();
			endDate = new Date();
			startDate.setMonth(endDate.getMonth() - 12);
		}
		var rootUrl = "http://ichart.finance.yahoo.com/table.csv?s={0}&a={1}&b={2}&c={3}&d={4}&e={5}&f={6}&y={7}&g={9}&ignore=.csv"
		var queryUrl = String.format(
			rootUrl,
			symbol,
			startDate.getMonth(), startDate.getDay(), startDate.getFullYear(), 
			endDate.getMonth(), endDate.getDay(), endDate.getFullYear(),
			"d"
		);

		var data;
		//data = AJ.curl(queryUrl);
		//return data;

		$.ajax({
	         url:    	queryUrl,
	         async:   false,
	         dataType: "text",
	         success: 	function(result) {
	         				console.log(result);
	                      	if(result.isOk == false){
	                        	alert(result.message);
	                      	}else{
	                      		data = result;
	                      	}
	                  	},
	         complete: 	function(result, status) {
	         				console.log(result);
	         				console.log(status);
	                      	if(result.isOk == false){
	                        	alert(result.message);
	                      	}else{
	                      		data = result;
	                      	}
							return data;
	                  	},
	    });          
	};

})(window, $, _, Backbone);




