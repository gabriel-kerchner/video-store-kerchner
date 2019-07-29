$(document).ready(function() {
    $("#searchMovie").keyup(function(){
        $.ajax({
            type: "GET",
            datatype: "html",
            url: "search/",
            data: {
                'titulo': $('#searchMovie').val(),
            },
            success: function (data) {
                $('#ajax').html(data)
            }
        });
    
    });
});

$(document).ready(function() {
    $("#favorite").click(function(){
        $.ajax({
            type: "GET",
            datatype: "html",
            url: "search/",
            data: {
                'titulo': $('#searchMovie').val(),
            },
            success: function (data) {
                $('#ajax').html(data)
            }
        });
    
    });
});



    
