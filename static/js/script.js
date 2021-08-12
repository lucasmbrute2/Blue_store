
const titulo = document.querySelector('h1');



function typeWrite(elemento){
    const textoArray = elemento.innerHTML.split('');
    elemento.innerHTML = ''
    textoArray.forEach((letra,i)=>{
        console.log(letra);
        setTimeout(() => elemento.innerHTML += letra, 200*i)
    });
    }

typeWrite(titulo)