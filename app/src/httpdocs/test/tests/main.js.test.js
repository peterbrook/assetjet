

with (jqUnit) {
	test('Test AssetJet object exists', function(){
		ok(window.AJ);
	});
	test('AJ Date manipulation', function(){
		var dt = new Date(2013, 3, 1);
		console.log(dt.isoFormat());
	});
	test('AJ Date manipulation 2', function(){
		var dt = new Date("2013-03-01");
		console.log(dt.isoFormat());
		ok(dt.isoFormat() === "2013-3-1T0:0:0.0");
	});    
}(jQuery);
