(function(root, $, _, Backbone, undefined){
	"use strict";
	
	// setup
	if(!_.isUndefined(root.AJ)){
		return;
	}
	var AJ = root.AJ = {
		VERSION : "0.1"
	,	rootUrl :"http://127.0.0.1:8080"
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
	
	// String convenience functions
	String.prototype.format = function() {
		var s = this;
	  	for (var i = 0; i < arguments.length; i++) {       
	    	var reg = new RegExp("\\{" + i + "\\}", "gm");             
	    	s = s.replace(reg, arguments[i]);
	  	}
		return s;
	};
	
	Date.prototype.getDayRebased = function(base){
		return this.getUTCDate();
		if(!base){
			// assume base 10
			return parseInt(10, this.getUTCDate());
		} else {
			return parseInt(base, this.getUTCDate());
		}
	};
	
	Date.prototype.getMonthRebased = function(base){
		var mth = this.getMonth() + 1;
		if(!base){
			// assume base 10
			return parseInt(10, mth);
		} else {
			return parseInt(base, mth);
		}
	};

	Date.prototype.isoFormat = function(){
		return "{0}-{1}-{2}T{3}:{4}:{5}.{6}".format(
			this.getFullYear(), this.getMonthRebased(), this.getDayRebased(), 
			this.getHours(), this.getMinutes(), this.getSeconds(), 
			this.getMilliseconds()
		); 
	};
		
	// parse a date in yyyy-mm-dd format
	Date.parseDate = function (input) {
	    var parts = input.match(/(\d+)/g);
	    return new Date(parts[0], parts[1]-1, parts[2]);
	};
	Date.prototype.getTicks = function(){
		return (this.getTime() * 10000) + 621355968000000000;

	}
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
		var serviceUrl = AJ.rootUrl + "/services/Prices/GetByTicker/?ticker={0}&startDate={1}&endDate={2}&period={3}"
		var queryUrl = String.format(
			serviceUrl,
			symbol,
			startDate.isoFormat(), 
			endDate.isoFormat(),
			(period || "d")
		);
		$.jsonp({
	        url:    	queryUrl
        ,   success: 	callback
        ,   error: 		function(result, status){
                console.log(result);
                console.log(status);
            }
	    });          
	};
})(window, $, _, Backbone);
