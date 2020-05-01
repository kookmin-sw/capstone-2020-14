import React from 'react';

class Header extends React.Component {
  constructor(props) {
    super(props);

    this.toggle = this._toggle.bind(this);
  }

  componentDidMount() {
  }

  render() {
    return (
      <div className="header">
        <div className="toggle-menu" onClick={() => this.toggle()}>
          <div className="parent">
            <div className="child">
              <div className="menu">
                <div></div>
                <div></div>
                <div></div>
              </div>
            </div>
          </div>
        </div>
        <div class="parent">
          <div class="child">
            <div class="logo">
              Y<a>ou</a> O<a>nly</a> L<a>ive</a> O<a>nce</a>
            </div>
          </div>
        </div>
      </div>
    );
  }

  _toggle() {
    var node = document.getElementsByClassName('sidebar');
    console.log(node[0]);
    console.log(node[0].style.display);

    if (node[0].style.display == 'none' || node[0].style.display == '') {
      node[0].style.display = 'inline-block';
      node[0].style.width = "260px";
    } else {
      node[0].style.display = 'none';
      node[0].style.width = "0s";
    }
  }
}

export default Header;