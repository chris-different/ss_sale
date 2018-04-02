Highcharts.setOptions({
    global: {
        useUTC: false
    }
});
function activeLastPointToolip(chart) {
    var points = chart.series[0].points;
    chart.tooltip.refresh(points[points.length -1]);
}
$('#container').highcharts({
    chart: {
        type: 'spline',
        animation: Highcharts.svg, // don't animate in old IE
        marginRight: 10,
        events: {
            load: function () {
                // set up the updating of the chart each second
                var series = this.series[0],
                    chart = this;

                setInterval(function () {
                    
                    var json
                    var data_int
                    $.get("api/go_coin",function(data,status){
                        
                        data_int = parseFloat(data.USD)
                        var x = (new Date()).getTime(), // current time
                        y = data_int;
                        series.addPoint([x, y], true, true);
                        activeLastPointToolip(chart)
                    });
                    
                    
                }, 2500);
            }
        }
    },
    title: {
        text: 'BTC实时数据(平台不同，有点差，仅供参考)'
    },
    xAxis: {
        type: 'datetime',
        tickPixelInterval: 150
    },
    yAxis: {
        title: {
            text: '值'
        },
        plotLines: [{
            value: 0,
            width: 1,
            color: '#808080'
        }]
    },
    tooltip: {
        formatter: function () {
            return '<b>' + this.series.name + '</b><br/>' +
                Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
                Highcharts.numberFormat(this.y, 2);
        }
    },
    legend: {
        enabled: false
    },
    exporting: {
        enabled: false
    },
    series: [{
        name: '实时数据',
        data: (function () {
            // generate an array of random data
            var data = [],
                time = (new Date()).getTime(),
                i;
            var data_intfirst
                    $.get("api/go_coin",function(data,status){
                        
                        data_intfirst = parseFloat(data.USD)
                        var x = (new Date()).getTime(), // current time
                        y = data_intfirst;
                        series.addPoint([x, y], true, true);
                        activeLastPointToolip(chart)
                    });
            for (i = -15; i <= 0; i += 1) {
                data.push({

                    
                    
                    x: time + i * 1000,
                    y: data_intfirst
                });
            }
            return data;
        }())
    }]
}, function(c) {
    activeLastPointToolip(c)
});







function myWebsocketStart() {
    var ws = new WebSocket("ws://127.0.0.1:8080/current_data/websocket");

    ws.onopen = function() {
        ws.send("ping")

    };
    ws.onmessage = function(evt) {

        if (evt.data){
            var json = JSON.parse(evt.data);
            if (a != 1){
                $.each(json,function(i,n){
                    var h = "#"+i;
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
