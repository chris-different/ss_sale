window.onload=function(){
	

	$.get("/api/server",function(data,status){
		
		$.each(data,function(i,n){




			

			$("div.container-fluid").append("<div class=\"col-md-4 col-sm-4 serverlist\" id=\""+i+"\"><\/div>");
			var h = "#"+i;
			$(h).append("<div class=\"serverlist-in\" id=\""+i+"\"><\/div>");	
			$("div#"+i+" .serverlist-in").append("<ul id=\""+i+"\" class=\"ul-list\"><\/ul>");
			$("#"+i+" ul").append("<li class=\"server\">Ip-address:"+n.ip_address+"<\/li>");
			$("#"+i+" ul").append("<li class=\"server\">port:"+n.port+"<\/li>");
			$("#"+i+" ul").append("<li class=\"server\">City-address:"+n.city_address+"<\/li>");
			$("#"+i+" ul").append("<li class=\"server\">Timeout:"+n.timeout+"<\/li>");	
				
				
				
		});
	});
}