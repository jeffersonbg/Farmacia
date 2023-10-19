

function logar(){

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

   
    if (email == "arthur@hotmail.com" && password == 12345) {
        
        window.location.href = "farmacia.html" ;

    } else {
        alert("Credenciais inválidas. Tente novamente.");
    }
}

function cadastrar(){
    
}