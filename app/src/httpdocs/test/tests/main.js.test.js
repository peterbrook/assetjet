

with (jqUnit) {
	module('With local interface');
	test('Test AJ exists', function(){
		ok(window.AJ);
	});
}(jQuery);
