var textsize = 1;
function changetextsize(up){
    if(up){
        textsize = parseFloat(textsize)+0.2;
    }else{
        textsize =parseFloat(textsize)-0.2;
    };
    fsize(textsize, 'em');
}

function fsize(size,unit){
    document.body.style.fontSize = size + unit;
    createCookie("textsizestyle", textsize, 365);
}

function createCookie(name,value,days) {
    if (days) {
        var date = new Date();
        date.setTime(date.getTime()+(days*24*60*60*1000));
        var expires = "; expires="+date.toGMTString();
    }
    else var expires = "";
    document.cookie = name+"="+value+expires+"; path=/";
}

function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}
