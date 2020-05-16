import React from 'react';
import Modal from 'react-modal';
import './Home.css';
import { BASE_0, BASE_1 } from '../constatns'

import { Doughnut, Bar, Line } from 'react-chartjs-2';
import CrazyLine from '../components/CrazyLine';
import DynamicDoughnut from '../components/DynamicDoughnut';
import DynamicDoughnut2 from '../components/DynamicDoughnut2'
import DynamicLineChart from '../components/Dynamic Line Chart';

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
    right: '30%',
    bottom: '-40%',
    marginRight: '-50%',
    transform: 'translate(-50%, -50%)'
  }
};

class Home extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      dummyState: false,
      itemCount: 0,
      isShowMain: false,
      isRawVideo: false,
      isObjVideo: false,
      showModal: false,
      isPlayer1Play: false,
      player1CurrentTime: 0,
      isPlayer2Play: false,
      player2CurrentTime: 0,
      currentVideoIndex: 0,
      player1: {
        isPlay: false,
        currentTime: 0
      },
      player2: {
        isPlay: false,
        currentTime: 0
      }
    }

    this.addDevice = this._addDevice.bind(this);
    this.viewObjVideo = this._viewObjVideo.bind(this);
    this.handleOpenModal = this._handleOpenModal.bind(this);
    this.handleCloseModal = this._handleCloseModal.bind(this);

    this.showMain = this._showMain.bind(this);
    this.videoClick = this._videoClick.bind(this);

    this.player1 = React.createRef();
  }

  componentDidMount() {
    console.log('mount');
  }

  componentDidUpdate() {
    console.log('@@@@ update home');
  }

  componentWillUnmount() {
    this.player1.removeEventListener('play');
    this.player1.removeEventListener('pause');
  }

  render() {
    console.log('@@@@ render home');
    console.log(this.state.player1)
    console.log(BASE_0);
    console.log(BASE_1);

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
                        <div
                          key={index}
                          className="sidebar-main-item"
                          onClick={() => this.showMain()}>
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
              <div
                className="contents-wrapper"
                style={{ justifyContent: this.state.itemCount < 1 ? 'center' : 'space-between' }}>
                {
                  this.state.itemCount > 0 ?
                    ''
                    :
                    <>
                      <h2>선택된 디바이스가 없습니다</h2>
                    </>
                }
                {
                  /**
                   * main
                   */
                }
                {
                  this.state.isShowMain ?
                    <>
                      <div className="contents-wrapper-section">
                        <div className="contents-item" onClick={() => this.videoClick(0)}>
                          <video width="100%" controls>
                            <source src="./assets/videos/base0.mp4" type="video/mp4" />
                          </video>
                        </div>
                      </div>
                      <div className="contents-wrapper-section">
                        <div className="contents-item" onClick={() => this.videoClick(1)}>
                          <video width="100%" controls>
                            <source src="./assets/videos/base1.mp4" type="video/mp4" />
                          </video>
                        </div>
                      </div>
                    </>
                    :
                    null
                }
              </div>
            </div>
          </div>
        </div>
        <Modal
          ariaHideApp={false}
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
              <div style={{ width: '50px' }} onClick={() => this.viewObjVideo()}>
                {
                  // this.state.isObjVideo ?
                  //   <img style={{ cursor: 'pointer' }} width="80%" src="/assets/images/on.png" />
                  //   :
                  //   <img style={{ cursor: 'pointer' }} width="80%" src="/assets/images/off.png" />
                }

              </div>
              {
                (() => {
                  if (this.state.currentVideoIndex === 0) {
                    return (
                      <video
                        onLoadedMetadata={() => {
                          console.log('load..');
                          console.log(this.player1);

                          this.player1.addEventListener('play', () => {
                            console.log('play....')


                            this.setState({
                              player1: {
                                ...this.state.player1,
                                isPlay: true,
                                currentTime: Number(this.player1.currentTime.toFixed(1))
                              }
                            });
                          });

                          this.player1.addEventListener('pause', () => {
                            console.log('@@@@ player pause: ', this.player1);
                            if (this.player1 === null) return;

                            this.setState({
                              player1: {
                                ...this.state.player1,
                                isPlay: false,
                                currentTime: Number(this.player1.currentTime.toFixed(1))
                              }
                            });

                            this.setState({
                              dummyState: !this.state.dummyState
                            });

                            console.log(this.player1.currentTime);
                            this.player1.currentTime = Number(this.player1.currentTime.toFixed(1));
                            // this.player1.currentTime = 0;
                            console.log(this.player1.currentTime);
                          });

                          this.player1.addEventListener('ended', () => {
                            console.log('vidoe ended');
                            if (this.player1 === null) return;

                            this.setState({
                              player1: {
                                ...this.state.player1,
                                isPlay: false,
                                currentTime: 0
                              }
                            });
                          });
                        }}
                        ref={ref => this.player1 = ref}
                        width="100%"
                        controls>
                        <source src="./assets/videos/base0_obj.mp4" type="video/mp4" />
                      </video>
                    )
                  } else {
                    return (
                      <video
                        onLoadedMetadata={() => {
                          this.player2.addEventListener('play', () => {
                            console.log('play');
                            console.log(this.player2.currentTime);

                            this.setState({
                              player2: {
                                ...this.state.player2,
                                isPlay: true
                              }
                            });
                          });
                          this.player2.addEventListener('pause', () => {
                            if (this.player2 === null) return;
                            console.log('pause');
                            console.log(this.player2.currentTime);

                            this.setState({
                              player2: {
                                ...this.state.player2,
                                isPlay: false,
                                currentTime: Number(this.player2.currentTime.toFixed(1))
                              }
                            });
                          });

                          this.player2.addEventListener('ended', () => {
                            console.log('vidoe ended');
                            if (this.player2 === null) return;

                            this.setState({
                              player2: {
                                ...this.state.player2,
                                isPlay: false,
                                currentTime: 0
                              }
                            });
                          });
                        }}
                        ref={ref => this.player2 = ref}
                        width="100%"
                        controls>
                        <source src="./assets/videos/base1_obj.mp4" type="video/mp4" />
                      </video>
                    );
                  }
                })()
              }
            </div>
            <div>
              <div style={{ marginBottom: '30px' }}>
                <DynamicLineChart
                  playerInfo={this.state.currentVideoIndex === 0 ? this.state.player1 : this.state.player2}
                  data={this.state.currentVideoIndex === 0 ? BASE_0 : BASE_1}
                  dummy={this.state.dummy}
                />
              </div>
              <div>
                <DynamicDoughnut
                  playerInfo={this.state.currentVideoIndex === 0 ? this.state.player1 : this.state.player2}
                  data={this.state.currentVideoIndex === 0 ? BASE_0 : BASE_1}
                />
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

  _showMain() {
    this.setState({
      isShowMain: true
    });
  }

  _viewObjVideo() {
    console.log('here')
    this.setState({
      isObjVideo: !this.state.isObjVideo,
      // player1CurrentTime: this.player1.currentTim
    });

  }

  _handleOpenModal() {
    this.setState({
      showModal: true
    });
  }

  _handleCloseModal() {
    this.setState({
      showModal: false,
      player1: {
        ...this.state.player1,
        isPlay: false,
        currentTime: 0
      },
      player2: {
        ...this.state.player2,
        isPlay: false,
        currentTime: 0
      }
    });
  }

  _videoClick(id) {
    this.setState({
      showModal: true,
      currentVideoIndex: id
    });
  }
}

export default Home;