    var i = 0;
    var imagenes = [];
    var tiempo = 3000;

    //Lista de imagenes
    imagenes[0] = 'static/image/ue1.jpg';
    imagenes[1] = 'static/image/ue2.jpg';
    imagenes[2] = 'static/image/univ1.jpg';

    function changeImg(){
        document.slide.src = imagenes[i];
        if (i < imagenes.length - 1) {
            i++;
        } else {
            i = 0;
        }

        setTimeout("changeImg()", tiempo);
    }
    window.onload = changeImg;

