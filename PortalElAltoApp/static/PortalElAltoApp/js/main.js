$(document).ready(function(){

    //$('.slider .slider-link').hide();//ocukltamos todos los slider
    //$('.slider .slider-link:first').show();//Mostramos el primer slider
    //alert('funciono')
    
    var imgItems = $('.slider .slider-link').length;//numero de SLider
    var imgPos = 1;

    console.log(imgItems);

    //Agregando paginacion--
    for(i = 1; i<=imgItems; i++){
        $('.pagination').append('<li class="pagItem"><span class="fa fa-circle"></span></li>');
    }

    $('.slider .slider-link').hide();//ocukltamos todos los slider
    $('.slider .slider-link:first').show();//Mostramos el primer slider
    $('.pagination .pagItem:first').css({'color':'#CD6E2E'});//Damos estilos al primer Item de la paginancion

    //Ejecutamos todas funciones
    $('.pagination .pagItem').click(pagination);
    $('.right span').click(nextSlider);
    $('.left span').click(prevSlider);

    //========================================
    setInterval(function(){
        nextSlider();
    }, 4000);

    //==============FUNCIONES==============

    function pagination(){

        var paginationPos = $(this).index() + 1;
        //console.log(paginationPos);

        $('.slider .slider-link').hide();
        $('.slider .slider-link:nth-child('+ paginationPos +')').fadeIn();
        //Dandolde estilos a la paginacin seleccionar
        $('.pagination .pagItem').css({'color': '#ffbb00'});
        $(this).css({'color': '#CD6E2E'});

        imgPos = paginationPos;

    }

    function nextSlider(){
        if(imgPos >= imgItems){
            imgPos = 1;
        }else{
            imgPos++;
        }

        $('.pagination .pagItem').css({'color': '#ffbb00'});
        $('.pagination .pagItem:nth-child('+imgPos+')').css({'color': '#CD6E2E'});

        $('.slider .slider-link').hide();//Ocultamos todos los sliders
        $('.slider .slider-link:nth-child('+imgPos+')').fadeIn();//mostramos el slider selecciondo
    }
    function prevSlider(){
        if(imgPos <= 1){
            imgPos = imgItems;
        }else{
            imgPos--;
        }

        $('.pagination .pagItem').css({'color': '#ffbb00'});
        $('.pagination .pagItem:nth-child('+imgPos+')').css({'color': '#CD6E2E'});

        $('.slider .slider-link').hide();//Ocultamos todos los sliders
        $('.slider .slider-link:nth-child('+imgPos+')').fadeIn();//mostramos el slider selecciondo
    }
  


});