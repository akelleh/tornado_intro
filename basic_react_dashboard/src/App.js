import React from 'react';
import './App2.css';
import charts from 'fusioncharts/fusioncharts.charts'
import ReactFC from 'react-fusioncharts'
import FusionCharts from 'fusioncharts'
import 'fusioncharts/themes/fusioncharts.theme.carbon'
import httpGet from 'requests'

charts(FusionCharts)


var App = React.createClass( {
  render: function() {
    var myDataSource = {
        chart: {
            caption: "Harry's SuperMart",
            subCaption: "Top 5 stores in last month by revenue",
            numberPrefix: "$",
            theme: "carbon"
        },
        data: [{
            label: "Bakersfield Central",
            value: "880000"
        }, {
            label: "Garden Groove harbour",
            value: "730000"
        }, {
            label: "Los Angeles Topanga",
            value: "590000"
        }, {
            label: "Compton-Rancho Dom",
            value: "520000"
        }, {
            label: "Daly City Serramonte",
            value: "330000"
        }
        ]
    };

    var revenueChartConfigs = {

        type: "column2d",
        width: "80%",
        height: 400,
        dataFormat: "json",
        dataSource: myDataSource
    };

 var myDataSource2 = {
        chart: {
            caption: "Age profile of website visitors",
            subcaption: "Last Year",
            startingangle: "120",
            showlabels: "0",
            showlegend: "1",
            enablemultislicing: "0",
            slicingdistance: "15",
            showpercentvalues: "1",
            showpercentintooltip: "0",
            plottooltext: "Age group : $label Total visit : $datavalue",
            theme: "carbon"
        },
        data: [
            {
                label: "Teenage",
                value: "1250400"
            },
            {
                label: "Adult",
                value: "1463300"
            },
            {
                label: "Mid-age",
                value: "1050700"
            },
            {
                label: "Senior",
                value: "491000"
            }
        ]
    }
    var props_pie_chart_left = {
        id: "pie_chart",
        type: "pie3d",
        width: "80%",
        height: 400,
        dataFormat: "json",
        dataSource: myDataSource2
    };

    var request = require('request');
    request('http://localhost:7777/chart/pie', function (error, response, body) {
      console.log('error:', error);
      console.log('statusCode:', response && response.statusCode);
    });

    var props_pie_chart_right = httpGet('http://localhost:7777/chart/pie')

    var temp = {
        id: "doughnut2d",
        type: "doughnut2d",
        width: "80%",
        height: 400,
        dataFormat: "json",
        dataSource: myDataSource
    };

    return(
request.get('http://localhost:7777/chart/pie')
//    <div>
//      <div className="chart-row">
//          <ReactFC{...revenueChartConfigs}/>
//      </div>
//      <div className="chart-row">
//        <div className="inline-chart">
//          <ReactFC{...props_pie_chart_left}/>
//        </div>
//        <div className="inline-chart">
//          <ReactFC{...props_pie_chart_right}/>
//        </div>
//       </div>
//    </div>

    )
}
})

export default App;
