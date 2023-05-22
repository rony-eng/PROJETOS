function missas()
{
    var container = document.querySelector('.div_intencoes');

    if(container.style.display === 'block'){
        container.style.display = 'none';
    }else{
        container.style.display = 'block'
    }
}

function adicionar_intencoes()
{
    var input_missa = document.getElementById('input_missa').value;
    var input_data = document.getElementById('input_data').value;
    var input_intencoes = document.getElementById('input_intencoes').value;
    
    alert('A missa é: ' + input_missa,);
    alert('A data da missa é: ' + input_data);
    alert('Intenções e falecidos da missa são:\n' + '\n' + input_intencoes);

    if(input_missa && input_data && input_intencoes != '')
    {
        var input_missa = document.getElementById('input_missa').value='';
        var input_data = document.getElementById('input_data').value='';
        var input_intencoes = document.getElementById('input_intencoes').value='';

        alert('Intenções adicionadas!')

    }
    else
    {
        alert('Campos faltam serem preenchidos!')
    }
}   

function fechar_intencoes()
{
    alert('Botão funcionando!');
}

function sair()
{
    alert('Você saiu da sua conta')
    location.href = 'login.html';
}