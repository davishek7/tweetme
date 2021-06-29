import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {TweetsComponent} from './tweets'


const appEl=document.getElementById('root')
if (appEl){
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,appEl
  );
}
const tweetsEl=document.getElementById('tweetme')
if(tweetsEl){
  ReactDOM.render(
    <React.StrictMode>
      <TweetsComponent />
    </React.StrictMode>,tweetsEl
    );
}

reportWebVitals();
