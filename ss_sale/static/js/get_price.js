
$(document).ready(function(){
	$.get("/api/coin",function(data,status){
		
		$.each(data,function(i,n){


			$("tbody").append("<tr id=\""+i+"\"><\/tr>");
			var h = "#"+i;
			$(h).append("<td id=\""+i+"\">"+n.f_id+"<\/td>");
			$(h).append("<td id=\""+i+"\">"+n.name+"<\/td>");	
			$(h).append("<td id=\""+i+"\">"+n.flow_market_price+"<\/td>");	
			$(h).append("<td id=\""+i+"\">"+n.flow_amount+"<\/td>");	
			$(h).append("<td id=\""+i+"\">"+n.trade_amount+"<\/td>");
			$(h).append("<td id=\""+i+"\">"+n.price+"<\/td>");
			$(h).append("<td id=\""+i+"\">"+n.price_change+"<\/td>");			
				
				
		});


	});



			

			
			
				
				
				
		
});
