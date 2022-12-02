import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import AppRoutes from "./AppRoutes";
import DataService from '../services/DataService';


const App = (props) => {

  console.log("================================== App ======================================");

  // Init Data Service
  DataService.Init();

  // Build App
  let view = (
    <React.Fragment>
        <Router basename="/">
            <AppRoutes />
        </Router>

    </React.Fragment>
  )

  // Return View
  return view
}

export default App;
