
(function(root, $, _, Backbone, undefined){
	"use strict";

	var margin = {top: 10, right: 10, bottom: 20, left: 40},
	    width = 960 - margin.left - margin.right,
	    height = 500 - margin.top - margin.bottom;

	var x = d3.scale.linear()
	    .domain([0, 1])
	    .range([0, width]);

	var y = d3.scale.linear()
	    .domain([0, 1])
	    .range([height, 0]);

	var xAxis = d3.svg.axis()
	    .scale(x)
	    .orient("bottom");

	var yAxis = d3.svg.axis()
	    .scale(y)
	    .orient("left");

	var line = d3.svg.line()
	    .x(function(d) { return x(d.x); })
	    .y(function(d) { return y(d.y); });

	var svg = d3.select("body").append("svg")
	    .datum(data)
	    .attr("width", width + margin.left + margin.right)
	    .attr("height", height + margin.top + margin.bottom)
	  .append("g")
	    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

	svg.append("g")
	    .attr("class", "x axis")
	    .attr("transform", "translate(0," + height + ")")
	    .call(xAxis);

	svg.append("g")
	    .attr("class", "y axis")
	    .call(yAxis);

	svg.append("path")
	    .attr("class", "line")
	    .attr("d", line);

	svg.selectAll(".dot")
	    .data(data)
	  .enter().append("circle")
	    .attr("class", "dot")
	    .attr("cx", line.x())
	    .attr("cy", line.y())
	    .attr("r", 3.5);

})(window, $, _, Backbone);

