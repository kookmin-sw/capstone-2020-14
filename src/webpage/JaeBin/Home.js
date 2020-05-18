import React from 'react';
import Modal from 'react-modal';
import './Home.css';

import { Doughnut, Bar, Line } from 'react-chartjs-2';
import CrazyLine from '../components/CrazyLine';
import DynamicDoughnut from '../components/DynamicDoughnut';


const data = {
  labels: [
    'Red',
    'Green',
    'Yellow'
  ],
  datasets: [{
    data: [300, 50, 100],
    backgroundColor: [
      '#FF6384',
      '#36A2EB',
      '#FFCE56'
    ],
    hoverBackgroundColor: [
      '#FF6384',
      '#36A2EB',
      '#FFCE56'
    ]
  }]
};

const data2 = {
  labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
  datasets: [
    {
      label: 'My First dataset',
      fill: false,
      lineTension: 0.1,
      backgroundColor: 'rgba(75,192,192,0.4)',
      borderColor: 'rgba(75,192,192,1)',
      borderCapStyle: 'butt',
      borderDash: [],
      borderDashOffset: 0.0,
      borderJoinStyle: 'miter',
      pointBorderColor: 'rgba(75,192,192,1)',
      pointBackgroundColor: '#fff',
      pointBorderWidth: 1,
      pointHoverRadius: 5,
      pointHoverBackgroundColor: 'rgba(75,192,192,1)',
      pointHoverBorderColor: 'rgba(220,220,220,1)',
      pointHoverBorderWidth: 2,
      pointRadius: 1,
      pointHitRadius: 10,
      data: [65, 59, 80, 81, 56, 55, 40]
    }
  ]
};

const customStyles = {
  content: {
    top: '50%',
    left: '50%',
    right: '40%',
    bottom: '-30%',
    marginRight: '-50%',
    transform: 'translate(-50%, -50%)'
  }
};

class Home extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      itemCount: 0,
      isRawVideo: false,
      isObjVideo: false,
      showModal: false,
      player1CurrentTime: 0,
      player2CurrentTime: 0
    }

    this.addDevice = this._addDevice.bind(this);
    this.viewRawVideo = this._viewRawVideo.bind(this);
    this.viewObjVideo = this._viewObjVideo.bind(this);
    this.handleOpenModal = this._handleOpenModal.bind(this);
    this.handleCloseModal = this._handleCloseModal.bind(this);
  }

  componentDidMount() {
    console.log('mount');
  }

  componentDidUpdate() {
    console.log('@@@@ palyer2')
    console.log(this.player2);
    if (this.player2) {
      this.player2.currentTime = this.state.player1CurrentTime;
    }
  }

  render() {
    console.log('render');
    console.log(this.state.itemCount);
    return (
      <div className="main">
        <div className="sidebar">
          <div className="sidebar-header">
            디바이스 목록
          </div>
          <div className="sidebar-main">
            {
              this.state.itemCount > 0 ?
                (() => {
                  return (
                    [...Array(this.state.itemCount)].map((item, index) => {
                      return (
                        <div className="sidebar-main-item" onClick={() => this.viewRawVideo()}>
                          <p>Seek Shot Pro</p>
                          <img src="assets/images/camera.jpeg" />
                        </div>
                      )
                    })
                  )
                })()
                :
                <div className="sidebar-main-empty">
                  없음
              </div>
            }
          </div>
          <div className="sidebar-add-btn-div">
            <div className="sidebar-add-btn" onClick={() => this.addDevice()}>
              + 디바이스 추가
            </div>
          </div>
        </div>
        <div className="contents">
          <div className="parent">
            <div className="child">
              <div className="contents-wrapper">
                {
                  // <CrazyLine />
                }

                {
                  this.state.itemCount > 0 ?
                    ''
                    :
                    <h2>선택된 디바이스가 없습니다</h2>

                }
                {
                  this.state.isRawVideo === true ?
                    (
                      <>
                        <div className="contents-item">
                          <video ref={ref => this.player1 = ref} width="100%" controls>
                            <source src="./assets/videos/output1.mp4" type="video/mp4" />
                          </video>
                        </div>
                        <div className="contents-sidebar">
                          <div style={{ width: '100%' }}>
                            <img style={{ cursor: 'pointer', width: '80%' }} src="/assets/images/rec.png" />
                          </div>
                          <div style={{ width: '100%;' }} onClick={() => this.viewObjVideo()}>
                            <img style={{ cursor: 'pointer' }} width="80%" src="/assets/images/off.png" />
                          </div>
                        </div>
                      </>
                    )
                    :
                    null
                }
                {
                  this.state.isObjVideo === true ?
                    (
                      <>
                        <div className="contents-item">
                          <video ref={ref => this.player2 = ref} width="100%" controls>
                            <source src="./assets/videos/output2.mp4" type="video/mp4" />
                          </video>
                        </div>
                        <div className="contents-sidebar">
                          <div style={{ width: '100%' }}>
                            <img style={{ cursor: 'pointer' }} width="80%" src="/assets/images/rec.png" />
                          </div>
                          <div style={{ width: '100%' }} onClick={() => this.viewRawVideo()}>
                            <img style={{ cursor: 'pointer' }} width="80%" src="/assets/images/on.png" />
                          </div>
                          <div style={{ width: '100%' }} onClick={() => this.handleOpenModal()}>
                            <img style={{ cursor: 'pointer' }} width="80%" src="/assets/images/stat.png" />
                          </div>
                        </div>
                      </>
                    )
                    :
                    null
                }
              </div>
            </div>
          </div>

        </div>
        <Modal
          isOpen={this.state.showModal}
          contentLabel="Minimal Modal Example"
          style={customStyles}
          className="Modal"
          overlayClassName="Overlay"
        >
          <div 
          onClick={() => this.handleCloseModal()}
          style={{ textAlign: 'right', cursor: 'pointer' }}
          >
            <img src="./assets/images/btn-thum-popup-close.svg" />
          </div>
          <div className="modal-div">
            <div>
              <video width="100%" controls>
                <source src="./assets/videos/output2.mp4" type="video/mp4" />
              </video>
            </div>
            <div>
              <div style={{ paddingBottom: '50px' }}>
                <CrazyLine />
              </div>
              <div>
                <DynamicDoughnut />
              </div>

            </div>

          </div>
        </Modal>
      </div>
    )
  }

  _addDevice() {
    this.setState({
      itemCount: this.state.itemCount + 1
    });
  }

  _viewRawVideo() {
    this.setState({
      isRawVideo: true,
      isObjVideo: false
    });

    console.log(document.body.clientWidth);
    if (document.body.clientWidth <= 600) {
      var node = document.getElementsByClassName('sidebar');
      console.log(node[0]);
      console.log(node[0].style.display);

      node[0].style.display = 'none';
      node[0].style.width = "0s";
    }

  }

  _viewObjVideo() {
    this.setState({
      isRawVideo: false,
      isObjVideo: true,
      player1CurrentTime: this.player1.currentTime
    });

    // console.log(this.player1.currentTime);
    // this.player2.currentTime = this.player1.currentTime;

  }

  _handleOpenModal() {
    this.setState({
      showModal: true
    });
  }

  _handleCloseModal() {
    this.setState({
      showModal: false
    });
  }
}

export default Home;