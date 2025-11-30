function acessar(){
	var usuario = document.getElementById('loginEmail').value;
	var senha = document.getElementById('loginPassword').value;

	if(usuario == "ronymenezes" && senha == "251302"){
		alert('Acesso Aprovado');
		location.href = 'index.html';
	}else{
		alert("Acesso Negado");
	}
}