window.onload=function(){
	alert(1);
	$.get("/api/server",function(data,status){
		for i in data:
			console.log(i);
	});
}