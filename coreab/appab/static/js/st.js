open = document.getElementById("modal")
let span = document.getElementsByClassName("close")[0]

open.addEventListener("click", function(){
    document.getElementById("modalwd").style.display='block'
})

span.addEventListener("click", function(){
    document.getElementById("modalwd").style.display='none'
})

// vk
vk = document.getElementById('vk')
vk.addEventListener('click',function(){
    location.href = 'https://vk.com'
})
// inst
inst = document.getElementById('inst')
inst.addEventListener('click',function(){
    location.href = 'https://en.wikipedia.org/wiki/Instagram'
})
// telegram
telegram = document.getElementById('telegram')
telegram.addEventListener('click',function(){
    location.href = 'https://telegram.org/?ysclid=lbtn9ovf1751511071'
})

glavcolor.onmouseover = function() {
    glavcolor.style.color= "red";
}