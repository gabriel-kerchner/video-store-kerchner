$(document).ready(function (){

    var source = $("#test-template").html();
    var template = Handlebars.compile(source);

    var context = {
        title: "Seja bem vindo(a) a Locadora Kerchner!",
        movies: '"Filmes"'
    }
    var implement = template(context);
    $("#handle").html(implement);
 
});

$(document).ready(function(){
	var uri = window.location.toString();
	if (uri.indexOf("?") > 0) {
	    var clean_uri = uri.substring(0, uri.indexOf("?"));
	    window.history.replaceState({}, document.title, clean_uri);
	}
});

//  Set caption from card text
$('.card-deck a').fancybox({
    caption : function( instance, item ) {
      return $(this).parent().find('.card-text').html();
    }
  });

$(document).ready(function (){

    $('#addList').click().style.visibility = 'hidden'
    $("#removeList").click().style.visibility = 'visible';

});

