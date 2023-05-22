
function acessar(){
    var usuario = document.getElementById('input_usuario').value;
    var senha = document.getElementById('input_senha').value;

    if(usuario == "sv_605" || usuario == "ronyy.oo026@gmail.com" && senha == "saovicente" || senha == "ronymenezes"){
        alert('Acesso Aprovado');
        location.href = 'pagina_inicial.html';
    }else{
        alert("Acesso Negado")
    }
}

function cadastrar(){
    var container = document.querySelector('.div_cadastrar');

    if(container.style.display === 'block'){
        container.style.display = 'none';
    }else{
        container.style.display = 'block'
    }
}

function botão_p_login(){
    var container = document.querySelector('.div_cadastrar');

    if(container.style.display === 'block'){
        container.style.display = 'none';
    }else{
        container.style.display = 'block'
    }
}