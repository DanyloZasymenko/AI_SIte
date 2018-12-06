function slide(){
	var tlSlider = new TimelineLite();
	tlSlider.to($('.slideHeader'), 0, {y: +window.innerHeight/1.5})
	    			.to($('.slideText'), 0, {y: +window.innerHeight/1.5})
					.to($('.slideHeader'), 0.8, {y: 0, ease: Power1.easeOut, delay: 0.6})
					.to($('.slideText'), 0.8, {y: 0, ease: Power1.easeOut}, "-=0.4");
}
$(document).ready(function(){
	console.log('hello)');
	$("#myCarousel").carousel({pause: false});
	slide();

	$("#carouselExampleIndicators").on('slide.bs.carousel', function(){
	    console.log("has start");
	    slide();
	});

});