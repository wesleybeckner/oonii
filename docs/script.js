// function myFunction() {
//   setTimeout(function(){
//     oonii = document.getElementById("oonii");
//     oonii.innerHTML = "admin@oonii.io"
//     }, 3000);
// }
// myFunction();
document.querySelector('.a').addEventListener('click', function(){
console.log('h1 has been clicked');
window.location = "https://sites.google.com/view/oonii/calendar"
});

// Wrap every letter in a span
var textWrapper = document.querySelector('.a');
textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

anime.timeline({loop: false})
  .add({
    targets: '.a .letter',
    opacity: [0,1],
    easing: "easeInOutQuad",
    duration: 2250,
    delay: (el, i) => 150 * (i+1)
  })

// function newtext()
// {

// document.getElementById('oonii').innerHTML = "admin@oonii.io";
// }

// setTimeout(newtext,3000);
