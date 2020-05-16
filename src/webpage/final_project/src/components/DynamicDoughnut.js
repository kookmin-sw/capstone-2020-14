import React from 'react';
import color from 'rcolor';
import createReactClass from 'create-react-class';

import { Doughnut } from 'react-chartjs-2';

let timer = null;
let index = 0;

function getRandomInt(min, max) {
  return 100;
}

const options = {
  legend: {
    labels: {
      fontColor: 'white'
    }
  }
}

const getState = () => ({
  labels: [
    'Person',
    'Car',
    'Bicycle',
    'Dog',
    'Other Vehicle'
  ],
  datasets: [{
    data: [0],
    backgroundColor: [
      'red',
      'yellow',
      'green',
      'lime',
      'black'
    ],
    hoverBackgroundColor: [
      'red',
      'yellow',
      'green',
      'lime',
      'black'
    ]
  }]
});

export default createReactClass({
  displayName: 'DynamicDoughnutExample',

  getInitialState() {
    return getState();
  },

  componentWillMount() {
    // setInterval(() => {
    //   this.setState(getState());
    // }, 100);
  },
  componentDidUpdate(prevProps) {
    console.log('@@@@ update DynamicDoughnut');
    console.log(this.props);
    const { data, playerInfo } = this.props;
    
    let isToggle = prevProps.playerInfo.isPlay !== playerInfo.isPlay;
    if (isToggle === true && playerInfo.currentTime === 0) {
      index = 0;
    }

    // console.log(playerInfo.isPlay);
    if (isToggle === true && playerInfo.isPlay) {
      timer = setInterval(() => {

        if (index + 1 > data.bounding_box.length) {
          index = 0;
          clearInterval(timer);
          return;
        }

        console.log(index);
        console.log(data.bounding_box[index].label)

        let elemOne, elemTwo, elemThree = 0;

        elemOne = data.bounding_box[index].label.filter((v) => v === 1);
        elemTwo = data.bounding_box[index].label.filter((v) => v === 2);
        elemThree = data.bounding_box[index].label.filter((v) => v === 3);

        let _state = getState();

        _state.datasets[0].data = [elemOne, elemThree];
        console.log('@@@@ _staet: ', _state);

        this.setState(_state);
        index++;
      }, 100);
    } else if (isToggle === true && !playerInfo.isPlay) {
      console.log('clear timer');
      clearInterval(timer);
    }
  },
  componentWillUnmount() {
    clearInterval(timer);
  },
  render() {
    console.log('@@@@ render DynamicDoughnut');
    return (
      <div>
        <Doughnut 
        data={this.state} 
        options={options}
        />
      </div>
    );
  }
});
