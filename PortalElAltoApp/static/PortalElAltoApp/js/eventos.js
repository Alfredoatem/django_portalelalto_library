
$(document).ready(function(){
    
    var swiper = new Swiper('.swiper-container', {
    slidesPerView: 5,
    centeredSlides: true,
    spaceBetween: 60,
    grabCursor: true,
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
  });
});