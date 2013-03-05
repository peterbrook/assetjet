

with (jqUnit) {
	module('With local interface');
	test('Test AssetJet object exists', function(){
		ok(window.AJ);
	});
	module('With local interface');
	test('AJ Datre manipulation', function(){

		var dt = new Date(2013, 03, 01);
		console.log(dt.isoFormat());
	});
    
}(jQuery);
