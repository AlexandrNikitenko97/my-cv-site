// Sidebar toggle script
$("#menu-toggle").click( function (e){
        e.preventDefault();
        $("#wrapper").toggleClass("menuDisplayed");
    });


// home arrow

$(document).ready(function() {

	var 
		move=true;
		pixels=0;
		timer = setInterval(function() {
				if(pixels <= 20 && move){
					pixels++;
					if(pixels==20){
						move = false;
					}
				}
				else{
					pixels--;
					if(pixels==0){
						move = true;
					}
				}	
				$('.home-header').css('padding-left', pixels+'px');
		}, 40);

});



$(document).ready(function(){
		var copy_hello = new String;
		copy_hello = $('.home-hello span').text();
		$('.home-hello span').text('');
		var string_len=copy_hello.length;
		letter=0;
		setInterval(function(){
			if(letter<string_len){
				$('.home-hello span').text($('.home-hello span').text()+copy_hello[letter]);
				letter++; 
			}
			else{
				$('.home-hello .after').removeClass('after')
			}  
		},120);
});



$(document).ready(function typing(){
		var copy_iam = new String;
		copy_iam = $('.home-text span').text();
		$('.home-text span').text('');
		var string1_len=copy_iam.length;
		letter1=0;
		setInterval(function(){
			if(letter1<string1_len){
				$('.home-text span').text($('.home-text span').text()+copy_iam[letter1]);
				letter1++; 
			} 
		},215);
});
