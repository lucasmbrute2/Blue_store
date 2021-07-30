let loginCard = document.querySelector('#loginCard')
let descriptionCard = document.querySelector('#descriptionCard')
let img = document.querySelector('#sideImg')
let loginChanger = document.querySelector('.firstBtn')
let descriptionChanger = document.querySelector('.jsBtn')

loginChanger.addEventListener('click', () =>{
    loginCard.style.display = 'Block'
    descriptionCard.style.display = 'none'
    img.src = '../static/img/home/admin.svg'
})
descriptionChanger.addEventListener('click', () =>{
    loginCard.style.display = 'none'
    descriptionCard.style.display = 'Block'
    img.src = '../static/img/home/initial.svg'
})
