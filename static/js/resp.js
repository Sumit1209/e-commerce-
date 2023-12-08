burger= document.querySelector('.burger')
navbar= document.querySelector('.navbar')
navList= document.querySelector('.nav-list')
rightNav= document.querySelector('.rightNav')
rightNav1= document.querySelector('.rightNav1')


burger.addEventListener('click',()=>{
    rightNav.classList.toggle('v-classresp');
    rightNav1.classList.toggle('v-classresp1');

    navList.classList.toggle('v-classresp');
    navbar.classList.toggle('h-nav-resp');

})


// const allHoverImages = document.querySelectorAll('.hover-container div img');
// const imgContainer = document.querySelector('.img-container');

// window.addEventListener('DOMContentLoaded', () => {
//     allHoverImages[0].parentElement.classList.add('active');
// });

// allHoverImages.forEach((image) => {
//     image.addEventListener('mouseover', () =>{
//         imgContainer.querySelector('img').src = image.src;
//         resetActiveImg();
//         image.parentElement.classList.add('active');
//     });
// });

// function resetActiveImg(){
//     allHoverImages.forEach((img) => {
//         img.parentElement.classList.remove('active');
//     });
// }

// //++++++++++++++++++++++



      


// if (localStorage.getItem('cart') == null){
//     var cart = {};
// }
// else
// {
//     cart = JSON.parse(localStorage.getItem('cart'));
// }
// $ ('.cart').click(function(){
//     console.log('clicked');
//     var idstr=this.id.toString();
//     console.log(idstr);
    
// });


    