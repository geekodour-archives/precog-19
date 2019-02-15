import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import UserLogin from './components/UserLogin'
import UserRegister from './components/UserRegister'

class App extends Component {
  render() {
    return (
      <div className="App">
<div class="ui segment">
You need to login to start rating!
</div>
<div class="ui placeholder segment">
  <div class="ui two column very relaxed stackable grid">
    <div class="column">
      <UserLogin/>
    </div>
    <div class="middle aligned column">
      <UserRegister/>
    </div>
  </div>
  <div class="ui vertical divider">
    Or
  </div>
</div>

      </div>
    );
  }
}

export default App;
