var i = 0;
var imagenes = [];
var tiempo = 3000;

//Lista de imagenes
imagenes[0] = 'static/PortalElAltoApp/image/publicidad/pub1.jpg';
imagenes[1] = 'static/PortalElAltoApp/image/publicidad/pub2.jpg';
imagenes[2] = 'static/PortalElAltoApp/image/publicidad/pub3.jpg';

function changeImg(){
    document.slideaside.src = imagenes[i];
    if (i < imagenes.length - 1) {
        i++;
    } else {
        i = 0;
    }

    setTimeout("changeImg()", tiempo);
}
window.onload = changeImg;
