$(document).ready(function() {
    
    var blog = window.setTimeout( function(){
        get_last_post();
    },1000);
    
});

function get_last_post () {
    var postwrapper=$('#postwrapper');
    $.post('myapp.com/last_post',function(data, textStatus, xhr) {
		var post=$.parseJSON(data);
        if(post.status=="ok"){
            var title=$('<h1></h1>').text(post.title);
            var descripction=$('<p></p>').text(post.descripction);
            var link=$('<a></a>').text('Read more').attr('href',post.url);
            postwrapper.empty().append(title).append(descripction).append(link);
        }
    });
}