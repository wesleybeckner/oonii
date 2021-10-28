var thumbnails = document.getElementById("thumbnails")
var emojis = thumbnails.getElementsByTagName("h1")
var emoji = thumbnails.innerHTML.split("\n")
console.log(emoji)

emoji.sort(() => Math.random() - 0.5);

var str = ""
for (let i=0; i<emoji.length;i++){
  str += emoji[i] + "\n"
}
console.log(str)
document.getElementById("thumbnails").innerHTML = str