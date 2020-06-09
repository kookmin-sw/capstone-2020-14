import React from 'react';
import color from 'rcolor';
import createReactClass from 'create-react-class';

import { Doughnut } from 'react-chartjs-2';

import { OBJ_MAP } from '../constants';


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
    data: [0, 0, 0, 0, 0],
    backgroundColor: [
      '#396E4D',
      'yellow',
      'blue',
      'red',
      'black'
    ],
    hoverBackgroundColor: [
      '#396E4D',
      'yellow',
      'blue',
      'red',
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

        if (index + 1 > data.boundingbox.length) {
          index = 0;
          clearInterval(timer);
          return;
        }

        console.log(index);
        console.log(data.boundingbox[index].label)

        let elemOne, elemTwo, elemThree, elemFour, elemFive = 0;

        elemOne = data.boundingbox[index].label.filter((v) => {
          console.log('@@@@ filter 1: ', v);
          if ((v + 1) === 1) return true;
        });
        console.log('elemOne: ', elemOne);
        elemTwo = data.boundingbox[index].label.filter((v) => (v + 1) === 2);
        elemThree = data.boundingbox[index].label.filter((v) => (v + 1) === 3);
        elemFour = data.boundingbox[index].label.filter((v) => (v + 1) === 18);
        elemFive = data.boundingbox[index].label.filter((v) => {
          console.log('@@@@ filter: ', v);
          v = v + 1;
          if (v !== 1 &&
            v !== 2 &&
            v !== 3 &&
            v !== 18) return true;
        });
        
        let _state = getState();

        _state.datasets[0].data = [elemOne, elemTwo, elemThree, elemFour, elemFive];
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
