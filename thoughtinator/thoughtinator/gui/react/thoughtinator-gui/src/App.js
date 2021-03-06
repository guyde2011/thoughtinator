import React from 'react';
import ReactDOM from 'react-dom';
import logo from './logo.svg';
import API from './api/api';
import MainPage from './components/main_page'
import './App.css';
import UsersPage from './components/users_page';

var api = new API(window.api_host, window.api_port);



function App() {
  return (
    <MainPage style={{overflow: 'hidden', width: '100%', height: '100%'}}></MainPage>
  );
}

export {api}
export default App;
