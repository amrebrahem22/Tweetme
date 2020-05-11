import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import { tweetsUrl } from './constants'

class App extends React.Component {
  componentDidMount() {
    axios.get(tweetsUrl)
    .then(res => console.log(res))
    .catch(err => console.log(err))
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.
          </p>
          <a
            className="App-link"
            href="https://reactjs.org"
            target="_blank"
            rel="noopener noreferrer"
          >
            Learn React
          </a>
        </header>
      </div>
    );
  }
}

export default App;
