import React from 'react';

class Page1 extends React.Component {
  constructor(props) {
    super(props);
  }

  componentDidMount() { }

  render() {
    return (
      <div className="main">
        <div className="sidebar">
          <div className="sidebar-header">
            디바이스 목록
          </div>
          <div className="sidebar-main">
            <div className="sidebar-main-item">
              <p>
                Seek Shot Pro
              </p>
              <img src="assets/images/camera.jpeg" />
            </div>
          </div>
          <div className="sidebar-add-btn-div">
            <div className="sidebar-add-btn">
              + 디바이스 추가
            </div>
          </div>
        </div>
        <div className="contents">
          <div className="parent">
            <div className="child">
              <div className="contents-wrapper">
                <div className="contents-item">
                  <video width="100%" controls>
                    <source src="./assets/videos/output1.mp4" type="video/mp4" />
                  </video>
                </div>
                <div className="contents-sidebar">
                  <div style={{ width: '100%' }}>
                    <img style={{ cursor: 'pointer', width: '80%' }} src="/assets/images/rec.png" />
                  </div>
                  <div style={{ width: '100%;' }}>
                    <img style={{ cursor: 'pointer' }} width="80%" src="/assets/images/off.png" />
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
    )
  }
}

export default Page1;