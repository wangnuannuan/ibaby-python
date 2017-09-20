$('.light').click( function() {
    if( $('.light').hasClass('lightoff') ) {
        $('.light').removeClass('lightoff').addClass('lighton');
        }
    else {
        ('.light').removeClass('lighton').addClass('lightoff');
    }
});