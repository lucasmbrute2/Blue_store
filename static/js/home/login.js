let usuario = document.querySelector('#username')
let senha = document.querySelector('#password')
let botao = document.querySelector("#bttnEntrar")

/* Função para fazer o botão aparecer e desaparecer de acordo com o length. */
usuario.addEventListener('keyup',()=>{

    if (usuario.value.length && senha.value.length >3){
        botao.style.display = 'block'
    } else{
        botao.style.display = 'none'
    }
})

senha.addEventListener('keyup',()=>{

    if (usuario.value.length && senha.value.length >3){
        botao.style.display = 'block'
    } else{
        botao.style.display = 'none'
    }
})


botao.addEventListener('click',()=>{

    if(senha.value != 'admin'){
        alert('Senha inválida')
    }
})