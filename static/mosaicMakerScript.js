//Mosaic Maker Script
$(document).ready(function(){
	
	$('#centerPane').click(function(){
		
		$.get('SuperImportantData/mosaicMakerProgData.log', function(data) {
			
			alert(data);
		
		}, 'text');
		
	});
	
});