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
function adc_missa_intencoes()
{
    var input_missa = document.getElementById('inp1_div_missa').value;
    var input_data = document.getElementById('inp2_div_missa').value;
    var input_hora = document.getElementById('inp3_div_missa').value;
    var input_intencoes = document.getElementById('inp4_div_missa').value;


    if(input_missa && input_data && input_hora && input_intencoes != '')
    {
        alert('A missa é: ' + input_missa);
        alert('A data da missa é: ' + input_data);
        alert('O horário é: ' + input_hora);
        alert('Intenções e falecidos da missa são:\n' + '\n' + input_intencoes);

        var input_missa = document.getElementById('inp1_div_missa').value='';
        var input_data = document.getElementById('inp2_div_missa').value='';
        var input_hora = document.getElementById('inp3_div_missa').value='';
        var input_intencoes = document.getElementById('inp4_div_missa').value='';

        alert('Intenções adicionadas!')

    }
    else
    {
        alert('Campos faltam serem preenchidos!')
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
    }else{
        container.style.display = 'none';
    }
}
function focado(){
    document.getElementsByClassName('dropDown')[0].style.display="block"
}
function desfoque(){
    document.getElementsByClassName('dropDown')[0].style.display="none"
}
function category(c){
    var item = document.getElementById('item-'+c).innerHTML
    document.getElementsByClassName('modo_config')[0].value = item
}
function aplicar_modo(){
    const bnt_modo = document.querySelector('.modo_noturno_claro')    
}

function desconectar(){
    alert('Você saiu da sua conta!')
    location.href = 'treinando_login.html'
}
