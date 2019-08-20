let loginscroll = $('html, body');
$('a').click(function () {
    loginscroll.animate({
        scrollTop: $($.attr(this, 'href')).offset().top
    }, 500);
    return false;
});

