function acessar(){
	var usuario = document.getElementById('usuario').value;
	var senha = document.getElementById('senha').value;

	if(usuario == "ronymenezes" && senha == "251302"){
		alert('Acesso Aprovado');
		location.href = 'mentalista02.html';
	}else{
		alert("Acesso Negado");
	}
}
