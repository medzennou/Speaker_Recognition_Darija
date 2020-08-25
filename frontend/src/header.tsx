import { NavLink } from "react-router-dom";
import React, { ReactNode } from "react"
import {
  withStreamlitConnection,
  StreamlitComponentBase,
  Streamlit,
} from "./streamlit"
//import Contact from "./contact"
import Styles from './stream.module.css'
import img from './henceforth_logo.png'

class Header extends StreamlitComponentBase{

  public render = (): ReactNode => {
    const same = this.props.args["nom"]
  return (
    
    <nav className={Styles.header}>

        <a href="#default" className={Styles.logo}><img src={img} height="30" width="150" /></a>

        <div className={Styles.headerr}>
      <NavLink exact activeClassName={Styles.active} to="/">
        Home
      </NavLink>
      <NavLink activeClassName={Styles.active} to="/users">
        FAQ
      </NavLink>
      <NavLink activeClassName={Styles.active} to="/contact">
        Contact
      </NavLink>
      </div>
    </nav>
   
  );
}
}


export default withStreamlitConnection(Header)