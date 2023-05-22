function bnt_off(){
    var container = document.querySelector('body');
    var bnt_lampanda_off = document.querySelector('.bnt_off')
    var bnt_lampanda_on = document.querySelector('.bnt_on')
    var img_on = document.querySelector('.lampanda_on')
    var img_off = document.querySelector('.lampanda_off')

    if (container.style.backgroundColor === 'white'){
        container.style.backgroundColor = 'black'
        bnt_lampanda_off.style.display = 'none'
        bnt_lampanda_on.style.display = 'block'
        img_on.style.display = 'none'
        img_off.style.display = 'block'
    }
    else{
        container.style.backgroundColor = 'white'
        bnt_lampanda_off.style.display = 'block'
        bnt_lampanda_on.style.display = 'none'
        img_on.style.display = 'block'
        img_off.style.display = 'none'
    }
}
function bnt_on(){
    var container = document.querySelector('body');
    var bnt_lampanda_off = document.querySelector('.bnt_off')
    var bnt_lampanda_on = document.querySelector('.bnt_on')
    var img_on = document.querySelector('.lampanda_on')
    var img_off = document.querySelector('.lampanda_off')

    if (container.style.backgroundColor === 'black'){
        container.style.backgroundColor = 'white'
        bnt_lampanda_off.style.display = 'block'
        bnt_lampanda_on.style.display = 'none'
        img_on.style.display = 'block'
        img_off.style.display = 'none'
    }
    else{
        container.style.backgroundColor = 'black'
        bnt_lampanda_off.style.display = 'none'
        bnt_lampanda_on.style.display = 'block'
        img_on.style.display = 'none'
        img_off.style.display = 'block'
    }
}