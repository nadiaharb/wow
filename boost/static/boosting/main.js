const closeCartBtn=document.querySelector('.close-cart')
const cartDOM=document.querySelector('.cart')
const cartOverlay=document.querySelector('.cart-overlay')

const loginBtn=document.querySelector('.login')
var updateBtns=document.querySelectorAll('.update-cart')





for(var i=0; i<updateBtns.length; i++){
   updateBtns[i].addEventListener('click', function(){
     var service=this.dataset.service
     var action=this.dataset.action
     console.log(service, action, user)



     if(user==='AnonymousUser'){
     addCookieItem(service,action)


     }else{
     updateOrder(service, action)
     }

   })

}

function addCookieItem(service, action){
console.log(service, action)
if(action=='add'){
if(cart[service]==undefined){

cart[service]={'quantity':1}
}else{
cart[service]['quantity']+=1
}

}
if(action=='remove'){
cart[service]['quantity']-=1
   if(cart[service]['quantity']<=0){
   console.log('Remove item')
   delete cart[service]

   }

}
console.log('Added here')
document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"


location.reload()
}


function updateOrder(service, action){
   var url='/update_item/'

   fetch(url,{
     method:'POST',
     headers:{
       'Content-Type':'application/json'
     },
     body:JSON.stringify({
     'service': service,
     'action': action
     })
   })
   .then((response)=>{
       return response.json()

   })
  .then((data)=>{
       console.log(data, 'no reload')
       location.reload()
   })

}


var faqs=document.querySelectorAll('.faq')

faqs.forEach(faq => {
faq.addEventListener('click', function(){
faq.classList.toggle('active')
})

})

function showCart(){

cartOverlay.classList.add('transparentBcg')
cartDOM.classList.add('showCart')
}
function hideCart(){
cartOverlay.classList.remove('transparentBcg')
cartDOM.classList.remove('showCart')
}

function get_latest_API(){
fetch(`/ex`)
    .then(response => response.json())
    .then(data => {
    console.log( data)
    })
}



