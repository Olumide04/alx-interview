import React from 'react';
import './App.css';
import Notifications from '../Notifications/Notifications';
import Header from '../Header/Header';
import Login from '../Login/Login';
import Footer from '../Footer/Footer';

function App() {
  return (
    <>
    <Notifications />
    <div className="App">
      <Header />
    </div>
    <div className="App-Login">
      <Login />
    </div>
    <div className="App-footer">
      <Footer />
    </div>
    </>
  );
}

export default App;