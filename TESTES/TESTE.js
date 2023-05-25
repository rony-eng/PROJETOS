function mudar_modo(){
    var bg = document.querySelector('html')
    if(bg.className === 'light_modo'){
        bg.className = 'dark_modo'
    }else{
        bg.className = 'light_modo'
    }
}
function enviar(){
    var inf_input = document.querySelector('.inp_t1').value
    var textarea = document.querySelector('.textarea')

    if(inf_input != ''){
        textarea.value = inf_input
    }
}
