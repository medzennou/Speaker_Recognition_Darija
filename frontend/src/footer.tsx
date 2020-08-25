import { NavLink } from "react-router-dom";
import React, { ReactNode } from "react"
import {
  withStreamlitConnection,
  StreamlitComponentBase,
  Streamlit,
} from "./streamlit"

class Footer extends StreamlitComponentBase{

  public render = (): ReactNode => {
  return (
    <div>
    <h2>This is footer</h2>
  </div>
  );
}
}


export default withStreamlitConnection(Footer)