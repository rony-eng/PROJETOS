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