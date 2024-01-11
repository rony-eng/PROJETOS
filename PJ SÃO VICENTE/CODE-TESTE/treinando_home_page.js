// aqui fica voltado para a página da história de são vicente
function bnt_historia_sv(){
    let container = document.querySelector('.historia_sv');
    let divp = document.querySelector('.div_hp')
    let div_perfil = document.querySelector('.div_perfil')
    let div_missa = document.querySelector('.div_missa')
    let div_eventos = document.querySelector('.div_eventos')
    let div_calendário = document.querySelector('.div_calendario')
    let div_arquivos = document.querySelector('.div_arquivos')
    let div_configurações = document.querySelector('.div_configuracoes')

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
    let container = document.querySelector('.historia_sv');
    let divp = document.querySelector('.div_hp')

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
    let container = document.querySelector('.div_perfil');

    if(container.style.display === 'none'){
        container.style.display = 'flex';
    }else{
        container.style.display = 'none';
    }
}

// aqui fica voltado para a página de missa e intenções
function bnt_missa(){
    let container = document.querySelector('.div_missa')
    let divp = document.querySelector('.div_hp')
    let div_historia_sv = document.querySelector('.historia_sv')
    let div_perfil = document.querySelector('.div_perfil')
    let div_eventos = document.querySelector('.div_eventos')
    let div_calendário = document.querySelector('.div_calendario')
    let div_arquivos = document.querySelector('.div_arquivos')
    let div_configurações = document.querySelector('.div_configuracoes')

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
    var recebe = document.querySelector('.receber_inf_missa')

    recebe.value = 'Missa:' + '\n' + input_missa + '\n' + '\n'  + 'Data:' + '\n' + input_data + '\n' + '\n' + 'Hora' + '\n' + input_hora + '\n' + '\n' + 'Intenções:' + '\n' + input_intencoes

    if(input_missa && input_data && input_hora && input_intencoes != '')
    {
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
function ver_missa_intencoes(){
    var container = document.querySelector('.div_ver_inf_missa');

    if(container.style.display === 'none'){
        container.style.display = 'flex';
    }else{
        container.style.display = 'none';
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

    if(container.style.display === 'none'){
        container.style.display = 'flex';
    }else{
        container.style.display = 'none';
    }
}
function category(c){
    var item = document.getElementById('item-'+c).innerHTML
    document.getElementsByClassName('modo_config')[0].value = item
}
function aplicar_modo(){
    var container = document.querySelector('html')
    var div_config = document.querySelector('.div_configuracoes');

    if(container.className === 'light_modo'){
        container.className = 'dark_modo'
        div_config.style.display = 'none'
        alert('Modo noturno ativado!')
    }else{
        container.className = 'light_modo'
        div_config.style.display = 'none'
        alert('Modo claro ativado!')
    }
}
function desconectar(){
    alert('Você saiu da sua conta!')
    location.href = 'treinando_login.html'
}
