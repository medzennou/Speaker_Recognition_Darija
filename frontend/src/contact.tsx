import { NavLink } from "react-router-dom";
import React, { ReactNode } from "react"
import {
  withStreamlitConnection,
  StreamlitComponentBase,
  Streamlit,
} from "./streamlit"

class Contact extends StreamlitComponentBase{

  public render = (): ReactNode => {
  return (
    <div>
    <h1>This our Contact</h1>
  </div>
  );
}
}


export default withStreamlitConnection(Contact)