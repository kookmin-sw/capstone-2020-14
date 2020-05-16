import React, { Component } from 'react';
import CanvasJSReact from './canvasjs.react';
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

// var dps = [{ x: 1, y: 10 }, { x: 2, y: 13 }, { x: 3, y: 18 }, { x: 4, y: 20 }, { x: 5, y: 17 }, { x: 6, y: 10 }, { x: 7, y: 13 }, { x: 8, y: 18 }, { x: 9, y: 20 }, { x: 10, y: 17 }];   //dataPoints.
var dps = [];   //dataPoints.
var xVal = dps.length + 1;
var yVal = 0;
var updateInterval = 100;

let timer = null;

let _data = null;

class DynamicLineChart extends Component {
  constructor(props) {
    super(props);
    this.updateChart = this.updateChart.bind(this);
  }
  componentDidMount() {
    const { data } = this.props;
  }

  componentDidUpdate(prevProps) {
    console.log('@@@@ update DynamicLineChart');
    console.log(this.props);
    const { data, playerInfo } = this.props;

    /**
     * 싱크 조정 필요할듯
     */
    if (playerInfo.isPlay) {
      timer = setInterval(() => this.updateChart(data, playerInfo), updateInterval);
    } else {
      xVal = playerInfo.currentTime * 10;
      yVal = playerInfo.currentTime * 10;
      console.log('@@@@ yVal(stop): ', yVal);
      clearInterval(timer);
    }
  }

  componentWillUnmount() {
    console.log('@@@@ unmount DynamicLineChart');
    xVal = 1;
    yVal = 0;
    dps = [];
    this.chart.render();
    this.chart.destroy();
    this.chart = null;
  }

  updateChart(data, playerInfo) {
    // console.log(data);

    // yVal = yVal +  Math.round(5 + Math.random() *(-5-5));
    if (yVal + 1 > data.bounding_box.length) {
      if (this.chart) this.chart.render();
      clearInterval(timer);
      return;
    }

    let yData = data.bounding_box[yVal].label.length;
    // console.log(data.bounding_box.length);
    console.log('@@@@ 1: ', yVal);
    console.log('@@@@ 1: ', playerInfo);

    dps.push({ x: xVal, y: yData });
    xVal++;
    yVal++;
    if (dps.length > 10) {
      dps.shift();
    }
    if (this.chart) this.chart.render();
  }
  render() {
    console.log('@@@@ yVal: ', yVal);

    const options = {
      title: {
        text: '프레임 당 객체 수 변화추이',
        //Uncomment properties below to see how they behave
        //fontColor: "red",
        //fontSize: 30
      },
      axisY: {
        minimum: 0,
        interval: 1,
        title: '객체 개수'
      },
      axisX: {
        title: '프레임 수'
      },
      height: 300,
      data: [{
        type: "line",
        dataPoints: dps
      }]
    }

    return (
      <div id={'dynamic-line-chart'}>
        <CanvasJSChart options={options}
          onRef={ref => this.chart = ref}
        />
        {/*You can get reference to the chart instance as shown above using onRef. This allows you to access all chart properties and methods*/}
      </div>
    );
  }
}

export default DynamicLineChart;