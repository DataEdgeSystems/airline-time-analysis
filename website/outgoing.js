$(function () {
	
    // Initiate the chart
    $('#container').highcharts('Map', {

        title : {
            text : 'Worst Airports To Fly To From JFK'
        },

        subtitle : {
            text : 'Average Delay (minutes) per flight'
        },

        mapNavigation: {
            enabled: true,
            buttonOptions: {
                verticalAlign: 'bottom'
            }
        },
        colorAxis: {
            min: 0
        },
		tooltip: {
		    headerFormat: '',
		    pointFormat: '<b>{point.name}</b><br>Avg Delay: {point.delay} mins<br>Total Trips: {point.trips}'
		},
        series : [
		{
            mapData: Highcharts.maps['countries/us/us-all'],
            name: 'Basemap',
		}, {
            name: 'Separators',
            type: 'mapline',
            data: Highcharts.geojson(Highcharts.maps['countries/us/us-all'], 'mapline'),
            color: 'silver',
            showInLegend: false,
            enableMouseTracking: false
        }, {
            type: 'mappoint',
            name: 'Cities',
            color: Highcharts.getOptions().colors[1],
            data: [
				{name:'BOS', delay:15.411, trips:7187, lat:42.364348, lon:-71.005179},
				{name:'LAX', delay:13.412, trips:7972, lat:33.942536, lon:-118.408074},
				{name:'SFO', delay:12.814, trips:6476, lat:37.619002, lon:-122.374843},
				{name:'ORD', delay:23.739, trips:3484, lat:41.979595, lon:-87.904464},
				{name:'MCO', delay:12.806, trips:5302, lat:28.428889, lon:-81.316028},
				{name:'FLL', delay:13.631, trips:4633, lat:26.072583, lon:-80.152750},
				{name:'MIA', delay:21.807, trips:2689, lat:25.793250, lon:-80.290556},
				{name:'RDU', delay:13.150, trips:4000, lat:35.877639, lon:-78.787472},
				{name:'LAS', delay:11.763, trips:4418, lat:36.080361, lon:-115.152333},
				{name:'TPA', delay:13.692, trips:3322, lat:27.975472, lon:-82.533250},
				{name:'SJU', delay:12.848, trips:3518, lat:18.439417, lon:-66.001833},
				{name:'ATL', delay:16.156, trips:2249, lat:33.640444, lon:-84.426944},
				{name:'DCA', delay:12.768, trips:2783, lat:38.852083, lon:-77.037722},
				{name:'BUF', delay:9.695, trips:3572, lat:42.940525, lon:-78.732167},
				{name:'PIT', delay:14.817, trips:2129, lat:40.491466, lon:-80.232871}],
		}, {
            type: 'mapbubble',
            mapData: Highcharts.maps['countries/us/us-all'],
            name: 'Mean Delay Time',
            data: [
				{name:'BOS', z:154.110, lat:42.364348, lon:-71.005179},
				{name:'LAX', z:134.120, lat:33.942536, lon:-118.408074},
				{name:'SFO', z:128.140, lat:37.619002, lon:-122.374843},
				{name:'ORD', z:237.390, lat:41.979595, lon:-87.904464},
				{name:'MCO', z:128.060, lat:28.428889, lon:-81.316028},
				{name:'FLL', z:136.310, lat:26.072583, lon:-80.152750},
				{name:'MIA', z:218.070, lat:25.793250, lon:-80.290556},
				{name:'RDU', z:131.500, lat:35.877639, lon:-78.787472},
				{name:'LAS', z:117.630, lat:36.080361, lon:-115.152333},
				{name:'TPA', z:136.920, lat:27.975472, lon:-82.533250},
				{name:'SJU', z:128.480, lat:18.439417, lon:-66.001833},
				{name:'ATL', z:161.560, lat:33.640444, lon:-84.426944},
				{name:'DCA', z:127.680, lat:38.852083, lon:-77.037722},
				{name:'BUF', z:96.950, lat:42.940525, lon:-78.732167},
				{name:'PIT', z:148.170, lat:40.491466, lon:-80.232871},],
			color: '#7cb5ec',
            minSize: 2,
            maxSize: '15%',
        }]
    });
});
