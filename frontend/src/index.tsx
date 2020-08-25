import React from "react"
import ReactDOM from "react-dom"
import MyComponent from "./speech_component"
import Header from "./header"
import Footer from "./footer"
import { Route, BrowserRouter as Router, Switch } from "react-router-dom"

import Contact from "./contact"

const routing = (
  <Router>
    <div>
      <Header />
      <hr />
      <Switch>
        <Route exact path="/" component={MyComponent} />
       
        <Route path="/contact" component={Contact} />
       
      </Switch>
      </div>
      <div>
    
      </div>
  
  </Router>
);
ReactDOM.render(routing, document.getElementById("root"));



