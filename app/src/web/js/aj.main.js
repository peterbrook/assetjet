//Utils = {}
//Utils.import


//Components.utils.import("resource://lib/jquery.js");
//Components.utils.import("resource://lib/jquery.jsonp.js");
//Components.utils.import("resource://lib/modernizr-min.js");
//Components.utils.import("resource://lib/bootstrap-min.js");
//Components.utils.import("resource://lib/underscore-min.js");
//Components.utils.import("resource://lib/backbone-min.js");

(function(root, $, _, Backbone, undefined){
	"use strict";
	
	// setup
	if(!_.isUndefined(root.AJ)){
		return;
	}
	var AJ = root.AJ = {
		VERSION : "0.1",
		rootUrl :"http://127.0.0.1:8080"
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
		$.jsonp(url, 
			function(data){
			    var dataStr = new String(data);
			    var lines = dataStr.split('\n');
			    return lines;
			},
			dataType='text',
			async = false
		);
	};
	AJ.curl = function(url) {
		var AJAX = window.AJAX;
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
			(period || "d")
		);
		
		rootUrl = AJ.rootUrl + "/services/Prices/GetByTicker/ticker={0}&startDate={1}&endDate={2}&period={3}"
		var queryUrl = String.format(
			rootUrl,
			symbol,
			startDate, 
			endDate,
			(period || "d")
		);

		var data;
		//data = AJ.curl(queryUrl);
		//return data;

		$.ajax({
	         url:    	queryUrl,
	         async:   	false,
	         dataType: 	"text",
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
	                  	}
	    });          
	};

})(window, $, _, Backbone);




