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

var raceDescriptions = "Humans have no ability adjustments but get an extra feat (perk) \n Dwarfs are extra hardy and tend to be a little uggo/unlikeable \nElves have great hands (tossin) but are not super healthy \nGnomes get that extra constitution but no strength. Great for not being a fighter while having strong fighting stats \nHalf elves have a couple skills boosts, and are generally liked by both humans and elves. Or hated by both. \nHalf orcs (you can be a full orc and I won't tell anyone) get extra strength and less intelligence \n Halflings get less dexterity and extra strength\n";

var prompts = ["Enter the name of your new adventurer: ",
"Now to select your gender (Non-spectrum):",
"Now to select your race: ",
];

function main()
{
    //Creates the textbox from javascript for easier manipulation and scaling 
    var textBox = document.createElement("P"); 
    textBox.setAttribute("id", "textBox");
    document.body.appendChild(textBox);
    
    //Creates the form 
    var inputForm = document.createElement("FORM"); 
    inputForm.setAttribute("id", "inputForm"); 
    document.body.appendChild(inputForm); 

    var inputField = document.createElement("INPUT");
    inputField.setAttribute("type", "text");
    inputField.setAttribute("value", "");
    document.getElementById("inputForm").appendChild(inputField);

    console.log("Displaying message"); 
    sendTextToHTML("this is some dummy text sent from javascript", "textBox"); 

    for(let i=0;i<prompts.length;++i)
    {
        sendTextToHTML(prompts[i], "textBox"); 
    }
}




