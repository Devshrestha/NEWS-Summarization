import React from "react";
import { Route, Switch as Routes, Redirect } from 'react-router-dom';
import MainPage from "../components/MainPage";
import InterPage from "../components/InterPage";
import natPage from "../components/natPage";
import sportPage from "../components/sportPage";
import techPage from "../components/techPage";



const AppRouter = (props) => {

  console.log("================================== AppRouter ======================================");

  return (
    <React.Fragment>
      <Routes>
        <Route path="/" exact component={MainPage} />
        <Route path="/inter" exact component={InterPage} />
        <Route path="/national" exact component={natPage} />
        <Route path="/sport" exact component={sportPage} />
        <Route path="/tech" exact component={techPage} />

      </Routes>
    </React.Fragment>
  );
}

export default AppRouter;