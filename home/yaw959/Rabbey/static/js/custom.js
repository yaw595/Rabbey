$(".heart.fa").click(function() {
  $(this).toggleClass("fa-heart fa-heart-o");
});

$(document).ready(function() {
  var scroll_start = 0;
  var startchange = $('.stc');
  var offset = startchange.offset();
    if (startchange.length) {
$(document).scroll(function() {
  scroll_start = $(this).scrollTop(); 
  if(scroll_start > offset.top){
      $('.navbar').css('background-color', '#000000');
      $('.navbar').css('transition', 'all ease-in-out 0.75s');
  } else {
      $('.navbar').css('background-color', 'transparent');
  }
});
    }
});

$(document).hover(function() {
   $('.dropdown').hover(function() {
     $(this).find('.dropdown-menu').stop(true, true).delay(300).show(500);
   }, function() {
     $(this).find('.dropdown-menu').stop(true, true).delay(300).hide(500);
   });
 });


/**
 * $(document).hover(function() {
   $('.dropdown').hover(function() {
     $(this).find('.dropdown-menu').stop(true, true).delay(300).fadeIn(500);
   }, function() {
     $(this).find('.dropdown-menu').stop(true, true).delay(300).fadeOut(500);
   });
 });
 */


$(Window).scroll(function() {
  var scrollTop = $(this).scrollTop();
  $('.header-bg').css('top', (scrollTop * 0.37) + 'px');
  $('.htxt').css('opacity', 1 - $(Window).scrollTop() / 450);
  $('.ltxt').css('opacity', 1 - $(Window).scrollTop() / 450);
});


$(document).ready(function(){
  $(Window).scroll(function(){
    if ($(this).scrollTop() > 100) {
        $('.fa-angle-up').fadeIn();
    } else {
        $('.fa-angle-up').fadeOut();
    }
});
$('.fa-angle-up').click(function(){
    $('html, body').animate({scrollTop: 0},
 2500);
    return false;
  });
});

$('.show').click(function () {
  $('#TMSG').show(500);
});

$('#scrBtn').click(function(){
    var offset = 20;
    $('html, body').animate({
        scrollTop: $('#stc').offset().top + offset
    }, 1000)
});