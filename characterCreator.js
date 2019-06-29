//random should already work 

function sendTextToHTML(text, htmlID) {
    console.log("In function"); 
    document.getElementById(htmlID).innerHTML = text; 
}

class Character{
    constructor(name, gender, race, profession, stats){
        this.name = name; 
        this.race=race; 
        this.profession=profession; 
        this.stats=stats; 
        this.gender=gender; 
    }


    //TO DO: write a toFile function for our character 



}

var races =  ["human", "halfling", "gnome", "half-orc", "dwarf", "half-Elf", "elf"];
var textBox = document.getElementById("textBox"); 

function main()
{
    console.log("Displaying message"); 
    sendTextToHTML("this is some dummy text sent from javascript", "textBox"); 
}




