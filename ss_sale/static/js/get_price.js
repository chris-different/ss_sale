
$(document).ready(myWebsocketStart());

var a = 1;

function myWebsocketStart() {
	var ws = new WebSocket("ws://127.0.0.1:8080/websocket");

	ws.onopen = function() {
		ws.send("ping")

	};
	ws.onmessage = function(evt) {

		if (evt.data){
			var json = JSON.parse(evt.data);
			if (a == 1){
				$.each(json,function(i,n){
					$("tbody").append("<tr style=\"font-size:18px;\" id=\""+i+"\"><\/tr>");
					var h = "#"+i;
					$(h).append("<td class=\"f_id"+i+"\" id=\""+i+"\">"+n.f_id+"<\/td>");
					$(h).append("<td class=\"name"+i+"\" id=\""+i+"\">"+n.name+"<\/td>");	
					$(h).append("<td class=\"flow_market_price"+i+"\" id=\""+i+"\">"+n.flow_market_price+"<\/td>");	
					$(h).append("<td class=\"flow_amount"+i+"\" id=\""+i+"\">"+n.flow_amount+"<\/td>");	
					$(h).append("<td class=\"trade_amount"+i+"\" id=\""+i+"\">"+n.trade_amount+"<\/td>");
					$(h).append("<td class=\"price"+i+"\" id=\""+i+"\">"+n.price+"<\/td>");
					$(h).append("<td class=\"price_change"+i+"\" id=\""+i+"\">"+n.price_change+"<\/td>");
					var intprice_change = parseInt(n.price_change) ;
					if (intprice_change > 0){
						$(" .f_id"+i).css({"color":"red"});
						$(" .name"+i).css({"color":"red"});
						$(" .flow_market_price"+i).css({"color":"red"});
						$(" .flow_amount"+i).css({"color":"red"});
						$(" .trade_amount"+i).css({"color":"red"});
						$(" .price_change"+i).css({"color":"red"});
						$(" .price"+i).css({"color":"red"});
					}else {
						$(" .f_id"+i).css({"color":"green"});
						$(" .name"+i).css({"color":"green"});
						$(" .flow_market_price"+i).css({"color":"green"});
						$(" .flow_amount"+i).css({"color":"green"});
						$(" .trade_amount"+i).css({"color":"green"});
						$(" .price_change"+i).css({"color":"green"});
						$(" .price"+i).css({"color":"green"});
					}
				});
			}
			if (a != 1){
				$.each(json,function(i,n){
					var h = "#"+i;
					var intprice_change = parseInt(n.price_change) ;
					if (intprice_change > 0){
						$(" .f_id"+i).css({"color":"red"});
						$(" .name"+i).css({"color":"red"});
						$(" .flow_market_price"+i).css({"color":"red"});
						$(" .flow_amount"+i).css({"color":"red"});
						$(" .trade_amount"+i).css({"color":"red"});
						$(" .price"+i).css({"color":"red"});
						$(" .price_change"+i).css({"color":"red"});
					}else {
						$(" .f_id"+i).css({"color":"green"});
						$(" .name"+i).css({"color":"green"});
						$(" .flow_market_price"+i).css({"color":"green"});
						$(" .flow_amount"+i).css({"color":"green"});
						$(" .trade_amount"+i).css({"color":"green"});
						$(" .price"+i).css({"color":"green"});
						$(" .price_change"+i).css({"color":"green"});
					}
					$(" .price"+i).text(n.price);
					$(" .price_change"+i).text(n.price_change);
				});
			}

			setTimeout(function(){

				ws.send("ping");
				a++;
			},10000);
		}
	};
	ws.onclose = function() {

	};
}

function get_json(){
	$.get("/api/coin",function(data,status){
		
		$.each(data,function(i,n){


			$("tbody").append("<tr style=\"font-size:20px;\" id=\""+i+"\"><\/tr>");
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
}