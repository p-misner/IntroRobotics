var user = {};

function setup() {	
	createCanvas(800,400);
	background('rgba(135,206,250,0.25)');
	setupStates();

}


function draw() {

}

class Mario {
	constructor(x, y){
		setupStates();
		setPosition(x,y);
	}
}

class State {
	constructor(name, graphic){
		this.states = {};
		this.name = name;
		this.link = graphic;
		this.curr_state;
		this.curr_graphic;
	}
}

function addState(newstate){
	console.log(newstate.name);
}
function setupStates() {
	addState(new State ("idle", "graphics/mario/small/Standing-mario.gif"));
	addState(new State("running", "graphics/mario/small/Running-mario.gif"));
    addState(new State("jumping", "graphics/mario/small/Jumping-mario.gif"));
    addState(new State("dead", "graphics/mario/small/Dead-mario.gif"));
    setCurrentState("idle");
}
function setCurrentState(name){
	console.log("name");
}