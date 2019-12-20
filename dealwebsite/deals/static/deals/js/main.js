'use strict';

$(window).on('load', function() {
	/*------------------
		Preloder
	--------------------*/
	$(".loader").fadeOut();
	$("#preloder").delay(400).fadeOut("slow");

});

document.getElementById("tech").addEventListener("click", tech_clicked);
document.getElementById("clothing").addEventListener("click", clothing_clicked);

function tech_clicked(){
	console.log("tech label has been clicked")
}

function clothing_clicked(){
	console.log("clothing label has been clicked")
}

function search_function(search_term){
	console.log("we are searching for "+(document.getElementById("search_term").value))
}

(function($) {
	/*------------------
		Navigation
	--------------------*/
	$(".main-menu").slicknav({
        appendTo: '.header-section',
		allowParentLinks: true,
		closedSymbol: '<i class="fa fa-angle-right"></i>',
		openedSymbol: '<i class="fa fa-angle-down"></i>'
	});

	$('.slicknav_nav').prepend('<li class="header-right-warp"></li>');
    $('.header-right').clone().prependTo('.slicknav_nav > .header-right-warp');

	/*------------------
		Background Set
	--------------------*/
	$('.set-bg').each(function() {
		var bg = $(this).data('setbg');
		$(this).css('background-image', 'url(' + bg + ')');
	});

	/*------------------
        Magnific Popup
    --------------------*/
    $('.video-play').magnificPopup({
        type: 'iframe'
    });


})(jQuery);
