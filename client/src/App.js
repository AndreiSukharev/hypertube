import React, { useState, useEffect } from 'react';
import './App.css';
import 'semantic-ui-css/semantic.min.css'
import {BrowserRouter as Router, Switch, Route, Redirect } from 'react-router-dom';
import Login from './Components/Login/Login';
import Registration from './Components/Login/Registration';
// import UserPage from "./Components/Profile/UserPage";
import MoviePage from "./Components/MoviePage/MoviePage";
function App() {
  const [isLoggedIn, setLoggedIn] = useState(false);
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    const token = localStorage.getItem('token');
    let headers = {};
    if (token) {
      headers = {
        Authorization: `Bearer ${token}`,
      };
    }
    fetch('http://localhost:5000/api/secret', { headers })
      .then((res) => {
        if (res.status === 200) {
          setLoggedIn(true);
          setIsLoaded(true);
        } else {
          setIsLoaded(true);
        }
      })
      .catch((e) => {
        console.log(e);
      });
  }, []);


  return (
    <div className="App">
      <MoviePage/>
      {/*<UserPage/>*/}
{/*<Router>*/}
{/*  <Switch>*/}
{/*    <Route path="/login" render={() => (!isLoggedIn ? <Login setLogedIn={setLoggedIn} /> : <Redirect to="/" />)} />*/}
{/*    <Route path="/registration" render={() => (!isLoggedIn ? <Registration setLogedIn={setLoggedIn} /> : <Redirect to="/" />)} />*/}
    {/*<Route path="/" render={() => (isLoggedIn ? <Skeleton setLoggedIn={setLoggedIn} isLoggedIn={isLoggedIn} /> : <Redirect to="/login" />)} />*/}
  {/*</Switch>*/}
{/*</Router>*/}
    </div>
  );
}

export default App;
