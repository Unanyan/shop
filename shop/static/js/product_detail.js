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
    $('.row .col-4:lt(3)').show();
    var items = 100;
    $('#more-mobile').click(function () {
        shown = $('.row .col-4:visible').length+3;
        $('.row .col-4:lt('+items+')').show(350);
        $('#more-mobile').hide();
    });
});

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("demo");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
