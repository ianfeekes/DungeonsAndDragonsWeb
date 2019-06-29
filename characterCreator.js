//random should already work 

function sendTextToHTML(text, htmlID) {
    console.log("In send text to html"+text); 
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

function main()
{
    //Creates the textbox from javascript for easier manipulation and scaling 
    var textBox = document.createElement("P"); 
    textBox.setAttribute("id", "textBox");
    document.body.appendChild(textBox);

    console.log("Displaying message"); 
    sendTextToHTML("this is some dummy text sent from javascript", "textBox"); 
}




