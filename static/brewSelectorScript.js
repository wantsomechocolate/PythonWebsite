//Brew Selector Script
$(document).ready(function(){
	alert("message");
	var $headerText = $('div.header');
	$headerText.click(function(){
		//Past and present headers
		var $selectedHeader = $(this);
		var $currentHeader = $('div.selected');
		//Past and present header Id's
		var $selectedHeaderId = $selectedHeader.attr('id');
		var $currentHeaderId = $currentHeader.attr('id');
		//Changing everything around
		if ($selectedHeaderId !== $currentHeaderId){
			//Past and present content panes
			var $currentContent = $('div.content#'+$currentHeaderId);
			var $selectedContent = $('div.content#'+$selectedHeaderId);
		
			$headerText.removeClass('selected');
			$(this).addClass('selected');
			
			
			$selectedContent.stop().animate({'opacity':'1',
								'height':'150px'},1400);	
					
			$currentContent.stop().animate({'opacity':'0',
									'height':'0px'},700);
			
		
		}
		
		
	
	});

	
	$(function() {
	$('.headerSlider').slider(
				{
					min:0,
					max:10,
					step:1,
					values:[0,10],
					range:true,
					stop: function ( event, vol ) 
						{
							// Use jQuery to select the 'volume' <span> and then
							// set it to the value of the slider.
							$('#volume').html(vol.value)
						}   
				});
	});
	
	$('#attr1 .contentText div').html('The bitterness of a beer is typically associated with the amount of hops,\
								but the bitterness of hops can be counteracted by other ingredients. This \
								should be a measurement of percieved bitterness.');
								
	$('#attr2 .contentText div').html('Mouth feel can be related to temperature, sweetness, and other factors.\
								I don\'t really notice mouth feel unless it is the opposite from what I would expect.\
								The reason I\'m put off by Guiness is because it is a dark beer with a watery mouth feel.');	

	$('#attr3 .contentText div').html('Judy is the best!');
	
	$('#attr4 .contentText div').html('Judy is the best!');
														
	$('#attr5 .contentText div').html('Beers that are more flavorful are typically more expensive. This not only\
								because a more flavorful beer requires more diverse ingredients, but also a\
								more intricate brewing process. Choose your price, just know that it affects the taste!');
	
	$('.headerValue span').html('Any');
	
});

