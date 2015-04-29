$(function () {
	
    // Initiate the chart
    $('#container').highcharts('Map', {

        title : {
            text : 'Worst Airports From Which To Fly To JFK'
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
				{name:'BOS', delay:17.649, trips:7029, lat:42.364348, lon:-71.005179},
				{name:'SFO', delay:13.785, trips:6817, lat:37.619002, lon:-122.374843},
				{name:'FLL', delay:18.424, trips:4610, lat:26.072583, lon:-80.152750},
				{name:'MIA', delay:30.588, trips:2681, lat:25.793250, lon:-80.290556},
				{name:'LAX', delay:9.562, trips:7908, lat:33.942536, lon:-118.408074},
				{name:'MCO', delay:14.081, trips:5286, lat:28.428889, lon:-81.316028},
				{name:'ORD', delay:18.982, trips:3489, lat:41.979595, lon:-87.904464},
				{name:'BUF', delay:16.458, trips:3559, lat:42.940525, lon:-78.732167},
				{name:'RDU', delay:13.300, trips:3828, lat:35.877639, lon:-78.787472},
				{name:'DCA', delay:14.559, trips:2871, lat:38.852083, lon:-77.037722},
				{name:'SJU', delay:11.745, trips:3504, lat:18.439417, lon:-66.001833},
				{name:'CLT', delay:23.044, trips:1772, lat:35.214011, lon:-80.943126},
				{name:'PIT', delay:18.166, trips:2134, lat:40.491466, lon:-80.232871},
				{name:'IAD', delay:17.581, trips:2204, lat:38.944532, lon:-77.455810},
				{name:'ATL', delay:19.094, trips:1896, lat:33.640444, lon:-84.426944},],
		}, {
            type: 'mapbubble',
            mapData: Highcharts.maps['countries/us/us-all'],
            name: 'Mean Delay Time',
            data: [
				{name:'BOS', z:176.490, lat:42.364348, lon:-71.005179},
				{name:'SFO', z:137.850, lat:37.619002, lon:-122.374843},
				{name:'FLL', z:184.240, lat:26.072583, lon:-80.152750},
				{name:'MIA', z:305.880, lat:25.793250, lon:-80.290556},
				{name:'LAX', z:95.620, lat:33.942536, lon:-118.408074},
				{name:'MCO', z:140.810, lat:28.428889, lon:-81.316028},
				{name:'ORD', z:189.820, lat:41.979595, lon:-87.904464},
				{name:'BUF', z:164.580, lat:42.940525, lon:-78.732167},
				{name:'RDU', z:133.000, lat:35.877639, lon:-78.787472},
				{name:'DCA', z:145.590, lat:38.852083, lon:-77.037722},
				{name:'SJU', z:117.450, lat:18.439417, lon:-66.001833},
				{name:'CLT', z:230.440, lat:35.214011, lon:-80.943126},
				{name:'PIT', z:181.660, lat:40.491466, lon:-80.232871},
				{name:'IAD', z:175.810, lat:38.944532, lon:-77.455810},
				{name:'ATL', z:190.940, lat:33.640444, lon:-84.426944},],
			color: '#800000',
            minSize: 2,
            maxSize: '15%',
        }]
    });
});
