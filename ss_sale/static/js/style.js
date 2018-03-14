
var i=0;
var a=0;
var all=0;
var strlf= "CC-data";
var strrg="带给您极致的数据体验"


function write(){
	var id = document.getElementById("lf");
	id.innerText = strlf.substring(0, i++);	
	if(i == strlf.length){
		setInterval(write2,100);
	}	
}

function write2(){
	var id = document.getElementById("rg");
	id.innerText = strrg.substring(0, a++);	
	if(a == strrg.length){
		return;
	}
}




function write3() {
	
	$("#zero").css("display","");
}
function write4() {
	$("#second").css("display","");
}

function write5() {
	$("#third").css("display","");
}

function write6() {
	$("#forth").css("display","");
}

function write7() {
	$("#fifth").css("display","");
}
function write8() {
	$("#zerorg").css("display","");
}

window.onload=function(){
	setInterval(write,100);
	setInterval(write3,300);
	setInterval(write4,500);
	setInterval(write5,700);
	setInterval(write6,800);
	setInterval(write7,900);
	setInterval(write8,1000);
}

