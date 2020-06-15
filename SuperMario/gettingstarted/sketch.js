var serial;
var portName = '/dev/tty.usbserial-AB0JN9HX';
var inData;
var outByte = 0;

function setup(){
	//put setup code here
	createCanvas(400,300);
	serial = new p5.SerialPort(); //new instance of serial port lib
	serial.on('list', printList);
	serial.list();
	serial.on('connected', serverConnected);
	serial.on('open', portOpen);
	serial.on('data', serialEvent);
	serial.on('error', serialError);
	serial.on('close', portClose);
	
	serial.open(portName); //open a serial port

}

function printList(portList){
	console.log(portList);
	console.log(portList.find(correctPort));

}

function correctPort(val){
	if (val.includes('usbserial')){
		return(val);
	}
}

function serverConnected() {
	console.log('connected to server.')
}

function portOpen() {
	console.log('serialport opened');
}

function serialEvent() {
	inData = Number(serial.read());
	//inData = serial.readStringUntil('\r\n');
	console.log(String.fromCharCode(int(inData)));
}

function serialError(err) {
	console.log('Error: '+ err);
}

function portClose() {
	console.log('serial port closed');
}


function keyPressed(){
	serial.write('3');
}

function draw() {
	background(0);
	fill(255);
	text('sensor val: '+ inData,30,30);
	
}
