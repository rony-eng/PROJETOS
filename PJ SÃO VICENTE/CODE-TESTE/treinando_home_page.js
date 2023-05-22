// aqui fica voltado para a página da história de são vicente
function bnt_historia_sv(){
    var container = document.querySelector('.historia_sv');
    var divp = document.querySelector('.div_hp')
    var div_perfil = document.querySelector('.div_perfil')
    var div_missa = document.querySelector('.div_missa')
    var div_eventos = document.querySelector('.div_eventos')
    var div_calendário = document.querySelector('.div_calendario')
    var div_arquivos = document.querySelector('.div_arquivos')
    var div_configurações = document.querySelector('.div_configuracoes')

    if(container.style.display === 'none'){
        container.style.display = 'flex';
        divp.style.display = 'none';
        div_perfil.style.display = 'none';
        div_missa.style.display = 'none';
        div_eventos.style.display = 'none';
        div_calendário.style.display = 'none';
        div_arquivos.style.display = 'none';
        div_configurações.style.display = 'none';
    }else{
        container.style.display = 'none';
        divp.style.display = 'flex';
        div_perfil.style.display = 'none';
        div_missa.style.display = 'none';
        div_eventos.style.display = 'none';
        div_calendário.style.display = 'none';
        div_arquivos.style.display = 'none';
        div_configurações.style.display = 'none';
    }
}
function bnt_sair_historia_sv(){
    var container = document.querySelector('.historia_sv');
    var divp = document.querySelector('.div_hp')

    if(container.style.display === 'flex'){
        container.style.display = 'none';
    }else{
        container.style.display = 'flex'
    }

    if(divp.style.display === 'none'){
        divp.style.display = 'flex';
    }else{
        divp.style.display = 'none';
    }
}

// aqui fica voltado para a página de perfil
function bnt_perfil(){
    var container = document.querySelector('.div_perfil')
    var divp = document.querySelector('.div_hp')
    var div_historia_sv = document.querySelector('.historia_sv')
    var div_missa = document.querySelector('.div_missa')
    var div_eventos = document.querySelector('.div_eventos')
    var div_calendário = document.querySelector('.div_calendario')
    var div_arquivos = document.querySelector('.div_arquivos')
    var div_configurações = document.querySelector('.div_configuracoes')

    if(container.style.display === 'none'){
        container.style.display = 'flex';
        divp.style.display = 'none';
        div_historia_sv.style.display = 'none';
        div_missa.style.display = 'none';
        div_eventos.style.display = 'none';
        div_calendário.style.display = 'none';
        div_arquivos.style.display = 'none';
        div_configurações.style.display = 'none';
    }else{
        container.style.display = 'none';
        divp.style.display = 'flex';
        div_historia_sv.style.display = 'none';
        div_missa.style.display = 'none';
        div_eventos.style.display = 'none';
        div_calendário.style.display = 'none';
        div_arquivos.style.display = 'none';
        div_configurações.style.display = 'none';
    }
}

// aqui fica voltado para a página de missa e intenções
function bnt_missa(){
    var container = document.querySelector('.div_missa')
    var divp = document.querySelector('.div_hp')
    var div_historia_sv = document.querySelector('.historia_sv')
    var div_perfil = document.querySelector('.div_perfil')
    var div_eventos = document.querySelector('.div_eventos')
    var div_calendário = document.querySelector('.div_calendario')
    var div_arquivos = document.querySelector('.div_arquivos')
    var div_configurações = document.querySelector('.div_configuracoes')

    if(container.style.display === 'none'){
        container.style.display = 'flex';
        divp.style.display = 'none';
        div_historia_sv.style.display = 'none';
        div_perfil.style.display = 'none';
        div_eventos.style.display = 'none';
        div_calendário.style.display = 'none';
        div_arquivos.style.display = 'none';
        div_configurações.style.display = 'none';
    }else{
        container.style.display = 'none'
        divp.style.display = 'flex';
        div_historia_sv.style.display = 'none';
        div_perfil.style.display = 'none';
        div_eventos.style.display = 'none';
        div_calendário.style.display = 'none';
        div_arquivos.style.display = 'none';
        div_configurações.style.display = 'none';
    }
}

// aqui fica voltado para a página de eventos
function bnt_eventos(){
    var container = document.querySelector('.div_eventos');
    var divp = document.querySelector('.div_hp')
    var div_historia_sv = document.querySelector('.historia_sv')
    var div_perfil = document.querySelector('.div_perfil')
    var div_configuracoes = document.querySelector('.div_configuracoes')
    var div_calendário = document.querySelector('.div_calendario')
    var div_arquivos = document.querySelector('.div_arquivos')
    var div_missa = document.querySelector('.div_missa')

    if(container.style.display === 'none'){
        container.style.display = 'flex';
        divp.style.display = 'none';
        div_historia_sv.style.display = 'none';
        div_perfil.style.display = 'none';
        div_configuracoes.style.display = 'none';
        div_calendário.style.display = 'none';
        div_arquivos.style.display = 'none';
        div_missa.style.display = 'none';
    }else{
        container.style.display = 'none'
        divp.style.display = 'flex';
        div_historia_sv.style.display = 'none';
        div_perfil.style.display = 'none';
        div_configuracoes.style.display = 'none';
        div_calendário.style.display = 'none';
        div_arquivos.style.display = 'none';
        div_missa.style.display = 'none';
    }
}

// aqui fica voltado para a página de calendário
function bnt_calendario(){
    var container = document.querySelector('.div_calendario');
    var divp = document.querySelector('.div_hp')
    var div_historia_sv = document.querySelector('.historia_sv')
    var div_perfil = document.querySelector('.div_perfil')
    var div_eventos = document.querySelector('.div_eventos')
    var div_configuracoes = document.querySelector('.div_configuracoes')
    var div_arquivos = document.querySelector('.div_arquivos')
    var div_missa = document.querySelector('.div_missa')

    if(container.style.display === 'none'){
        container.style.display = 'flex';
        divp.style.display = 'none';
        div_historia_sv.style.display = 'none';
        div_perfil.style.display = 'none';
        div_eventos.style.display = 'none';
        div_configuracoes.style.display = 'none';
        div_arquivos.style.display = 'none';
        div_missa.style.display = 'none';
    }else{
        container.style.display = 'none';
        divp.style.display = 'flex';
        div_historia_sv.style.display = 'none';
        div_perfil.style.display = 'none';
        div_eventos.style.display = 'none';
        div_configuracoes.style.display = 'none';
        div_arquivos.style.display = 'none';
        div_missa.style.display = 'none';
    }
}

// aqui fica voltado para a página de arquivos
function bnt_arquivos(){
    var container = document.querySelector('.div_arquivos')
    var divp = document.querySelector('.div_hp')
    var div_historia_sv = document.querySelector('.historia_sv')
    var div_perfil = document.querySelector('.div_perfil')
    var div_eventos = document.querySelector('.div_eventos')
    var div_calendário = document.querySelector('.div_calendario')
    var div_configuracoes = document.querySelector('.div_configuracoes')
    var div_missa = document.querySelector('.div_missa')

    if(container.style.display === 'none'){
        container.style.display = 'flex';
        divp.style.display = 'none';
        div_historia_sv.style.display = 'none';
        div_perfil.style.display = 'none';
        div_eventos.style.display = 'none';
        div_calendário.style.display = 'none';
        div_configuracoes.style.display = 'none';
        div_missa.style.display = 'none';
    }else{
        container.style.display = 'none'
        divp.style.display = 'flex';
        div_historia_sv.style.display = 'none';
        div_perfil.style.display = 'none';
        div_eventos.style.display = 'none';
        div_calendário.style.display = 'none';
        div_configuracoes.style.display = 'none';
        div_missa.style.display = 'none';
    }
}

// aqui fica voltado para a página de configurações
function bnt_configuracoes(){
    var container = document.querySelector('.div_configuracoes');
    var divp = document.querySelector('.div_hp')
    var div_historia_sv = document.querySelector('.historia_sv')
    var div_perfil = document.querySelector('.div_perfil')
    var div_eventos = document.querySelector('.div_eventos')
    var div_calendário = document.querySelector('.div_calendario')
    var div_arquivos = document.querySelector('.div_arquivos')
    var div_missa = document.querySelector('.div_missa')

    if(container.style.display === 'none'){
        container.style.display = 'flex';
        divp.style.display = 'none';
        div_historia_sv.style.display = 'none';
        div_perfil.style.display = 'none';
        div_eventos.style.display = 'none';
        div_calendário.style.display = 'none';
        div_arquivos.style.display = 'none';
        div_missa.style.display = 'none';
    }else{
        container.style.display = 'none';
        divp.style.display = 'flex';
        div_historia_sv.style.display = 'none';
        div_perfil.style.display = 'none';
        div_eventos.style.display = 'none';
        div_calendário.style.display = 'none';
        div_arquivos.style.display = 'none';
        div_missa.style.display = 'none';
    }
}
function desconectar(){
    alert('Você saiu da sua conta!')
    location.href = 'treinando_login.html'
}
