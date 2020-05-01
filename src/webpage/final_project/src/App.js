import React from 'react';
import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Route, Link, Redirect, Switch } from 'react-router-dom';

import Header from './components/Header';
import Home from './pages/Home';
import Page1 from './pages/Page1';
import Page2 from './pages/Page2';

function App() {
  return (
    // header
    // sidebar
    /**
     * main
     */
    <Router>
      <Header />
      <Switch>
        <Route exact path="/" component={Home} />
        <Route exact path="/page1" component={Page1} />
        <Route exact path="/page2" component={Page2} />
      </Switch>
    </Router>

  );
}

export default App;
