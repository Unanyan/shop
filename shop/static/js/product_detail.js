$(document).ready(function () {
    $('.row .col-3:lt(4)').show();
    var items = 100;
    $('#more').click(function () {
        shown = $('.row .col-3:visible').length+4;
        $('.row .col-3:lt('+items+')').show(350);
        $('#more').hide();
    });
});

$(document).ready(function () {
    $('.row .col-6:lt(2)').show();
    var items = 100;
    $('#more-mobile').click(function () {
        shown = $('.row .col-6:visible').length+2;
        $('.row .col-6:lt('+items+')').show(500);
        $('#more-mobile').hide();
    });
});
